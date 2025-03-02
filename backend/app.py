from flask import Flask, request, jsonify
from retriever import get_relevant_documents
from model import get_llm_response

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    user_query = data.get("query")

    # Retrieve relevant documents
    relevant_docs = get_relevant_documents(user_query)

    # Generate AI response
    response = get_llm_response(user_query, relevant_docs)

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
