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

        # Ensure all numerical inputs are standard Python types
        seed = int(inputs.get("seed", 1234))  # Convert to Python int
        temperature = float(inputs.get("temperature", 0.7))  # Convert to Python float
        presence_penalty = float(inputs.get("presence_penalty", 0.5))  # Convert to Python float
        max_completion_tokens = int(inputs.get("max_completion_tokens", 256))  # Convert to Python int

        completion = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=temperature,
            messages=inputs["message"],
            presence_penalty=presence_penalty,
            max_completion_tokens=max_completion_tokens,
            seed=seed,
        )
        logging.info(completion)
        print(completion, flush=True)
        logging.info(completion.choices)
        print(completion.choices, flush=True)
        response_dict = completion.model_dump()
        return {"generated_text": response_dict}

    # Perform any cleanup activity here
    def finalize(self, args):
        self.pipe = None
