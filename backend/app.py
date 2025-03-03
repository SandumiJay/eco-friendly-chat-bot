import os
import logging
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from services.chatbot_service import get_response
from config import CHROMA_DB_DIR

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Ensure ChromaDB directory exists
os.makedirs(CHROMA_DB_DIR, exist_ok=True)

CORS(app)

@app.route("/chat", methods=["POST"])
@app.route("/chat/history", methods=["GET"])
@app.route("/chat/new", methods=["POST"])
def chat():
    """
    Handles user queries and maintains conversation context.
    """
    try:
        # Get JSON data from the request
        data = request.get_json()
        if not data or "message" not in data:
            return jsonify({"error": "No message provided"}), 400
        
        user_input = data["message"].strip()
        if not user_input:
            return jsonify({"error": "Empty message provided"}), 400

        # Store the chat message in the database (to be implemented)
        # Generate a contextual response
        # If the user requests chat history, return it (to be implemented)
        response = get_response(user_input)

        # Stream the response word by word
        def generate_response():
            for word in response.split():
                yield word + " "

        return Response(generate_response(), content_type="text/plain")

    except Exception as e:
        logger.error(f"Error processing request: {e}")
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500

if __name__ == "__main__":
    # Run in debug mode for development; disable in production
    app.run(debug=True)
