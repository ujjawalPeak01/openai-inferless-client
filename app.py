import json
import os
import numpy as np
import logging
from transformers import pipeline


class InferlessPythonModel:

    # Implement the Load function here for the model
    def initialize(self):
        self.pipe = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-360M-Instruct")

    # Function to perform inference 
    def infer(self, inputs):
        # Ensure all numerical inputs are standard Python types
        temperature = float(inputs.get("temperature", 0.7))  # Convert to Python float
        repetition_penalty = float(inputs.get("repetition_penalty", 0.5))  # Convert to Python float
        max_length = int(inputs.get("max_length", 256))  # Convert to Python int
        top_p = float(inputs.get("top_p", 0.9))

        output = self.pipe(
            inputs["message"], 
            max_length=max_length,
            temperature=temperature,
            repetition_penalty=repetition_penalty,
            top_p=top_p,
            do_sample=True
        )

        assistant_response = [
            msg for msg in output[0]['generated_text'] if msg.get("role") == "assistant"
        ]
        return {"choices": [{"message": assistant_response}]}

    # Perform any cleanup activity here
    def finalize(self, args):
        self.pipe = None
