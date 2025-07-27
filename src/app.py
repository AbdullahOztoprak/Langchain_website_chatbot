import streamlit as st
from PIL import Image

# --- Page Config ---
st.set_page_config(
    page_title="AI Website Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
# --- Sidebar ---
st.sidebar.title("🤖 AI Website Chatbot")
st.sidebar.markdown("""
Welcome! This is a creative, professional chatbot interface powered by Langchain & OpenAI.

- Ask anything about the website
- Get instant, AI-powered answers
---
**Made with ❤️ using Streamlit**
""")
# --- Header ---
# --- Header ---
st.markdown(
    """
    <link href='https://fonts.googleapis.com/css2?family=Outfit:wght@400;700&display=swap' rel='stylesheet'>
    <div style='text-align: center; padding: 1rem 0; font-family: "Outfit", sans-serif;'>
        <h1 style='color: #30cfd0; margin-bottom: 0; font-family: "Outfit", sans-serif;'>AI Website Chatbot</h1>
        <p style='color: #a259c6; font-size: 1.2rem; font-family: "Outfit", sans-serif;'>Your smart assistant for any website</p>
    </div>
    """,
    unsafe_allow_html=True
)
# --- Chat Interface ---
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
chat_container = st.container()
with chat_container:
    for msg in st.session_state['messages']:
        if msg['role'] == 'user':
            st.markdown(f"<div class='user-bubble'><b>🧑 You:</b> {msg['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-bubble'><b>🤖 Bot:</b> {msg['content']}</div>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message...", "", key="input")
    submit = st.form_submit_button("Send")

if submit and user_input.strip():
    st.session_state['messages'].append({"role": "user", "content": user_input})
    # Placeholder for bot response (to be replaced with Langchain/OpenAI integration)
    bot_response = "I'm an AI bot. (Langchain/OpenAI integration coming soon!)"
    st.session_state['messages'].append({"role": "bot", "content": bot_response})

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Outfit', sans-serif !important;
        background: linear-gradient(135deg, #30cfd0 0%, #a259c6 100%) fixed;
        min-height: 100vh;
    }
    .stApp {
        background: linear-gradient(135deg, #30cfd0 0%, #a259c6 100%) fixed !important;
    }
    .stTextInput>div>div>input {
        border-radius: 8px;
        border: 1.5px solid #a259c6;
        padding: 10px;
        font-size: 1.1rem;
        font-family: 'Outfit', sans-serif;
        background: #e0f7fa;
        color: #222;
    }
    .stButton>button {
        background: linear-gradient(90deg, #a259c6 0%, #30cfd0 100%);
        color: white;
        border-radius: 8px;
        font-weight: bold;
        font-size: 1.1rem;
        padding: 8px 24px;
        margin-top: 8px;
        font-family: 'Outfit', sans-serif;
        border: none;
    }
    /* Chat bubbles */
    .user-bubble {
        background: #30cfd0;
        color: white;
        border-radius: 10px;
        padding: 8px 16px;
        margin: 8px 0 8px 40px;
        text-align: right;
        font-family: 'Outfit', sans-serif;
        box-shadow: 0 2px 8px rgba(48,207,208,0.08);
    }
    .bot-bubble {
        background: #a259c6;
        color: white;
        border-radius: 10px;
        padding: 8px 16px;
        margin: 8px 40px 8px 0;
        text-align: left;
        font-family: 'Outfit', sans-serif;
        box-shadow: 0 2px 8px rgba(162,89,198,0.08);
    }
    .stSidebar {
        background: #e0f7fa !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
