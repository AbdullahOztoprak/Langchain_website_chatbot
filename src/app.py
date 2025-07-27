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
        <h1 style='color: #1a1a2e; margin-bottom: 0; font-family: "Outfit", sans-serif;'>AI Website Chatbot</h1>
        <p style='color: #3d246c; font-size: 1.2rem; font-family: "Outfit", sans-serif;'>Your smart assistant for any website</p>
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

    st.markdown(
        """
        <div class="custom-input-container">
            <input id="custom-input" name="input" type="text" placeholder="Type your message..." maxlength="200" autocomplete="off" />
            <button type="submit" class="custom-send-btn">Send</button>
        </div>
        """,
        unsafe_allow_html=True
    )
    submit = st.form_submit_button("Send", use_container_width=True)
    user_input = st.session_state.get('input', '')

if submit and user_input.strip():
    st.session_state['messages'].append({"role": "user", "content": user_input})
    # Placeholder for bot response (to be replaced with Langchain/OpenAI integration)
    bot_response = "I'm an AI bot. (Langchain/OpenAI integration coming soon!)"
    st.session_state['messages'].append({"role": "bot", "content": bot_response})

st.markdown(
    """
    <style>
    /* Make the very top Streamlit toolbar and header area match the app background */
    header[data-testid="stHeader"] {
        background: linear-gradient(135deg, #30cfd0 0%, #a259c6 100%) !important;
        box-shadow: none !important;
    }
    /* Remove Streamlit's default white padding above the header */
    section.main > div:first-child {
        background: linear-gradient(135deg, #30cfd0 0%, #a259c6 100%) !important;
        border-radius: 0 0 24px 24px;
        padding-top: 0 !important;
        margin-top: 0 !important;
    }
    /* Remove Streamlit's default white padding above the header */
    section.main > div:first-child {
        background: linear-gradient(135deg, #30cfd0 0%, #a259c6 100%) !important;
        border-radius: 0 0 24px 24px;
        padding-top: 0 !important;
        margin-top: 0 !important;
    }
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Outfit', sans-serif !important;
        background: linear-gradient(135deg, #1a6fa5 0%, #5e3370 100%) fixed;
        min-height: 100vh;
        color: #1a1a2e;
    }
    .stApp {
        background: linear-gradient(135deg, #1a6fa5 0%, #5e3370 100%) fixed !important;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #3d246c;
        padding: 14px 18px;
        font-size: 1.15rem;
        font-family: 'Outfit', sans-serif;
        background: #fff;
        color: #1a1a2e;
        box-shadow: 0 2px 8px rgba(48,207,208,0.08);
        margin-bottom: 0.5rem;
    }
    .stButton>button {
        background: linear-gradient(90deg, #a259c6 0%, #30cfd0 100%);
        color: white;
        border-radius: 10px;
        font-weight: bold;
        font-size: 1.1rem;
        padding: 10px 28px;
        margin-top: 8px;
        font-family: 'Outfit', sans-serif;
        border: none;
        box-shadow: 0 2px 8px rgba(48,207,208,0.08);
        transition: background 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #30cfd0 0%, #a259c6 100%);
    }
    /* Custom input container */
    .custom-input-container {
        display: flex;
        align-items: center;
        background: #fff;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(48,207,208,0.10);
        padding: 8px 12px;
        margin-bottom: 1rem;
        border: 2px solid #30cfd0;
    }
    #custom-input {
        flex: 1;
        border: none;
        outline: none;
        font-size: 1.15rem;
        font-family: 'Outfit', sans-serif;
        color: #1a1a2e;
        background: transparent;
        padding: 10px 0;
    }
    .custom-send-btn {
        background: linear-gradient(90deg, #a259c6 0%, #30cfd0 100%);
        color: #fff;
        border: none;
        border-radius: 8px;
        font-size: 1.1rem;
        font-weight: bold;
        padding: 8px 20px;
        margin-left: 10px;
        cursor: pointer;
        font-family: 'Outfit', sans-serif;
        transition: background 0.3s;
    }
    .custom-send-btn:hover {
        background: linear-gradient(90deg, #30cfd0 0%, #a259c6 100%);
    }
    /* Chat bubbles */
    .user-bubble {
        background: #30cfd0;
        color: #fff;
        border-radius: 10px;
        padding: 8px 16px;
        margin: 8px 0 8px 40px;
        text-align: right;
        font-family: 'Outfit', sans-serif;
        box-shadow: 0 2px 8px rgba(48,207,208,0.08);
    }
    .bot-bubble {
        background: #a259c6;
        color: #fff;
        border-radius: 10px;
        padding: 8px 16px;
        margin: 8px 40px 8px 0;
        text-align: left;
        font-family: 'Outfit', sans-serif;
        box-shadow: 0 2px 8px rgba(162,89,198,0.08);
    }
    .stSidebar {
        background: linear-gradient(135deg, #30cfd0 0%, #a259c6 100%) !important;
        /* Lighter turquoise and purple gradient */
    }
    </style>
    """,
    unsafe_allow_html=True
)
