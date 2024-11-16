
from .model_service import ModelService

class ChatService:
    def __init__(self, model_path: str = None):
        self.model_service = ModelService(model_path)

    def chat(self,
            messages: list,
            do_sample=True,
            max_new_tokens=256,
            temperature=0.3
        ):
        inputs = self.model_service.prepare_input(messages)

        output = self.model_service.generate_response(
            inputs,
            do_sample=do_sample,
            max_new_tokens=max_new_tokens,
            temperature=temperature
        )

        decoded_response = self.model_service.decode_response(
            output,
            inputs.input_ids.shape[1]
        )

        return decoded_response
