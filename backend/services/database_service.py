from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from config import CHROMA_DB_DIR, EMBEDDING_MODEL

def initialize_vector_store():
    embedding_function = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    return Chroma(persist_directory=CHROMA_DB_DIR, embedding_function=embedding_function)
