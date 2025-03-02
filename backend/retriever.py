import chromadb

def get_relevant_documents(query):
    client = chromadb.PersistentClient(path="./data")
    collection = client.get_or_create_collection("eco_products")

    # Query the database
    results = collection.query(query_texts=[query], n_results=3)
    return results["documents"]
