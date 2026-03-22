from fastapi import FastAPI, Query, Response
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

# ------------------ DATA ------------------

menu = [
    {"id": 1, "name": "Pizza", "price": 200, "category": "Food", "is_available": True},
    {"id": 2, "name": "Burger", "price": 150, "category": "Food", "is_available": True},
    {"id": 3, "name": "Pasta", "price": 180, "category": "Food", "is_available": False},
    {"id": 4, "name": "Coke", "price": 50, "category": "Drink", "is_available": True},
    {"id": 5, "name": "Ice Cream", "price": 100, "category": "Dessert", "is_available": True},
    {"id": 6, "name": "Sandwich", "price": 120, "category": "Food", "is_available": True}
]

orders = []
order_counter = 1

cart = []

# ------------------ HELPERS ------------------

def find_menu_item(item_id):
    for item in menu:
        if item["id"] == item_id:
            return item
    return None

def calculate_bill(price, quantity, order_type="delivery"):
    total = price * quantity
    if order_type == "delivery":
        total += 30
    return total

# ------------------ MODELS ------------------

class OrderRequest(BaseModel):
    customer_name: str = Field(min_length=2)
    item_id: int = Field(gt=0)
    quantity: int = Field(gt=0, le=20)
    delivery_address: str = Field(min_length=5)
    order_type: str = "delivery"

class NewMenuItem(BaseModel):
    name: str
    price: int
    category: str
    is_available: bool = True

class CheckoutRequest(BaseModel):
    customer_name: str
    delivery_address: str

# ------------------ DAY 1 ------------------

@app.get("/")
def home():
    return {"message": "Welcome to Food Delivery App"}

@app.get("/menu")
def get_menu():
    return {"total": len(menu), "data": menu}

@app.get("/menu/summary")
def menu_summary():
    available = [i for i in menu if i["is_available"]]
    return {
        "total": len(menu),
        "available": len(available)
    }

@app.get("/menu/{item_id}")
def get_item(item_id: int):
    item = find_menu_item(item_id)
    if not item:
        return {"error": "Item not found"}
    return item

# ------------------ DAY 2 ------------------

@app.post("/orders")
def create_order(order: OrderRequest):
    global order_counter

    item = find_menu_item(order.item_id)
    if not item:
        return {"error": "Item not found"}

    if not item["is_available"]:
        return {"error": "Item not available"}

    total = calculate_bill(item["price"], order.quantity, order.order_type)

    new_order = {
        "order_id": order_counter,
        "customer": order.customer_name,
        "total": total
    }

    orders.append(new_order)
    order_counter += 1

    return new_order

@app.get("/orders")
def get_orders():
    return {"total_orders": len(orders), "data": orders}

# ------------------ DAY 3 FILTER ------------------

@app.get("/menu/filter")
def filter_menu(category: Optional[str] = None, max_price: Optional[int] = None):
    result = menu

    if category is not None:
        result = [i for i in result if i["category"] == category]

    if max_price is not None:
        result = [i for i in result if i["price"] <= max_price]

    return {"count": len(result), "data": result}

# ------------------ DAY 4 CRUD ------------------

@app.post("/menu")
def add_item(item: NewMenuItem, response: Response):
    new_id = len(menu) + 1
    new_item = item.dict()
    new_item["id"] = new_id
    menu.append(new_item)
    response.status_code = 201
    return new_item

@app.put("/menu/{item_id}")
def update_item(item_id: int, price: Optional[int] = None):
    item = find_menu_item(item_id)
    if not item:
        return {"error": "Not found"}

    if price is not None:
        item["price"] = price

    return item

@app.delete("/menu/{item_id}")
def delete_item(item_id: int):
    item = find_menu_item(item_id)
    if not item:
        return {"error": "Not found"}

    menu.remove(item)
    return {"message": "Deleted"}

# ------------------ DAY 5 CART ------------------

@app.post("/cart/add")
def add_cart(item_id: int, quantity: int = 1):
    item = find_menu_item(item_id)
    if not item:
        return {"error": "Item not found"}

    cart.append({"item_id": item_id, "quantity": quantity})
    return {"message": "Added to cart"}

@app.get("/cart")
def view_cart():
    return {"cart": cart}

@app.post("/cart/checkout")
def checkout(data: CheckoutRequest):
    global order_counter

    if not cart:
        return {"error": "Cart empty"}

    result = []
    for c in cart:
        item = find_menu_item(c["item_id"])
        total = calculate_bill(item["price"], c["quantity"])

        order = {
            "order_id": order_counter,
            "customer": data.customer_name,
            "total": total
        }
        orders.append(order)
        result.append(order)
        order_counter += 1

    cart.clear()
    return {"orders": result}

# ------------------ DAY 6 SEARCH ------------------

@app.get("/menu/search")
def search(keyword: str):
    result = [i for i in menu if keyword.lower() in i["name"].lower()]
    return {"results": result}

@app.get("/menu/page")
def pagination(page: int = 1, limit: int = 2):
    start = (page - 1) * limit
    return menu[start:start + limit]
