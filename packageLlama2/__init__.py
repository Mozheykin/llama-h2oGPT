from typing import Optional
from .main import WebSocket
import random
import string
from .requests_llama import SettingsModel
from progress.bar import ChargingBar

class RequestLlama:
    def __init__(self, INDEX:int=94, temperature:float=0.2, max_length:int=512, 
                min_length:int=0, max_time:int=120, top_p:float=0.85, 
                top_k:int=70, repetition_penalty:float=1.07, stream:bool=True, progress_:bool=False) -> None:
        self.settings = SettingsModel(temperature, max_length, max_time, top_p, 
                                    top_k, min_length,repetition_penalty, stream)
        self.session_hash = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(11)) 
        self.progress_ = progress_
        self.INDEX = INDEX
    
    def get(self, message:str) -> Optional[str]:
        if self.progress_:
            with ChargingBar('Processing', max=9) as bar:
                self._first_request(message)
                bar.next()
                answer = None
                for _ in range(9):
                    answer = self._request(message)
                    bar.next()
                return answer
        else:
            self._first_request(message)
            answer = None
            for _ in range(9):
                answer = self._request(message)
            return answer
    
    def _first_request(self, message:str):
        WebSocket("wss://llama.h2o.ai/queue/join", 'start', self.session_hash, message, self.settings, self.INDEX)
    
    def _request(self, message:str) -> Optional[str]:
        WebSocket("wss://llama.h2o.ai/queue/join", 'wait', self.session_hash, message, self.settings, self.INDEX)
        return WebSocket.answer
