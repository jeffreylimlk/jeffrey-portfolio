# Jeffrey Lim — Professional Portfolio & AI Chatbot

A modern, single-page professional portfolio web application featuring an interactive AI chatbot powered by a Context-Aware Prompt Injection pipeline via the OpenAI API.

## ✨ Features

- **Professional Portfolio** — Clean, modern UI showcasing career experience, AI projects, skills, and certifications
- **AI Profile Assistant** — Interactive chatbot that answers questions about Jeffrey's background using context injected from `profile.md`
- **Multi-Turn Conversations** — Full conversation history support for natural follow-up questions
- **Premium Design** — Google Fonts, smooth animations, gradient accents, and responsive layout

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend & UI | Python (Streamlit) |
| AI Model | OpenAI API (`openai`) |
| Knowledge Base | Markdown Context (`profile.md`) |
| Environment Config | `python-dotenv` |

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- An [OpenAI API key](https://platform.openai.com/api-keys)

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd jeffrey-portfolio

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

### Running Locally

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

## 📁 Project Structure

```
jeffrey-portfolio/
├── app.py                # Main Streamlit application
├── profile.md            # Knowledge base (Jeffrey's profile)
├── jeffrey.jpg           # Profile photo
├── requirements.txt      # Python dependencies
├── .env                  # API keys (not committed)
├── .env.example          # Environment template
├── .gitignore            # Git exclusions
├── .streamlit/
│   └── config.toml       # Streamlit theme configuration
├── claude.md             # Project documentation for AI assistants
└── README.md             # This file
```

## 📝 License

This project is for personal portfolio use.
