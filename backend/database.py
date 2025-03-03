import chromadb
import json

# Initialize the persistent client for ChromaDB
client = chromadb.PersistentClient(path="./data")
collection = client.get_or_create_collection("eco_products")

# Load documents from the JSON file
try:
    with open("data/documents.json", "r") as file:
        documents = json.load(file)
except FileNotFoundError:
    print("Error: documents.json file not found.")
    documents = []  # Fallback to an empty list if the file is not found

# Ensure documents and metadatas have matching lengths
documents_to_add = []
metadatas_to_add = []
ids_to_add = []  # Initialize the list for IDs

for index, product in enumerate(documents):
    description = product.get("description", "No description available")
    documents_to_add.append(description)
    
    metadatas_to_add.append({
        "title": product.get("name", "Unnamed Product"),
        "tags": ", ".join(product.get("tags", [])),  # Convert list of tags to a string
        "price": product.get("price", 0),
        "currency": product.get("currency", "USD"),
        "shipping_cost": product.get("shipping_cost", 0),
        "shipping_method": product.get("shipping_method", "Standard"),
        "category": product.get("category", "General"),
        "certifications": ", ".join(product.get("certifications", []))  # Convert list of certifications to a string
    })
    
    ids_to_add.append(f"product_{index}")  # Create a unique ID for each product

def store_chat_message(user_input):
    """Store the chat message in the database."""
    # Code to store the chat message (to be implemented)
    pass

def retrieve_chat_history():
    """Retrieve chat history from the database."""
    # Code to retrieve chat history (to be implemented)
    return []

# Adding all documents and metadata at once
collection.add(
    documents=documents_to_add, 
    metadatas=metadatas_to_add,
    ids=ids_to_add  # Include the IDs
)

print("Database populated!")
