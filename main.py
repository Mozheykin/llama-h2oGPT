import websocket
import random
import json
import string
from requests_llama import request_form 
from typing import Optional


STATE_ANALIZE = False 
FULL_ANALIZE = False
INDEX_DEF = 94

class WebSocket(websocket.WebSocketApp):
    result:Optional[str] = None
    output:Optional[dict] = None
    answer:str = ''
    index = 0

    def __init__(self, url:str, request:str, session_hash:str, message:str):
        self.index = WebSocket.index
        self.index_session = INDEX_DEF + self.index
        self.request = request
        self.session_hash = session_hash
        WebSocket.index += 1
        super().__init__(url=url, on_open=self.on_open)
        self.on_message = lambda ws, msg: self.message(ws, msg, message)
        self.on_error = lambda *args: print(f'[ERROR] Session error: {self.index_session=}, {self.session_hash=}', args)
        self.on_close = lambda *args:  print(f'[INFO] Session close: {self.index_session=}, {self.session_hash=}\n') if STATE_ANALIZE or FULL_ANALIZE else ...     
        self.run_forever()

    def on_open(self, ws):
        if STATE_ANALIZE or FULL_ANALIZE:
            print(f'[INFO] Session open: {self.index_session=}, {self.session_hash=}')
        

    def message(self, ws, msg:str, message:str):
        result = json.loads(msg)
        if FULL_ANALIZE:
            print(result)
        msg = result.get('msg')
        WebSocket.output = result.get('output')
        match msg:
            case 'send_hash':
                ws.send(json.dumps({"fn_index":self.index_session,"session_hash": self.session_hash}))
            case 'send_data':
                match self.request:
                    case 'start':
                        response = request_form(1, message=message)
                    case 'wait':
                        response = request_form(self.index+1, message=message) 
                    case _:
                        response = {'data': 'None'}
                response = response | {"fn_index":self.index_session,"session_hash": self.session_hash}
                if STATE_ANALIZE or FULL_ANALIZE:
                    print(f'[+] Response: {json.dumps(response)}')
                ws.send(json.dumps(response))
            case 'process_starts':
                pass
                # print('[INFO] Process starts')
            case 'estimation':
                pass
            case 'process_completed':
                output = result.get('output')
                if output is not None:
                    data = output.get('data')
                    genarating = output.get('is_generating')
                    if data is not None and genarating is True:
                        if len(data) > 0:
                            dialog = data[0]
                            if type(dialog) is list and len(dialog) > 0:
                                answer = dialog[0][1]
                                if answer is not None:
                                    WebSocket.answer = answer
                if STATE_ANALIZE or FULL_ANALIZE:
                    print(f"[INFO] Process completed\n {output}")
            case 'process_generating':
                pass
                if STATE_ANALIZE or FULL_ANALIZE:
                    print(f"[GENERATING] {result}")
            case _:
                print('[ERR] Error data msg')



if __name__ == "__main__":
    if FULL_ANALIZE:
        websocket.enableTrace(True)
    session_hash = ''.join( random.choice(string.ascii_lowercase + string.digits) for _ in range(11)) 
    message = input('write you question:\n\t->>> ')
    WebSocket("wss://llama.h2o.ai/queue/join", 'start', session_hash, message)
    for _ in range(9):
        WebSocket("wss://llama.h2o.ai/queue/join", 'wait', session_hash, message)
    
    print("Answer: ", WebSocket.answer)

