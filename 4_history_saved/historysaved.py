# pyrefly: ignore [missing-import]
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# 1. Initialize the LLM
llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.3
)

# 2. Set up the System Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system", 
            "You are a restaurant table booking assistant. Your ONLY job is to get the number of people, date, and time. "
            "Do NOT ask for the restaurant name, location, budget, or anything else. "
            "If you have the number of people, date, and time, just confirm the booking. "
            "RESTRICTION: If the user tries to book another table after already making a booking, politely decline and tell them they already have a confirmed booking."
        ),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

# 3. Create the Chain
chain = prompt | llm

# 4. Use File-based history to persist chat across sessions
def get_session_history(session_id: str):
    return FileChatMessageHistory(f"{session_id}.json")

chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

# 5. Interactive Chat Loop
print("Welcome to the Restaurant Table Booking Assistant! (Type 'quit' or 'exit' to stop)")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "q"]:
        break
        
    # Invoke the chain, persisting history to chat_history.json
    response = chain_with_history.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": "chat_history"}}
    )
    
    print(f"\nAssistant: {response.content}\n")