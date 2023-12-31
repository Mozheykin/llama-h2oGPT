# Project llama-h2oGPT WebSocket client

## Project description

The project is a simple WebSocket client written in Python programming language. The client is designed to communicate with the H2O.ai server and receive responses in real time.

## Installation

1. Clone the repository using the command:

   ```
   git clone https://github.com/Mozheykin/llama-h2oGPT.git
   ```

2. Navigate to the project directory:

   ```
   cd llama-h2oGPT
   ```

3. Install the dependencies specified in the `requirements.txt` file by executing the following command:

   ```
   pip install -r requirements.txt
   ```

   _Be sure you have Python and pip installed and configured._

## Usage

1. import RequestLlama from the llama-h2oGPT module:

   ```python
   from llama-h2oGPT import RequestLlama
   ```

2. Create an instance of RequestLlama and send message:

   ```python
   llh = RequestLlama()
   response = llh.get('Hello')
   ```

## Need to be eliminated:

+ To put the main model quality settings into RequestLlama class
- Add possibility to load history
- Getting fn_index in automatic mode. So far it does not get it and there is a need to get it from websocket request of the site https://llama.h2o.ai/ ![](https://i.imgur.com/yAJIivj.png)
+ Add progressbar
  
## License

[MIT License](https://github.com/Mozheykin/llama-h2oGPT/LICENSE)