from langchain.llms import LlamaCpp
from config import MODEL_PATH

def load_model():
    return LlamaCpp(model_path=MODEL_PATH)