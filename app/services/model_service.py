import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class ModelService:
    def __init__(self, model_path):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.bfloat16,
            device_map="auto"
        )

    def prepare_input(self, conversation: list):
        inputs = self.tokenizer.apply_chat_template(
            conversation=conversation,
            return_tensors='pt',
            return_dict=True,
        ).to(self.model.device)
        return inputs

    def generate_response(self,
        inputs,
        do_sample=True,
        max_new_tokens=256,
        temperature=0.01,
        ):
        with torch.no_grad():
            output = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=do_sample,
                temperature=temperature,
                eos_token_id=self.tokenizer.eos_token_id,
                pad_token_id=self.tokenizer.pad_token_id,
            )
        return output

    def decode_response(self, output, input_len=0):
        return self.tokenizer.decode(output[0][input_len:], skip_special_tokens=True)