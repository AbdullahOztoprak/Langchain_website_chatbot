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
    st.session_state['messages'] = [
        {"role": "bot", "content": "Welcome to your AI Website Chatbot! I'm here to help you with any questions. Try asking me about websites, development or anything else!"}
    ]

for msg in st.session_state['messages']:
    if msg['role'] == 'user':
        st.markdown(f"<div class='user-bubble'><b>🧑 You:</b> {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-bubble'><b>🤖 Bot:</b> {msg['content']}</div>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

with st.form(key="chat_form", clear_on_submit=True):
    # Create a custom container with gradient background
    st.markdown(
        """
        <div class="input-container-wrapper">
            <div class="input-container-inner">
        """,
        unsafe_allow_html=True
    )
    
    user_input = st.text_input("", placeholder="Type your message...", key="user_message", label_visibility="collapsed")
    submit = st.form_submit_button("Send", use_container_width=True)
    
    st.markdown(
        """
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

if submit and user_input.strip():
    st.session_state['messages'].append({"role": "user", "content": user_input})
    
    # Simple AI responses (you can replace this with OpenAI/Langchain later)
    user_message = user_input.lower()
    if "hello" in user_message or "hi" in user_message:
        bot_response = "Hello! 👋 I'm your AI website assistant. How can I help you today?"
    elif "how are you" in user_message:
        bot_response = "I'm doing great! Thanks for asking. I'm here to help you with any questions about websites or anything else you'd like to know!"
    elif "website" in user_message:
        bot_response = "I can help you with website-related questions! Whether it's about web development, design, SEO, or functionality - just ask!"
    elif "help" in user_message:
        bot_response = "I'm here to help! You can ask me about:\n• Website development\n• Design tips\n• Technical questions\n• General information\n\nWhat would you like to know?"
    elif "thank" in user_message:
        bot_response = "You're very welcome! 😊 Is there anything else I can help you with?"
    elif "bye" in user_message or "goodbye" in user_message:
        bot_response = "Goodbye! 👋 Feel free to come back anytime if you have more questions!"
    else:
        bot_response = f"That's an interesting question about '{user_input}'! I'm currently a demo chatbot, but I'm learning to provide better responses. Soon I'll be powered by advanced AI to give you more detailed answers!"
    
    st.session_state['messages'].append({"role": "bot", "content": bot_response})
    st.rerun()

st.markdown(
    """
    <style>
    /* Make the very top Streamlit toolbar and header area match the app background */
    header[data-testid="stHeader"] {
        background: linear-gradient(135deg, #1a6fa5 0%, #5e3370 100%) !important;
        box-shadow: none !important;
    }
    /* Remove Streamlit's default white padding above the header */
    section.main > div:first-child {
        background: linear-gradient(135deg, #1a6fa5 0%, #5e3370 100%) !important;
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
    /* Form container styling */
    .stForm {
        border: none !important;
        background: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
        min-height: 70px !important;
    }
    
    /* New input container with gradient background */
    .input-container-wrapper {
        background: linear-gradient(135deg, #1a6fa5 0%, #5e3370 100%);
        border-radius: 25px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 2px solid rgba(48,207,208,0.3);
    }
    
    .input-container-inner {
        background: rgba(255,255,255,0.1);
        border-radius: 20px;
        padding: 15px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    .stTextInput>div {
        margin-bottom: 0 !important;
        margin-top: 0 !important;
        padding: 0 !important;
        min-height: 70px !important;
        height: 70px !important;
    }
    .stTextInput>div>div {
        min-height: 70px !important;
        height: 70px !important;
        display: flex !important;
        align-items: center !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    .stTextInput>div>div>input {
        border-radius: 20px;
        border: 4px solid #30cfd0;
        padding: 20px 30px;
        font-size: 1.35rem;
        font-family: 'Outfit', sans-serif;
        background: #fff;
        color: #1a1a2e;
        box-shadow: 0 8px 25px rgba(48,207,208,0.2);
        margin-bottom: 0 !important;
        margin-top: 0 !important;
        min-height: 70px;
        height: 70px !important;
        transition: all 0.4s ease;
        width: 100%;
        box-sizing: border-box;
        line-height: 1.2;
    }
    .stTextInput>div>div>input:focus {
        border-color: #a259c6;
        box-shadow: 0 12px 35px rgba(162,89,198,0.35);
        transform: translateY(-3px);
        outline: none;
    }
    .stTextInput>div>div>input::placeholder {
        color: #999;
        font-size: 1.2rem;
        font-weight: 400;
    }
    .stButton>button {
        background: linear-gradient(90deg, #a259c6 0%, #30cfd0 100%);
        color: white;
        border-radius: 20px;
        font-weight: bold;
        font-size: 1.35rem;
        padding: 20px 45px;
        margin-top: 15px;
        font-family: 'Outfit', sans-serif;
        border: none;
        box-shadow: 0 8px 25px rgba(48,207,208,0.2);
        transition: all 0.4s ease;
        min-height: 70px;
        width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #30cfd0 0%, #a259c6 100%);
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(162,89,198,0.35);
    }
    .stButton>button:active {
        transform: translateY(-1px);
        box-shadow: 0 6px 20px rgba(162,89,198,0.25);
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
