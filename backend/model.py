class MockLlama:
    def __init__(self, model_path):
        self.model_path = model_path

    def generate(self, prompt):
        return "This is a response for the prompt: " + prompt

# Load the LLaMA model (download model first)
llm = MockLlama(model_path="./models/llama-7B.gguf")

# Load the LLaMA model (download model first)
# llm = Llama(model_path="./models/llama-7B.gguf")

def get_llm_response(query, context):
    # This function will now use the MockLlama class
    full_prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
    output = llm.generate(full_prompt)
    return output.strip()
