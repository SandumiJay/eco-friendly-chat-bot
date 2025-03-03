import chromadb
import requests
def get_relevant_documents(query, knowledge_base_url):
    client = chromadb.PersistentClient(path="./data")
    collection = client.get_or_create_collection("eco_products")

    # Query the database
    # Fetch documents from the knowledge base
    response = requests.get(knowledge_base_url, params={"query": query})
    knowledge_base_documents = response.json()  # Assuming the response is in JSON format

    # Combine local and knowledge base results
    results = collection.query(query_texts=[query], n_results=3) + knowledge_base_documents
    return results["documents"]
