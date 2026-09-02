import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-flash-latest", google_api_key=os.getenv("GOOGLE_API_KEY"))
print("\nWelcome to Simple ChefBot!\n")
ingredients = input("What ingredients do you have? ").strip()
print(f"\nCooking up a recipe for you using {ingredients}...\n")
recipe_system = SystemMessage(
    "You are a helpful chef. The user will give you ingredients. "
    "Provide a simple, easy-to-follow recipe using mostly those ingredients. "
    "Do not use any emojis in your response."
)
response = llm.invoke([
    recipe_system, 
    HumanMessage(f"My ingredients are: {ingredients}. Please give me a recipe.")
])
print("\n" + "=" * 50)
print("YOUR RECIPE")
print("=" * 50)
print(response.text)
print("\nEnjoy your meal!\n")
