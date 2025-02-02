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
    "max_completion_tokens": {
        'datatype': 'INT32',
        'required': False,
        'shape': [1],
        'example': [250]
    },
    "presence_penalty": {
        'datatype': 'FP32',
        'required': False,
        'shape': [1],
        'example': [0.5]
    },
    "seed": {
        'datatype': 'INT32',
        'required': False,
        'shape': [1],
        'example': [1234]
    }
}
OPENAI_CLIENT_COMPATIBLITY = True
