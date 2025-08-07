import streamlit as st
from PIL import Image
from openai import OpenAI
import os
from datetime import datetime

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
**Made with Streamlit**
""")

# --- AI Configuration ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 🧠 AI Settings")

# OpenAI API Key input
api_key = st.sidebar.text_input("Enter OpenAI API Key:", type="password", key="api_key")
if api_key:
    client = OpenAI(api_key=api_key)
    st.sidebar.success("✅ API Key configured!")
else:
    st.sidebar.warning("⚠️ Please enter your OpenAI API key to enable AI responses")
    client = None

# AI Model selection
model_choice = st.sidebar.selectbox(
    "Choose AI Model:",
    ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo-preview"],
    index=0
)

# AI Temperature (creativity) slider
temperature = st.sidebar.slider(
    "AI Creativity (Temperature):",
    min_value=0.0,
    max_value=2.0,
    value=0.7,
    step=0.1,
    help="Higher values make the AI more creative but less focused"
)

# Example prompts
st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Example Questions")
st.sidebar.markdown("""
**Try asking me about:**
- "How do I optimize my website for SEO?"
- "What's the best way to design a responsive layout?"
- "Explain React hooks with examples"
- "How to improve website loading speed?"
- "Write a Python function to scrape websites"
- "What are the latest web design trends?"
""")

# --- New Chat Section ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 💬 Chat Management")

if st.sidebar.button("🆕 New Chat", use_container_width=True, key="new_chat_btn"):
    # Clear all messages and start fresh
    welcome_msg = "Welcome to your AI Website Chatbot! 🤖✨"
    if api_key:
        welcome_msg += " I'm powered by OpenAI and ready to help you with any questions about websites, development, or anything else!"
    else:
        welcome_msg += " Please add your OpenAI API key in the sidebar to unlock my full AI capabilities!"
    
    st.session_state['messages'] = [
        {"role": "bot", "content": welcome_msg}
    ]
    st.rerun()

st.sidebar.markdown("---")
# --- Chat Interface ---
if 'messages' not in st.session_state:
    welcome_msg = "Welcome to your AI Website Chatbot! 🤖✨ I'm here to help you with any questions about websites, development, or anything else!"
    if 'api_key' in st.session_state and st.session_state.api_key:
        welcome_msg += " I'm powered by OpenAI and ready to provide intelligent responses!"
    else:
        welcome_msg += " Please add your OpenAI API key in the sidebar to unlock my full AI capabilities!"
    
    st.session_state['messages'] = [
        {"role": "bot", "content": welcome_msg}
    ]

# --- Header ---
# Only show header if there are no user messages yet
user_messages = [msg for msg in st.session_state['messages'] if msg['role'] == 'user']
if len(user_messages) == 0:
    st.markdown(
        """
        <link href='https://fonts.googleapis.com/css2?family=Outfit:wght@400;700&display=swap' rel='stylesheet'>
        <div class="header-container" style='text-align: center; padding: 1rem 0; font-family: "Outfit", sans-serif; transition: all 0.5s ease-in-out; opacity: 1; transform: translateY(0);'>
            <h1 style='color: #1a1a2e; margin-bottom: 0; font-family: "Outfit", sans-serif; transition: all 0.3s ease;'>AI Website Chatbot</h1>
            <p style='color: #3d246c; font-size: 1.2rem; font-family: "Outfit", sans-serif; transition: all 0.3s ease;'>Your smart assistant for any website</p>
        </div>
        """,
        unsafe_allow_html=True
    )

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
    
    # AI-powered responses using OpenAI
    if api_key and client:
        try:
            # Prepare conversation history for OpenAI
            messages_for_ai = [
                {"role": "system", "content": """You are a helpful AI assistant for a website chatbot. You are knowledgeable, friendly, and professional. 
                You can help with:
                - Website development questions
                - General programming and coding help
                - Design and UX advice
                - SEO and web optimization
                - Technical troubleshooting
                - General questions about any topic
                
                Always be helpful, concise, and provide practical advice when possible. Use emojis sparingly but appropriately to make responses engaging."""}
            ]
            
            # Add recent conversation history (last 10 messages to avoid token limits)
            recent_messages = st.session_state['messages'][-10:]
            for msg in recent_messages:
                if msg['role'] == 'user':
                    messages_for_ai.append({"role": "user", "content": msg['content']})
                else:
                    messages_for_ai.append({"role": "assistant", "content": msg['content']})
            
            # Add the current user message
            messages_for_ai.append({"role": "user", "content": user_input})
            
            # Get AI response
            with st.spinner("🤖 AI is thinking..."):
                response = client.chat.completions.create(
                    model=model_choice,
                    messages=messages_for_ai,
                    temperature=temperature,
                    max_tokens=1000
                )
                
                bot_response = response.choices[0].message.content
            
        except Exception as e:
            bot_response = f"❌ Sorry, I encountered an error: {str(e)}. Please check your API key and try again."
    
    else:
        # Fallback responses when no API key is provided
        user_message = user_input.lower()
        if "hello" in user_message or "hi" in user_message:
            bot_response = "Hello! 👋 I'm your AI website assistant. Please add your OpenAI API key in the sidebar to enable full AI capabilities!"
        elif "api" in user_message or "key" in user_message:
            bot_response = "🔑 To enable AI responses, please enter your OpenAI API key in the sidebar. You can get one from https://platform.openai.com/api-keys"
        elif "help" in user_message:
            bot_response = "I can help you with:\n• Website development\n• Programming questions\n• Design advice\n• SEO optimization\n• And much more!\n\n🔑 Add your OpenAI API key to unlock full AI capabilities!"
        else:
            bot_response = f"I'd love to help you with '{user_input}'! 🤖 Please add your OpenAI API key in the sidebar to enable intelligent AI responses."
    
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
        transition: all 0.3s ease;
    }
    
    .input-container-wrapper:hover {
        box-shadow: 0 15px 40px rgba(0,0,0,0.15);
        transform: translateY(-2px);
    }
    
    .input-container-inner {
        background: rgba(255,255,255,0.1);
        border-radius: 20px;
        padding: 15px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        transition: all 0.3s ease;
    }
    
    /* Header smooth transitions */
    .header-container {
        animation: fadeInDown 0.6s ease-out;
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
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
        border-radius: 15px;
        border: 3px solid rgba(255,255,255,0.4);
        padding: 20px 30px;
        font-size: 1.35rem;
        font-family: 'Outfit', sans-serif;
        background: #ffffff !important;
        color: #1a1a2e;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        margin-bottom: 0 !important;
        margin-top: 0 !important;
        min-height: 70px;
        height: 70px !important;
        transition: all 0.4s ease;
        width: 100%;
        box-sizing: border-box;
        line-height: 1.2;
        caret-color: #a259c6;
    }
    .stTextInput>div>div>input:focus {
        border-color: rgba(255,255,255,0.8);
        box-shadow: 0 8px 25px rgba(255,255,255,0.2);
        transform: translateY(-2px);
        outline: none;
        background: #ffffff !important;
        caret-color: #30cfd0;
    }
    .stTextInput>div>div>input::placeholder {
        color: #999;
        font-size: 1.2rem;
        font-weight: 400;
    }
    
    /* Blinking cursor animation */
    @keyframes blink {
        0%, 50% { opacity: 1; }
        51%, 100% { opacity: 0; }
    }
    
    .stTextInput>div>div>input {
        animation: none;
    }
    
    .stTextInput>div>div>input:focus {
        animation: none;
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
    
    /* New Chat Button Styling */
    .stSidebar .stButton > button {
        background: linear-gradient(90deg, #ffffff 0%, #f8f9fa 100%) !important;
        color: #1a1a2e !important;
        border: 2px solid rgba(255,255,255,0.3) !important;
        border-radius: 15px !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
        padding: 12px 20px !important;
        margin: 8px 0 !important;
        font-family: 'Outfit', sans-serif !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        min-height: 50px !important;
    }
    
    .stSidebar .stButton > button:hover {
        background: linear-gradient(90deg, #30cfd0 0%, #a259c6 100%) !important;
        color: white !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(162,89,198,0.3) !important;
        border-color: rgba(255,255,255,0.6) !important;
    }
    
    .stSidebar .stButton > button:active {
        transform: translateY(0px) !important;
        box-shadow: 0 3px 10px rgba(162,89,198,0.2) !important;
    }
    
    /* Sidebar text styling */
    .stSidebar .markdown-text-container {
        color: white !important;
    }
    
    .stSidebar h3 {
        color: white !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: bold !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
