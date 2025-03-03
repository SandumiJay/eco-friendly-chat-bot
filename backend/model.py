class MockLlama:
    """
    A mock implementation of a language model for testing purposes.
    """
    def __init__(self, model_path):
        self.model_path = model_path

    def generate(self, prompt):
        """
        Generates a response based on the provided prompt.
        """
        return "This is a response for the prompt: " + prompt

# Load the LLaMA model (download model first)
llm = MockLlama(model_path="./models/llama-7B.gguf")

# Uncomment the following line to load the actual LLaMA model after downloading it
# llm = Llama(model_path="./models/llama-7B.gguf")

def get_llm_response(query, context, history=None):
    """
    Generates a response using the MockLlama class, maintaining conversation history.
    """
    if history is None:
        history = []
    full_prompt = f"Context: {context}\nHistory: {history}\nQuestion: {query}\nAnswer:"
    output = llm.generate(full_prompt)
    history.append((query, output))  # Update history with the latest query and response
    return output.strip()
