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

# --- Page Navigation State ---
if 'page' not in st.session_state:
    st.session_state['page'] = 'chatbot'

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

# --- Main Navigation Button ---
if st.session_state['page'] == 'chatbot':
    if st.button("📄 Internship Documentation", use_container_width=False):
        st.session_state['page'] = 'internship'
        st.rerun()

# --- Internship Documentation Page ---
if st.session_state['page'] == 'internship':
    st.markdown("## 📄 Internship Documentation Generator (English)")
    st.markdown("Fill in the following fields to generate your internship documentation. Only these three fields are required.")

    col1, col2 = st.columns([3,1])
    with col1:
        period = st.text_input("Period (e.g. July-August 2025)", key="intern_period_minimal")
        days = st.text_input("How many days", key="intern_days_minimal")
        description = st.text_area("Describe your main tasks, responsibilities, and what you learned during the internship.", key="intern_desc_minimal", height=120)
        generate_doc = st.button("Generate Internship Documentation", use_container_width=True)
    
    with col2:
        if st.button("⬅️ Back to Home", use_container_width=True):
            st.session_state['page'] = 'chatbot'
            st.rerun()

    if generate_doc and api_key and period and days and description:
        prompt = f"""
You are an expert assistant. Write a professional internship documentation in English for a student. Use the following information:

Period: {period}
Duration: {days} days
Description: {description}
Description: {description}

The documentation should be formal, clear, and suitable for an official internship report.
"""
        with st.spinner("📝 Generating your internship documentation..."):
            try:
                response = client.chat.completions.create(
                    model=model_choice,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=temperature,
                    max_tokens=1000
                )
                doc = response.choices[0].message.content
                st.markdown("### 📝 Generated Internship Documentation")
                st.text_area("Your Internship Documentation (English)", value=doc, height=350)
                st.success("You can copy and use this documentation in your internship report!")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    elif generate_doc and not api_key:
        st.error("Please enter your OpenAI API key in the sidebar.")
    elif generate_doc:
        st.error("Please fill in all fields.")
    st.stop()

# --- Chat Interface (Only show on chatbot page) ---
if 'messages' not in st.session_state:
    welcome_msg = "Welcome to your AI Website Chatbot! 🤖✨ I'm here to help you with any questions about websites, development, or anything else!"
    if api_key:
        welcome_msg += " I'm powered by OpenAI and ready to provide intelligent responses!"
    else:
        welcome_msg += " Please add your OpenAI API key in the sidebar to unlock my full AI capabilities!"
    
    st.session_state['messages'] = [
        {"role": "bot", "content": welcome_msg}
    ]

# --- Header ---
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
    
    user_input = st.text_input("Mesajınız", placeholder="Type your message...", key="user_message", label_visibility="collapsed")
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

# --- Styling ---
st.markdown("""
<style>
    .user-bubble {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        color: white;
        padding: 1rem;
        border-radius: 1rem;
        margin: 0.5rem 0;
        max-width: 80%;
        margin-left: auto;
        margin-right: 0;
    }
    
    .bot-bubble {
        background: linear-gradient(135deg, #66BB6A 0%, #388E3C 100%);
        color: white;
        padding: 1rem;
        border-radius: 1rem;
        margin: 0.5rem 0;
        max-width: 80%;
        margin-left: 0;
        margin-right: auto;
    }
    
    .input-container-wrapper {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        padding: 2px;
        border-radius: 1rem;
        margin: 1rem 0;
    }
    
    .input-container-inner {
        background: white;
        border-radius: 1rem;
        padding: 1rem;
    }
    
    .stTextInput > div > div > input {
        border: none !important;
        background: transparent !important;
        font-size: 1.1rem !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        color: white;
        border: none;
        border-radius: 0.5rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(76, 175, 80, 0.4);
    }
</style>
""", unsafe_allow_html=True)
