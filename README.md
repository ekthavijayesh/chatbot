# 💬 Ektha AI — Personal AI Chatbot

Ektha AI is a simple, interactive AI chatbot built using Python and Streamlit. It uses OpenRouter and LangChain to generate AI-powered responses and provide a conversational experience through a web-based interface.

## ✨ Features

- 💬 **Interactive Chat:** Ask questions and receive AI-generated responses.
- 🧠 **AI-Powered Responses:** Uses an OpenRouter language model through LangChain.
- 🔄 **Conversation History:** Maintains chat messages during the current session.
- 🗑️ **Clear Conversation:** Clear the current conversation with one click.
- 🌐 **Web-Based Interface:** Chat through a simple Streamlit application.
- 🔐 **Environment-Based API Key:** Reads the API key from an environment variable instead of hardcoding it in the source code.

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Streamlit** — Web application interface
- **LangChain** — Connects the application to the language model
- **OpenRouter** — Provides access to AI language models
- **Git and GitHub** — Version control and project hosting

## 📁 Project Structure

```text
chatbot-ektha/
│
├── app.py              # Streamlit chatbot interface
├── chatbot.py          # Python chatbot script
├── README.md           # Project documentation
└── .gitignore          # Files excluded from Git
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/chatbot-ektha.git
cd chatbot-ektha
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install streamlit langchain-openrouter
```

### 4. Configure the OpenRouter API Key

Create an API key through [OpenRouter](https://openrouter.ai/settings/keys).

Set the key in PowerShell:

```powershell
$env:OPENROUTER_API_KEY="YOUR_API_KEY"
```

Replace `YOUR_API_KEY` with your actual key. Never upload your API key to GitHub or share it publicly.

### 5. Run the Application

```bash
python -m streamlit run app.py
```

Open the local URL shown in your terminal, usually:

```text
http://localhost:8501
```

## 🧠 How It Works

1. The user enters a message through the Streamlit chat interface.
2. The application stores messages in Streamlit session state.
3. LangChain formats the conversation as chat messages.
4. The conversation is sent to the configured OpenRouter language model.
5. The model generates a response.
6. The response is displayed in the chat interface.

## 🔒 Security

- Keep API keys private.
- Store the API key in an environment variable.
- Never commit `.env` files or API credentials to GitHub.
- If an API key is exposed, revoke it and generate a replacement.

## 🚀 Future Improvements

- 🎨 Improve the interface with custom styling and animations.
- 💾 Add persistent conversation storage.
- 📄 Support document uploads and question answering.
- 🗣️ Add voice input and text-to-speech.
- 🌍 Deploy the chatbot online so others can use it.

## 👩‍💻 Author

Created as a personal AI chatbot project to explore Python, large language models, LangChain, and Streamlit.

## 📜 License

This project is available for learning and educational purposes. Add a license file if you wish to specify formal reuse and distribution terms.
