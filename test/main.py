import os
import sys
sys.path.append(os.getcwd())
from packageLlama2 import RequestLlama

llama = RequestLlama(INDEX=102, temperature=0.1, progress_=True)
message = ''
while not message == 'exit':
    message = input('Write message for Llama2:\n\t --->>> ')
    print(llama.get(message=message))
