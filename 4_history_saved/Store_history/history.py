import time
from langchain_ollama import ChatOllama
# pyrefly: ignore [missing-import]
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

# ── 1. LLM ────────────────────────────────────────────────────────────────────
llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0,
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful AI assistant. "
        "Provide helpful and concise answers.",
    ),
    MessagesPlaceholder(variable_name="history"),   # injected chat history
    ("human", "{input}"),
])

# ── 3. Chain ───────────────────────────────────────────────────────────────────
chain = prompt | llm

# ── 4. History store (JSON file per session) ───────────────────────────────────
def get_session_history(session_id: str) -> FileChatMessageHistory:
    """Return a FileChatMessageHistory backed by chat_history_<session_id>.json"""
    return FileChatMessageHistory(f"chat_history_{session_id}.json")

# ── 5. Wrap chain with persistent message history ─────────────────────────────
agent = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

# ── 6. Main chat loop ─────────────────────────────────────────────────────────
def main():
    print("\n🤖  AI Assistant (powered by LangChain + Ollama)")
    print("─" * 52)
    session_id = input("Session ID (press Enter for 'default'): ").strip() or "default"
    print(f"📁 History stored in: chat_history_{session_id}.json")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye! 👋")
            break

        start = time.time()
        response = agent.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": session_id}},
        )
        elapsed = time.time() - start

        print(f"\nAssistant: {response.content}")
        print(f"⏱  {elapsed:.2f}s\n")

if __name__ == "__main__":
    main()