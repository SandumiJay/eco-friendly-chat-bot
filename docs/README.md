# Application Documentation

## Overview
This application is a Flask-based chatbot service that utilizes a conversational retrieval chain to generate responses based on user input.

## Prerequisites
- Python 3.10 
- pip (Python package installer)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment**
   It is recommended to use a virtual environment to manage dependencies.
   ```bash
   python3.10 -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```

3. **Install Dependencies**
   Install the required packages using pip. Make sure you have the `requirements.txt` file in your project directory.
   ```bash
   pip install -r requirements.txt
   ```

4. Install model
   ```mkdir -p backend/models
        cd backend/models
        wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf 
  ```

5. **Configure Environment Variables**
   Ensure that any necessary environment variables are set. You may need to create a `.env` file or set them in your shell.

6. **Run the Application**
   Start the Flask application using the following command:
   ```bash
   python backend/app.py
   ```

6. **Access the Application**
   Open your web browser and navigate to `http://127.0.0.1:5000/chat` to interact with the chatbot.

## Usage
- Send a POST request to `/chat` with a JSON body containing the user message:
  ```json
  {
    "message": "Hello, how can I help you?"
  }
  ```

- You can also access chat history and other functionalities as defined in the routes.

## Troubleshooting
- If you encounter issues related to token limits, ensure that your input does not exceed the specified limits in the code (token limit 512).
- Check the logs for any error messages that may indicate what went wrong.
