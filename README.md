# 🚀 LLM Tool Calling Project

## Multi-Provider AI Assistant with OpenAI & Gemini Support

A powerful AI chatbot that demonstrates real-world LLM tool calling
using:

-   ✅ OpenAI (Paid Version)
-   ✅ Google Gemini (Free Version via API)
-   ✅ Multiple Tool Calls in a Single Conversation
-   ✅ Weather + Date Retrieval via External APIs
-   ✅ Clean Gradio UI Interface

This project showcases how to build a context-aware AI assistant that
integrates external APIs using tool/function calling.

------------------------------------------------------------------------

## ✨ Features

### 🔁 Multiple Tool Calls Support

The system can handle multiple tool calls within a single user request.

### 🌍 Weather + Date Fetching Tool

Uses: - OpenStreetMap Nominatim API (Geocoding) - Open-Meteo API
(Weather Data)

### 🧠 Context-Aware Responses

-   Calls tool only when needed
-   Keeps responses short when elaboration is unnecessary

### 🔀 Provider Flexibility

-   Use OpenAI (Paid)
-   Or use Gemini (Free Tier)

⚠️ Users must provide their own API keys for the selected provider.

------------------------------------------------------------------------

## 🏗 Project Structure

    llm-tool-calling/
    │
    ├── gemini_tool.py
    ├── openai_tool.py
    ├── requirements.txt
    ├── .gitignore
    ├── README.md
    └── .env (not tracked)

------------------------------------------------------------------------

## 🔐 Environment Variables Setup

Create a `.env` file in the root directory:

    OPENAI_API_KEY=your_openai_key_here
    GEMINI_API_KEY=your_gemini_key_here

⚠️ `.env` is ignored by Git for security reasons.

------------------------------------------------------------------------

## 🐍 Creating Python Virtual Environment

### 🖥 macOS / Linux

``` bash
# Create virtual environment
python3 -m venv venv

# Activate
source venv/bin/activate

# Deactivate
deactivate
```

### 🪟 Windows

``` bash
# Create virtual environment
python -m venv venv

# Activate (Command Prompt)
venv\Scripts\activate

# Activate (PowerShell)
venv\Scripts\Activate.ps1

# Deactivate
deactivate
```

------------------------------------------------------------------------

## 📦 Clone & Setup Project

``` bash
# Clone repository
git clone https://github.com/kapcodeO/llm-tool-calling.git
cd llm-tool-calling

# Create virtual environment
python3 -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Running the Project

``` bash
# Gemini Version (Free)
python3 gemini_tool.py

# OpenAI Version (Paid)
python3 openai_tool.py
```

The app will run on:

    http://127.0.0.1:7860

------------------------------------------------------------------------

## 🔄 How Tool Calling Works

1.  User asks for temperature.
2.  LLM detects temperature request.
3.  LLM calls `get_weather_tool`.
4.  System geocodes city and fetches temperature.
5.  Tool response is fed back into model.
6.  Final user-friendly response is generated.

Supports: - Single tool call - Multiple tool calls in same session

------------------------------------------------------------------------

## 🎯 Real-World Use Case

This system demonstrates how LLM tool calling can be used to:
- Build context-aware AI agents
- Integrate external APIs
- Handle multiple tool calls dynamically

------------------------------------------------------------------------

## 🛡 Security Notes

-   Never commit `.env`
-   Always regenerate API keys if exposed
-   Keep secrets local

------------------------------------------------------------------------

## 🧩 Tech Stack

-   Python
-   OpenAI SDK
-   Google Gemini (OpenAI-compatible endpoint)
-   Gradio
-   Open-Meteo API
-   OpenStreetMap Nominatim
-   python-dotenv

------------------------------------------------------------------------

## 👨‍💻 Author

Kapil Ojha\
AI Enthusiast \| LLM Engineering Learner \| BTech Graduate

------------------------------------------------------------------------

⭐ If you like this project, consider giving it a star on GitHub!
