import time
import json
import datetime as dt
import uuid
from pprint import pprint
from colored import fg, attr

import websocket


try:
    import thread
except ImportError:
    import _thread as thread


def on_open(ws):
    # counter = 0
    # while True:
    #     ws.send(json.dumps({
    #         'message': f'{counter}'
    #     }))
    #     counter += 1
    def run(*args):
        counter = 0
        while True:
            ws.send(json.dumps({
                'message': f'{counter}'
            }))
            print(counter)
            counter += 1

    thread.start_new_thread(run, ())


def on_message(ws, message):
    print(fg('yellow'))
    res = json.loads(message)
    pprint(res)
    print(attr('reset'))
    with open('response.json', 'w', encoding='utf-8') as file:
        json.dump(res, file)
    ws.close()


def on_error(ws, error):
    print(error)
    ws.close()


def on_close(ws, close_status_code, close_msg):
    print('*** closed ***', close_status_code, close_msg)
    ws.close()


def main():
    url = 'ws://127.0.0.1:8000/ws/chat/one/'

    ws = websocket.WebSocketApp(url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever(ping_timeout=60)




if __name__ == '__main__':
    main()
