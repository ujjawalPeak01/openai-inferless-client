INPUT_SCHEMA = {
    "message": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["[{\"role\":\"developer\",\"content\":\"You are a helpful assistant.\"},{\"role\":\"user\",\"content\":\"Hello!\"}]"]
    },
    "temperature": {
        'datatype': 'FP32',
        'required': False,
        'shape': [1],
        'example': [0.7]
    },
    "max_length": {
        'datatype': 'INT32',
        'required': False,
        'shape': [1],
        'example': [250]
    },
    "repetition_penalty": {
        'datatype': 'FP32',
        'required': False,
        'shape': [1],
        'example': [0.5]
    },
    "top_p": {
        'datatype': 'FP32',
        'required': False,
        'shape': [1],
        'example': [0.9]
    }
}
OPENAI_CLIENT_COMPATIBLITY = True
