import json
import os
import numpy as np
from openai import OpenAI
import logging


class InferlessPythonModel:

    # Implement the Load function here for the model
    def initialize(self):
        pass

    
    # Function to perform inference 
    def infer(self, inputs):
        OPEN_AI_API_KEY = os.environ.get("OPEN_AI_API_KEY")
        OPEN_AI_ORG_ID = os.environ.get("OPEN_AI_ORG_ID")
        openai_client = OpenAI(
            api_key=OPEN_AI_API_KEY,
            organization=OPEN_AI_ORG_ID
        )

        completion = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=inputs.get("temperature", 0.7),
            messages=inputs["message"],
            presence_penalty=inputs.get("presence_penalty", 0.5),
            max_completion_tokens=inputs.get("max_completion_tokens", 256),
            seed=inputs.get("seed", 1234),
        )
        logging.info(completion)
        logging.info(completion.choices, flush=True)
        return {"generated_text": "ABCD"}

    # perform any cleanup activity here
    def finalize(self,args):
        self.pipe = None
