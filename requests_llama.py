temperature = 0.1
max_length = 4046
max_time = 120
top_p = 0.85
top_k = 70
min_length = 0
repetition_penalty = 1.07
stream = True

def request_form(index_message:int, message:str, answer:str=''):
    predirected_message = {
                        'PreInput': 'None',
                        'PreInstruct': '<s>[INST]',
                        'PreResponse': '[/INST]',
                        'botstr': '[/INST]',
                        'chat_sep': '',
                        'chat_turn_sep': '</s>',
                        'generates_leading_space': 'false',
                        'humanstr': '[INST]',
                        'promtA': '',
                        'promtB': '',
                        'system_promt': 'None',
                        'terminate_response': ['[INST]', '</s>'],
                        }
    data_list = [
                    '',
                    '',
                    stream,
                    'llama2',
                    predirected_message,
                    temperature,
                    top_p,
                    top_k,
                    1,
                    max_length,
                    min_length,
                    False,
                    max_time,
                    repetition_penalty,
                    1,
                    False,
                    True,
                    '',
                    '',
                    'LLM',
                    True,
                    'Query',
                    [],
                    4,
                    True,
                    512,
                    'Relevant',
                    ['All'],
                    "Pay attention and remember information below, which will help to answer the question or imperative after the context ends.",
                    "According to only the information in the document sources provided within the context above, ",
                    "In order to write a concise single-paragraph or bulleted list summary, pay attention to the following text",
                    "Using only the text above, write a condensed and concise summary of key results (preferably as bullet points):",
                    "",
                    ["Caption"],
                    ["PyMuPDF"],
                    ["Unstructured"],
                    ".[]",
                    ]
    match index_message:
        case 1:
            return {"data":[None, None, message,message],"event_data":None} 
        case 2 | 4 :
            return {
                'data' : [message, *data_list, []],
                    "event_data": None,
                }
        case 3 | 5 | 6:
            return {
                'data': [],
                'event_data': None,
            }
        case 7 | 9 | 10:
            return {
                'data' : ['', *data_list, None, None, None, None, [[message, None],]],
                    "event_data": None,
            }
        case 8:
            return {
                'data' : ['', *data_list, None, None, None, None, [[message, answer],]],
                    "event_data": None,
            }
        case _:
            return dict()