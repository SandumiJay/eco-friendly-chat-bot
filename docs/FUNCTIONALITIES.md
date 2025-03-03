# Application Functionalities

## Overview
This application is a Flask-based chatbot service that utilizes a conversational retrieval chain to generate responses based on user input.

## Key Services
- **Chatbot Service**: Handles user queries and generates responses using the language model.
- **Database Service**: Manages interactions with the Chroma database for storing and retrieving documents.
- **Model Service**: Interfaces with the language model to process and generate text.

## User Interaction
Users can interact with the chatbot by sending POST requests to the `/chat` endpoint with a JSON body containing their message. The chatbot will respond with generated text based on the input.

## Additional Features
- Access to chat history.
- Ability to handle various types of queries related to eco-friendly products.

## Future Improvements
- Integration of more advanced language models.
- Enhanced user interface for better interaction.
