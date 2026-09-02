import os
import json
import time
from pathlib import Path
from mem0 import MemoryClient

# 1. Initialize Mem0 client
api_key = os.getenv("MEM0_API_KEY", "m0-5CHIxLOLW2h3LoorqEv1sIAU8WUTJkjUlpdugKcW")
client = MemoryClient(api_key=api_key)

# 2. Locate and load chat history from basic_chat_history.json
history_file = Path(__file__).resolve().parent.parent / "basic_chat_history.json"
if not history_file.exists():
    history_file = Path("basic_chat_history.json")

with open(history_file, "r", encoding="utf-8") as f:
    chat_data = json.load(f)

# 3. Transform chat messages into Mem0 format
messages = []
for entry in chat_data:
    sender = entry.get("sender", "").strip().lower()
    role = "user" if sender in ["you", "user", "human"] else "assistant"
    messages.append({
        "role": role,
        "content": entry.get("message", "")
    })

USER_ID = "user_weather_chat"

print(f"Loaded {len(messages)} messages from {history_file.name}")
print("Adding chat history to Mem0 to extract context...")

# 4. Add conversation to Mem0
add_response = client.add(messages, user_id=USER_ID)
print(f"Memory extraction started (Event ID: {add_response.get('event_id', 'N/A')})...")

# Wait for Mem0 cloud to finish extracting semantic memories
print("Waiting for Mem0 to process memories...", end="", flush=True)
all_memories = {"results": []}
for _ in range(15):
    time.sleep(2)
    print(".", end="", flush=True)
    all_memories = client.get_all(filters={"user_id": USER_ID})
    if all_memories.get("results"):
        break
print(" Done!\n")
print("--- Extracted Context / Memories ---")
for idx, mem in enumerate(all_memories.get("results", []), 1):
    category = mem.get("categories", ["general"])[0] if mem.get("categories") else "general"
    print(f"{idx}. [{category.upper()}] {mem.get('memory')}")

# 6. Search context for a specific topic (e.g. location or intent)
print("\n--- Search Context for 'weather and location' ---")
search_results = client.search("What is the user's inquiry and location?", filters={"user_id": USER_ID})
for idx, res in enumerate(search_results.get("results", []), 1):
    print(f"{idx}. {res.get('memory')} (score: {res.get('score', 0):.4f})")