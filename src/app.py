import streamlit as st
from PIL import Image
import requests
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

# Initialize session state for token
if 'hf_token_saved' not in st.session_state:
    st.session_state['hf_token_saved'] = ""

# Hugging Face API Token form
with st.sidebar.form(key="token_form"):
    hf_token_input = st.text_input("Enter Hugging Face API Token:", type="password", key="hf_token_input")
    token_submit = st.form_submit_button("💾 Save Token")
    
    if token_submit and hf_token_input:
        st.session_state['hf_token_saved'] = hf_token_input
        st.success("✅ Token saved successfully!")
    elif token_submit and not hf_token_input:
        st.error("⚠️ Please enter a valid token!")

# Use saved token
hf_token = st.session_state['hf_token_saved']

if hf_token:
    st.sidebar.success("✅ Hugging Face Token configured!")
else:
    st.sidebar.warning("⚠️ Please enter your Hugging Face API token to enable documentation generation.")

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
    welcome_msg = "Welcome to your AI Website Chatbot! 🤖✨ I'm here to help you with any questions about websites, development, or anything else!"
    
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
        days = st.text_input("How many days?", key="intern_days_minimal")
        description = st.text_area("Describe your main tasks, responsibilities, and what you learned during the internship.", key="intern_desc_minimal", height=120)
        generate_doc = st.button("Generate Internship Documentation", use_container_width=True)

    with col2:
        if st.button("⬅️ Back to Home", use_container_width=True):
            st.session_state['page'] = 'chatbot'
            st.rerun()

    if generate_doc and period and days and description:
        with st.spinner("📝 Generating your internship documentation..."):
            try:
                # Generate document using local template
                internship_doc = f"""
# INTERNSHIP DOCUMENTATION

## Period: {period}
## Duration: {days} days

### Introduction
I completed an internship during {period}, which lasted for {days} days. The internship provided valuable practical experience and professional development opportunities.

### Main Tasks and Responsibilities
During this internship, I was involved in the following activities:
{description}

### Skills Developed
Through this internship, I developed several key skills:
- Technical knowledge in the related field
- Professional communication
- Time management
- Problem-solving
- Teamwork and collaboration

### Conclusion
This internship has been extremely valuable for my professional development. I gained practical experience that complemented my academic knowledge and provided me with insights into real-world professional environments.

### Acknowledgments
I would like to thank my supervisors and colleagues for their guidance and support throughout this internship.
                """
                
                st.markdown("### 📝 Generated Internship Documentation")
                st.text_area("Your Internship Documentation (English)", value=internship_doc, height=350)
                st.success("You can copy and use this documentation in your internship report!")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    elif generate_doc and not hf_token:
        st.error("Please enter your Hugging Face API token in the sidebar.")
    elif generate_doc:
        st.error("Please fill in all fields.")
    st.stop()

# --- Chat Interface (Only show on chatbot page) ---
if 'messages' not in st.session_state:
    welcome_msg = "Welcome to your AI Website Chatbot! 🤖✨ I'm here to help you with any questions about websites, development, or anything else!"
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
    # Only append user message once
    if not st.session_state['messages'] or st.session_state['messages'][-1]['content'] != user_input:
        st.session_state['messages'].append({"role": "user", "content": user_input})
    # Fallback responses since OpenAI is not used
    user_message = user_input.lower()
    if "hello" in user_message or "hi" in user_message:
        bot_response = "Hello! 👋 I'm your AI website assistant."
    elif "api" in user_message or "key" in user_message:
        bot_response = "🔑 To enable AI responses, please use the internship documentation generator with your Hugging Face token."
    elif "help" in user_message:
        bot_response = "I can help you with:\n• Website development\n• Programming questions\n• Design advice\n• SEO optimization\n• And much more!"
    else:
        bot_response = f"I'd love to help you with '{user_input}'! 🤖 Please use the internship documentation generator for AI-powered text."
    st.session_state['messages'].append({"role": "bot", "content": bot_response})
    st.rerun()
