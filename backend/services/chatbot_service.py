from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.document_loaders import WebBaseLoader
from services.model_service import load_model
from config import EMBEDDING_MODEL

# Load model and vector store
llm = load_model()

try:
    embedding_function = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
except Exception as e:
    print(f"Error loading embeddings: {e}")
    exit()

# Load and process website data
url = "https://organicnation.co.nz/"
loader = WebBaseLoader(url)
documents = loader.load()
print(f"Loaded {len(documents)} documents from {url}")

def split_doc(documents, chunk_size=100, chunk_overlap=0): 
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", "(?<=\. )"]
    )
    splits = splitter.split_documents(documents)
    return splits

chunks = split_doc(documents)
print(f"Split into {len(chunks)} chunks")

# Initialize Chroma vector store
vector_store = Chroma.from_documents(chunks, embedding_function, persist_directory="./chroma_db")
retriever = vector_store.as_retriever()
print("Vector store initialized")

# Initialize conversation memory
memory = ConversationBufferWindowMemory(memory_key="chat_history", return_messages=True)

# Define CoT-enhanced prompt template
cot_prompt = PromptTemplate(
    input_variables=["chat_history", "question", "context"],
    template="""
You are an intelligent AI assistant capable of deep reasoning and maintaining conversation history.

## Previous Conversation:
{chat_history}

## Relevant Information from Knowledge Base:
{context}

## User's Question:
{question}

## Think step by step before answering:
1. Identify the main topic in the user's question.
2. Retrieve relevant background information from the knowledge base (provided above).
3. Analyze the retrieved information and reason logically.
4. Provide a structured, informative response.

## Final Answer:
"""
)

# Create conversational retrieval chain
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory,
    combine_docs_chain_kwargs={"prompt": cot_prompt}
)
print("Conversational chain initialized")

def fetch_knowledge_base_data(question):
    loaded_vectordb = Chroma(persist_directory="./chroma_db", embedding_function=embedding_function)
    docs = loaded_vectordb.max_marginal_relevance_search(question, k=4)
    print(f"Fetched {len(docs)} docs for question: {question}")
    return " ".join([chunk.page_content for chunk in docs])

def get_response(user_input, store_chat=True):
    """Generate a response using Chain of Thought (CoT) reasoning."""
    question = user_input.strip()

    # Store the chat message in the database if required
    if store_chat:
        # Code to store the chat message (to be implemented)
        pass
    print(f"Processing question: {question}")
    print(f"Chat History: {memory.load_memory_variables({})}")

    # Clear memory if requested (this will also clear chat history)
    if question.lower() == "start new chat":
        memory.clear()
        return "Chat history cleared. How can I assist you now?"

    # Token limit check
    if len(question.split()) > 2048:
        return "Error: Input exceeds the maximum token limit of 2048."

    # Invoke the chain
    try:
        response = qa_chain.invoke({"question": question})
        print(f"Raw response: {response}")
    except Exception as e:
        print(f"Error in chain invocation: {e}")
        raise

    # Extract the answer
    answer = response.get("answer", "I'm sorry, but I couldn't find relevant information. Can you clarify?")
    print(f"Extracted answer: {answer}")
    
    # Handle empty responses
    if not answer.strip():
        answer = "I'm sorry, but I couldn’t find relevant information. Can you clarify?"

    return answer
