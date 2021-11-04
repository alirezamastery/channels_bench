import time
import json
import datetime as dt
import uuid
from pprint import pprint
from colored import fg, attr
import concurrent.futures

import websocket


try:
    import thread
except ImportError:
    import _thread as thread


def on_open(ws):
    ws.send(json.dumps({
        'message': f'{time.time()}'
    }))


def on_message(ws, message):
    print(fg('yellow'))
    res = json.loads(message)
    pprint(res)
    print(attr('reset'))
    ws.close()


def on_error(ws, error):
    print(error)
    ws.close()


def on_close(ws, close_status_code, close_msg):
    print('*** closed ***', close_status_code, close_msg)
    ws.close()


def websocket_client():
    url = 'ws://127.0.0.1:8000/ws/chat/one/'

    ws = websocket.WebSocketApp(url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever(ping_timeout=60)


def main():
    connections = 2
    with concurrent.futures.ProcessPoolExecutor() as executor:
        [executor.submit(websocket_client) for _ in range(connections)]


if __name__ == '__main__':
    main()
