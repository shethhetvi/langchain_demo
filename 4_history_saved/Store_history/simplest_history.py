import json
from langchain_ollama import ChatOllama
# 1. Initialize Ollama
llm = ChatOllama(model="qwen2.5:7b")
HISTORY_FILE = "basic_chat_history.json"
def main():
    print("Welcome! (Type 'quit' to exit)")
    # We will just keep a simple list of dictionaries
    chat_log = []
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
        # 2. Record the User's message
        chat_log.append({"sender": "You", "message": user_input})
        # 3. Get AI response (just sending the raw string for absolute simplicity)
        response = llm.invoke(user_input)
        print(f"Bot: {response.content}")
        # 4. Record the Bot's message
        chat_log.append({"sender": "Bot", "message": response.content})
        # 5. Save the simple list to a JSON file
        with open(HISTORY_FILE, "w") as f:
            json.dump(chat_log, f, indent=4)
if __name__ == "__main__":
    main()
