from typing import Optional
from main import WebSocket
import random
import string


class RequestLlama:
    def __init__(self, ) -> None:
        self.session_hash = ''.join( random.choice(string.ascii_lowercase + string.digits) for _ in range(11)) 
    
    def get(self, message:str) -> Optional[str]:
        WebSocket("wss://llama.h2o.ai/queue/join", 'start', self.session_hash, message)
        for _ in range(9):
            WebSocket("wss://llama.h2o.ai/queue/join", 'wait', self.session_hash, message)
        
        return WebSocket.answer