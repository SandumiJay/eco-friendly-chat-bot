import streamlit as st
import requests
import time
import emoji

# Streamlit UI Setup
st.set_page_config(page_title="AI Chatbot for EcoShop", layout="wide")
st.title("🌴 AI Chatbot for EcoShop")

# Flask API Endpoint
API_URL = "http://127.0.0.1:5000/chat"

# Sidebar for New Chat and Other Options
with st.sidebar:
    st.header("Options")
    if st.button("Start New Chat"):
        st.session_state.messages.clear()

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History with Timestamp
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        timestamp = time.strftime('%H:%M:%S', time.gmtime(msg["timestamp"]))
        st.markdown(f"**{timestamp}** - {msg['content']}")

# Add padding at the bottom of the page to prevent overlap with chat input
st.markdown("""
    <style>
    .css-ffhzg2 {
        padding-bottom: 120px;  /* Ensure space for the input box */
    }
    </style>
""", unsafe_allow_html=True)

# Initialize user input session state
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# User Input Box with Enter Button Icon
user_input = st.text_input("Ask me anything...", value=st.session_state.user_input)

# Layout with columns to arrange input box and button
col1, col2 = st.columns([4, 1])

with col2:
    # Adding the "Enter" Button with a send icon
    enter_button = st.button(emoji.emojize(":rocket: Send"))

if enter_button and user_input:
    # Add User Message to Chat History
    st.session_state.messages.append({"role": "user", "content": user_input, "timestamp": time.time()})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Show Loading Animation While Waiting for Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response_text = ""
        message_placeholder.markdown("**Loading...**")

        # Get AI Response from Flask API
        try:
            with requests.post(API_URL, json={"message": user_input}, stream=True) as r:
                for chunk in r.iter_content(chunk_size=1024):
                    response_text += chunk.decode()
                    message_placeholder.markdown(response_text)
        except requests.exceptions.RequestException as e:
            message_placeholder.markdown("**Error occurred while fetching response**")

        # Add Assistant's Response to Chat History
        st.session_state.messages.append({"role": "assistant", "content": response_text, "timestamp": time.time()})

    # Clear the input field after sending the message
    st.session_state.user_input = ""  # Clear input after submitting
