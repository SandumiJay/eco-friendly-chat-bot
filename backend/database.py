import chromadb
import json

client = chromadb.PersistentClient(path="./data")
collection = client.get_or_create_collection("eco_products")

with open("data/documents.json", "r") as file:
    documents = json.load(file)

ids = [str(i) for i in range(len(documents))]  # Generate unique IDs as strings
for i, doc in enumerate(documents):
    tags_string = ', '.join(doc["tags"])  # Convert list of tags to a string
    collection.add(documents=[doc["description"]], metadatas=[{"title": doc["title"], "tags": tags_string}], ids=[ids[i]])

print("Database populated!")
