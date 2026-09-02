# LangChain & Agentic AI Practicals (`langchain_demo`)

A collection of hands-on practical implementations showcasing LLM agents, tool integrations, conversational memory, and semantic context extraction using LangChain, Ollama, Google Generative AI, and Mem0.

## 📁 Repository Structure

- **`1_simple_agent/`**: Basic LangChain agent setup and tool invocation.
- **`2_whether_ai/`**: Weather assistant agent querying current weather data.
- **`3_recipe/`**: Recipe assistant and web interface powered by Google Generative AI (`gemini-flash`).
- **`4_history_saved/`**: Multi-turn conversation history persistence using `FileChatMessageHistory` and `RunnableWithMessageHistory`.
- **`5_context_from_history/`**: Semantic memory and context extraction from conversation history using `mem0ai`.
- **`Agentic-ai-whether/`**: Agentic AI workflow for weather queries.

## 🚀 Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd langchain_demo
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install mem0ai
   ```

4. **Environment Configuration:**
   Set required API keys as environment variables:
   ```bash
   export GOOGLE_API_KEY="your-google-api-key"
   export MEM0_API_KEY="your-mem0-api-key"
   ```

## 🛠️ Usage Example (Semantic Memory Context)

Run the Mem0 context extractor on `basic_chat_history.json`:
```bash
python 5_context_from_history/main.py
```
