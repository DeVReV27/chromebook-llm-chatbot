import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Ensure the API key is loaded
if not openai_api_key:
    st.error("API key not found. Please ensure it is set in the .env file.")
    st.stop()

# OpenAI API setup
client = OpenAI(api_key=openai_api_key)

# Personalities
PERSONALITIES = {
    "Normal": "Respond as a polite and helpful assistant.",
    "Brainy": "Provide detailed and intellectual explanations.",
    "Mean": "Respond sarcastically and rudely.",
    "Cat": "Respond only in variations of 'Meow'."
}

def get_chat_response(prompt, temperature, personality):
    """Fetch response from OpenAI based on personality."""
    if personality == "Cat":
        # Generate cat-like responses
        return " ".join(["Meow"] * (len(prompt) % 10 + 1))  # Randomized "Meow" length
    else:
        system_message = {"role": "system", "content": PERSONALITIES[personality]}
        user_message = {"role": "user", "content": prompt}
        
        try:
            response = client.chat.completions.create(
                model="gpt-4",  # Adjust to your desired model version
                temperature=temperature,
                messages=[system_message, user_message]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

# Streamlit App
st.title("Chromebook LLM Chatbot")
st.subheader("Chat with your AI assistant. Adjust settings below.")

# Sidebar Settings
st.sidebar.header("Settings")
temperature = st.sidebar.slider("Response Creativity (Temperature)", 0.0, 1.0, 0.7)
personality = st.sidebar.selectbox("Choose Personality", list(PERSONALITIES.keys()))

# Chat Interface
user_input = st.text_input("You:", placeholder="Type your message here...")
if user_input:
    with st.spinner("Generating response..."):
        response = get_chat_response(user_input, temperature, personality)
    st.text_area("Chromebook LLM:", value=response, height=200, disabled=True)

# Footer
st.markdown(
    """
    ---
    **Chromebook LLM** | Powered by Computers 
    Developed with ❤️ by Macierai
    """
)
