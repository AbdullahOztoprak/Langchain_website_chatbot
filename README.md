# Industrial Automation AI Assistant 🚀🤖

> This project was developed as a showcase for an industrial automation AI internship application. It demonstrates skills in software design, implementation, debugging, unit/module testing, test automation, and release tasks for industrial automation projects. The solution leverages state-of-the-art AI models (LLMs), LangChain, and modern web technologies (Streamlit, FastAPI) to create a professional chatbot focused on industrial/building automation topics.
>
> **Key responsibilities and qualifications addressed in this project:**
> - Applied AI for industrial/building automation
> - LLM-based solution development (LangChain, OpenAI)
> - Frontend/backend development (Streamlit, FastAPI)
> - Test automation and modular architecture
> - Research and prototyping with real industrial documentation
> - Passion for new technologies and tools

# AI Website Chatbot 🤖✨

A beautiful, professional AI-powered chatbot interface built with Streamlit and OpenAI. This intelligent chatbot can help you with website development, programming questions, design advice and much more!

## Features

- **AI-Powered Responses**: Powered by OpenAI's GPT models 
- **Beautiful UI**: Modern gradient design with glass morphism effects
- **⚙Customizable AI Settings**: Adjust model selection and creativity levels
- **Smart Chat Management**: Create new conversations with one click
- **Responsive Design**: Works perfectly on desktop and mobile
- **Secure API Key Input**: Safe, encrypted API key handling
- **Smooth Animations**: Professional transitions and hover effects

## ⚡️ Quick Installation & Run (Optimized for Low Resource PCs)

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/your-username/Langchain_website_chatbot.git
cd Langchain_website_chatbot

# Install only essential dependencies
python -m pip install streamlit openai python-dotenv
```

### 2. Get OpenAI API Key

1. Visit [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Create a new API key
3. Copy your API key

### 3. Run the Application

```bash
# Run the Streamlit app (no heavy backend)
streamlit run src/app.py
# Alternatif: python -m streamlit run src/app.py
```

### 4. Configure AI

1. Open your browser to `http://localhost:8501`
2. Enter your OpenAI API key in the sidebar
3. Start chatting!

## 🛠️ Configuration

### AI Models Available:
- **GPT-3.5-turbo**: Fast and cost-effective
- **GPT-4**: More capable, higher quality responses
- **GPT-4-turbo**: Latest and most advanced model

### Temperature Settings:
- **0.0-0.3**: More focused and deterministic
- **0.4-0.7**: Balanced creativity and accuracy
- **0.8-2.0**: More creative and varied responses

## 🗂️ Project Structure & Technical Details

```
Langchain_website_chatbot/
├── src/
│   ├── app.py                # Main Streamlit application (UI)
│   ├── api/                  # FastAPI backend (optional, for advanced use)
│   │   ├── __init__.py
│   │   └── endpoints.py      # REST API endpoints for industrial automation
│   ├── models/               # LLM and RAG modules
│   │   ├── __init__.py
│   │   ├── llm_utils.py      # LLM helper functions (LangChain, OpenAI)
│   │   └── rag.py            # Retrieval Augmented Generation (RAG) implementation
│   ├── data/
│   │   └── industrial_docs/  # Sample industrial automation documents (txt/pdf)
│   └── utils/
│       ├── __init__.py
│       └── helpers.py        # Utility functions (validation, formatting, etc.)
├── tests/
│   ├── __init__.py
│   └── test_llm_utils.py     # Unit tests for LLM utilities
├── requirements.txt          # Python dependencies
├── .env.template             # Environment variables template
└── README.md                 # Project documentation
```

### Technologies Used
- **Streamlit**: Interactive web UI for chatbot
- **OpenAI API**: LLM-powered responses
- **LangChain**: Advanced LLM orchestration and RAG
- **FastAPI**: Optional backend for REST API
- **ChromaDB**: Vector database for document retrieval
- **Python-dotenv**: Secure environment variable management
- **PyPDF**: Industrial document processing

## 💡 Example Questions (Industrial Automation Focus)

Try asking the AI about:
- "How do I implement a PID control loop in a PLC?"
- "What are the best practices for SCADA security?"
- "How can I integrate OPC UA with my IoT platform?"
- "What's the difference between BACnet and KNX protocols?"
- "How to design an MES that integrates with SAP?"
- "What sensors are typically used in predictive maintenance?"
- "Explain the main components of a Building Automation System."
- "How can I optimize energy usage in smart factories?"
- "What are the latest trends in industrial automation?"
- "How do I secure industrial networks against cyber threats?"

## 🎨 Features Showcase

### Beautiful Design
- Modern gradient backgrounds
- Glass morphism input containers
- Smooth animations and transitions
- Professional typography with Outfit font

### Smart AI Integration
- Conversation history context
- Customizable AI personality
- Error handling and fallback responses
- Real-time response generation

### User Experience
- Dynamic header that disappears after first message
- One-click new chat functionality
- Visual feedback during AI processing
- Mobile-responsive design


## 📄 License

This project is open source and available under the MIT License.

## 🧪 Testing & Test Automation

Unit and module tests are provided to ensure code reliability and maintainability. You can run all tests with:

```bash
python -m unittest discover tests
```

- All core logic (LLM helpers, utility functions) are covered by tests.
- You can add more tests in the `tests/` directory for new features.
- Test automation is recommended for professional development and CI/CD.
