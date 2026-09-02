# Agentic AI Weather Assistant 🌤️🤖

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Powered-green?logo=chainlink)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

An intelligent, conversational weather assistant built with **LangChain** and **Ollama** (local LLMs). The agent answers natural-language weather queries, remembers the full conversation history across sessions, and stores every chat in a JSON file for later reference.

---

## 📌 Features

- **Local LLM Powered**: Runs entirely on-device using [Ollama](https://ollama.com/) — no cloud API keys needed.
- **Conversational Memory**: Persists chat history per session using `FileChatMessageHistory`, so the assistant remembers past messages across runs.
- **Natural Language Weather Summaries**: Returns concise weather info — Temperature, Humidity, Rainfall probability, Wind speed & direction.
- **Multi-Session Support**: Each session gets its own JSON history file, keeping conversations isolated and reproducible.
- **Simple CLI Interface**: Lightweight terminal chat loop — just type your city and get an answer.

---

## 📁 Project Structure

```text
Agentic-ai-whether/
│
├── Whether.py               # Basic single-query weather agent (LangChain + Ollama)
├── Store_history/
│   └── history.py           # Full conversational agent with persistent session history
├── chat_history.json        # Sample stored chat history (default session)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## ⚡ Quick Start

### 1. Prerequisites

- **Python**: `3.9+`
- **[Ollama](https://ollama.com/)** installed and running locally
- A supported model pulled, e.g.:

```bash
ollama pull qwen2.5:7b
# or
ollama pull qwen3.5:4b
```

### 2. Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/shethhetvi/Agentic-ai-whether.git
cd Agentic-ai-whether

# (Optional) Create & activate a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 3. Run the Basic Weather Agent

`Whether.py` runs a single-turn query against the agent:

```bash
# Pass city as a command-line argument
python Whether.py London

# Or let it prompt you
python Whether.py
```

### 4. Run the Conversational Agent (with History)

`Store_history/history.py` starts an interactive chat loop with full session memory:

```bash
python Store_history/history.py
```

You'll be asked for a **Session ID** (press `Enter` for `default`). Your conversation is saved to `chat_history_<session_id>.json` and automatically reloaded on the next run.

```
🌤️  Weather Assistant (powered by LangChain + Ollama)
────────────────────────────────────────────────────
Session ID (press Enter for 'default'): 
📁 History stored in: chat_history_default.json
Type 'quit' to exit.

You: What is the weather in Vadodara?
Assistant: Here is the current weather in Vadodara:
  • Temperature: 30°C (Warm)
  • Humidity: 65%
  • Rainfall Probability: Low (10%)
  • Wind Speed: 12 km/h
  • Wind Direction: North-East
```

---

## 🛠️ Tech Stack

| Component         | Library / Tool                             |
|-------------------|--------------------------------------------|
| Agent Framework   | [LangChain](https://www.langchain.com/)    |
| LLM Runtime       | [Ollama](https://ollama.com/) (local)      |
| LLM Model         | `qwen2.5:7b` / `qwen3.5:4b`               |
| Chat History      | `FileChatMessageHistory` (JSON)            |
| Prompt Management | `ChatPromptTemplate`, `MessagesPlaceholder`|

---

## 📦 Dependencies

```text
langchain
langchain-community
langchain-ollama
python-dotenv
```

Install all at once:

```bash
pip install -r requirements.txt
```

---

## 🔍 How It Works

The assistant follows a simple but powerful agentic pipeline:

```
 User Input (natural language)
        │
        ▼
  ChatPromptTemplate
  (System prompt + MessagesPlaceholder for history)
        │
        ▼
  Ollama LLM (qwen2.5:7b / qwen3.5:4b)
  Running 100% locally — no internet required
        │
        ▼
  LangChain LCEL Chain
  (prompt | llm | output_parser)
        │
        ▼
  FileChatMessageHistory
  Saves conversation to JSON per session
        │
        ▼
  Response returned to User
```

1. **User sends a message** — e.g., *"What's the weather in Mumbai?"*
2. **History is loaded** — prior messages for this session are injected into the prompt context.
3. **LLM generates a response** — Ollama runs the local model to produce a structured weather summary.
4. **History is persisted** — both the user message and AI response are appended to the session's JSON file.
5. **Response is displayed** — the assistant's answer is printed to the terminal.

---

## 🤝 Contributing

Contributions, feature requests, and bug reports are welcome! Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
