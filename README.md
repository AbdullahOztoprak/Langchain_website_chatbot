# AI Website Chatbot 🤖✨

A beautiful, professional AI-powered chatbot interface built with Streamlit and OpenAI. This intelligent chatbot can help with website development, programming questions, design advice, and much more!

## 🌟 Features

- **AI-Powered Responses**: Powered by OpenAI's GPT models 
- **Beautiful UI**: Modern gradient design with glass morphism effects
- **⚙Customizable AI Settings**: Adjust model selection and creativity levels
- **Smart Chat Management**: Create new conversations with one click
- **Responsive Design**: Works perfectly on desktop and mobile
- **Secure API Key Input**: Safe, encrypted API key handling
- **Smooth Animations**: Professional transitions and hover effects

## To Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/your-username/Langchain_website_chatbot.git
cd Langchain_website_chatbot

# Install dependencies
pip install -r requirements.txt
```

### 2. Get OpenAI API Key

1. Visit [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Create a new API key
3. Copy your API key

### 3. Run the Application

```bash
# Navigate to the src directory
cd src

# Run the Streamlit app
streamlit run app.py
```

### 4. Configure AI

1. Open your browser to `http://localhost:8501`
2. Enter your OpenAI API key in the sidebar
3. Choose your preferred AI model and settings
4. Start chatting!

## 🛠️ Configuration

### AI Models Available:
- **GPT-3.5-turbo**: Fast and cost-effective
- **GPT-4**: More capable, higher quality responses
- **GPT-4-turbo**: Latest and most advanced model

### Temperature Settings:
- **0.0-0.3**: More focused and deterministic
- **0.4-0.7**: Balanced creativity and accuracy
- **0.8-2.0**: More creative and varied responses

## 📁 Project Structure

```
Langchain_website_chatbot/
├── src/
│   └── app.py              # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env.template          # Environment variables template
└── README.md              # This file
```

## 🔧 Environment Variables (Optional)

Create a `.env` file based on `.env.template`:

```env
OPENAI_API_KEY=your_openai_api_key_here
DEFAULT_MODEL=gpt-3.5-turbo
DEFAULT_TEMPERATURE=0.7
```

## 💡 Example Questions

Try asking the AI about:
- "How do I optimize my website for SEO?"
- "What's the best way to design a responsive layout?"
- "Explain React hooks with examples"
- "How to improve website loading speed?"
- "Write a Python function to scrape websites"
- "What are the latest web design trends?"

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

## 🔄 Future Enhancements

- [ ] Website scraping with LangChain
- [ ] File upload capability
- [ ] Chat history persistence
- [ ] Multiple conversation threads
- [ ] Voice input/output
- [ ] Custom AI personas


## 📄 License

This project is open source and available under the MIT License.
