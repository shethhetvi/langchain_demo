import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, send_from_directory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()
app = Flask(__name__, static_folder=".")
llm = ChatGoogleGenerativeAI(model="gemini-flash-latest", google_api_key=os.getenv("GOOGLE_API_KEY"))

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/confirm-ingredients", methods=["POST"])
def confirm_ingredients():
    """Ask Gemini to parse and list the ingredients clearly."""
    data = request.json
    raw = data.get("ingredients", "")
    system = SystemMessage("You are a friendly kitchen assistant. The user has described their leftover ingredients. Extract and list each ingredient clearly as a comma-separated list. Keep it short. Example: 'cooked rice, 2 eggs, fresh spinach, half onion'. Just list them, nothing else.")
    response = llm.invoke([system, HumanMessage(f"My leftovers: {raw}")])
    return jsonify({"parsed": response.text.strip()})

@app.route("/generate", methods=["POST"])
def generate():
    """Generate 3-4 recipes based on ingredients + dietary preferences."""
    data = request.json
    ingredients = data.get("ingredients", "")
    diet = data.get("diet", "any")
    no_onion_garlic = data.get("no_onion_garlic", False)
    allergies = data.get("allergies", "")
    count = data.get("count", 3)

    constraints = []
    if diet == "veg": constraints.append("strictly vegetarian (no meat, no eggs, no seafood)")
    elif diet == "egg-veg": constraints.append("vegetarian but eggs are allowed")
    elif diet == "non-veg": constraints.append("non-vegetarian (meat and seafood allowed)")
    if no_onion_garlic: constraints.append("NO onion and NO garlic (Jain-friendly)")
    if allergies: constraints.append(f"avoid these allergens: {allergies}")

    constraint_str = ". ".join(constraints) if constraints else "no dietary restrictions"

    system = SystemMessage(
        f"You are an expert chef who specialises in reducing food waste. "
        f"Create exactly {count} creative, delicious recipes using primarily the user's leftover ingredients. "
        f"Dietary rules: {constraint_str}. "
        f"For EACH recipe use this exact format:\n"
        f"## [Recipe Name]\n"
        f"⏱ Time: [X mins] | 👤 Serves: [X] | 🌶 Difficulty: [Easy/Medium/Hard]\n"
        f"**Ingredients:**\n- item\n- item\n"
        f"**Steps:**\n1. step\n2. step\n"
        f"💡 Tip: [one useful tip]\n"
        f"---\n"
        f"Separate recipes with ---. Be warm and encouraging."
    )
    response = llm.invoke([system, HumanMessage(f"I have these leftovers: {ingredients}. Please suggest {count} recipes.")])
    return jsonify({"recipes": response.text})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
