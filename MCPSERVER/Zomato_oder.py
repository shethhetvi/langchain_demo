from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Vadodara Food Order")

restaurants={
"Pizza Hut Akota":{"area":"Akota","cuisine":"Pizza","menu":{"Margherita Pizza":199,"Farmhouse Pizza":299,"Garlic Bread":129}},
"La Pinoz Alkapuri":{"area":"Alkapuri","cuisine":"Pizza","menu":{"Farmhouse Pizza":299,"Cheese Burst Pizza":349,"Garlic Bread":149}},
"Jassi De Parathe":{"area":"Alkapuri","cuisine":"Punjabi","menu":{"Aloo Paratha":120,"Paneer Paratha":160,"Lassi":90}},
"Burger King Alkapuri":{"area":"Alkapuri","cuisine":"Burger","menu":{"Veg Whopper":179,"Cheese Burger":149,"French Fries":99}},
"Pizza On The Rock":{"area":"Diwalipura","cuisine":"Pizza","menu":{"Farmhouse Pizza":299,"Paneer Pizza":319,"Garlic Bread":149}}
}

cart=[]

@mcp.tool()
def search_restaurants(area:str="",cuisine:str="")->str:
    """Search restaurants in Vadodara."""
    result=[]
    for name,data in restaurants.items():
        if area and area.lower() not in data["area"].lower():
            continue
        if cuisine and cuisine.lower() not in data["cuisine"].lower():
            continue
        result.append(f"{name} | {data['area']} | {data['cuisine']}")
    return "\n".join(result) if result else "No restaurants found."

@mcp.tool()
def get_menu(restaurant:str)->str:
    """Get restaurant menu."""
    if restaurant not in restaurants:
        return "Restaurant not found."
    return "\n".join(f"{item} - ₹{price}" for item,price in restaurants[restaurant]["menu"].items())

@mcp.tool()
def add_to_cart(restaurant:str,item:str,quantity:int=1)->str:
    """Add food item to cart."""
    if restaurant not in restaurants:
        return "Restaurant not found."
    if item not in restaurants[restaurant]["menu"]:
        return "Food item not found."
    if quantity<=0:
        return "Invalid quantity."
    price=restaurants[restaurant]["menu"][item]
    cart.append({"restaurant":restaurant,"item":item,"quantity":quantity,"price":price})
    return f"Added {quantity} x {item} from {restaurant} = ₹{price*quantity}"

@mcp.tool()
def view_cart()->str:
    """View current cart."""
    if not cart:
        return "Cart is empty."
    total=0
    result=[]
    for x in cart:
        amount=x["price"]*x["quantity"]
        total+=amount
        result.append(f"{x['item']} x {x['quantity']} = ₹{amount}")
    result.append(f"Total = ₹{total}")
    return "\n".join(result)

@mcp.tool()
def place_order(address:str)->str:
    """Place food order."""
    if not cart:
        return "Cart is empty."
    total=sum(x["price"]*x["quantity"] for x in cart)
    order_id="VAD"+str(len(cart)+1000)
    cart.clear()
    return f"Order placed!\nOrder ID: {order_id}\nAddress: {address}\nTotal: ₹{total}\nDelivery: 30-45 minutes"

if __name__=="__main__":
    mcp.run()