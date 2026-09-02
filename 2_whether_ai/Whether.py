import sys
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get the current weather forecast for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="ollama:qwen2.5:7b",
    tools=[get_weather],
    system_prompt="You are a helpful assistant. Help the user get weather information so they can plan their day."
)

city_name = sys.argv[1] if len(sys.argv) > 1 else input("Enter city name: ")

result = agent.invoke(
    {"messages": [{"role": "user", "content": f"What is the weather like in {city_name}?"}]}
)
print(result["messages"][-1].content)