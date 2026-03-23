📄 🍕 QuickBite — Food Delivery API
FastAPI  Python  Pydantic  Swagger
A complete FastAPI backend for a Food Delivery System — built as the Final Project for the FastAPI Internship Training (Days 1–6).

This project covers all FastAPI concepts from basic APIs to advanced features like search, sorting, pagination, CRUD operations, and multi-step workflows.
📁 Project Structure
fastapi-food-delivery-app/
├── main.py
├── requirements.txt
├── README.md
└── screenshots/
    ├── Q1_home.png
    ├── Q2_menu.png
    ├── Q3_item.png
    ├── Q4_orders.png
    ├── Q5_summary.png
    ├── Q6_validation.png
    ├── Q7_helpers.png
    ├── Q8_create_order.png
    ├── Q9_delivery_charge.png
    ├── Q10_filter.png
    ├── Q11_add_item.png
    ├── Q12_update_item.png
    ├── Q13_delete_item.png
    ├── Q14_cart_add.png
    ├── Q15_checkout.png
    ├── Q16_search.png
    ├── Q17_sort.png
    ├── Q18_pagination.png
    ├── Q19_orders_search_sort.png
    └── Q20_browse.png
🚀 How to Run Project
Step 1
pip install fastapi uvicorn

Step 2
python -m uvicorn main:app --reload
Step 3
Open:

http://127.0.0.1:8000/docs
📦 Dependencies
fastapi
uvicorn
pydantic
🎯 Project Overview
QuickBite is a backend system where users can:

View food menu

Place food orders

Add items to cart

Checkout orders

Search food items

Sort and paginate menu

Manage menu items (CRUD)

📌 All 20 API Endpoints
🟢 Day 1 — GET APIs
| Q  | Method | Route         | Description        |
| -- | ------ | ------------- | ------------------ |
| Q1 | GET    | /             | Welcome message    |
| Q2 | GET    | /menu         | Get all menu items |
| Q3 | GET    | /menu/{id}    | Get item by ID     |
| Q4 | GET    | /orders       | Get all orders     |
| Q5 | GET    | /menu/summary | Menu statistics    |

🟡 Day 2 — POST + Validation
| Q  | Method | Route   | Description                     |
| -- | ------ | ------- | ------------------------------- |
| Q6 | POST   | /orders | Validate request using Pydantic |
| Q8 | POST   | /orders | Create order                    |
| Q9 | POST   | /orders | Add delivery charge             |

🟠 Day 3 — Helpers + Filter
| Q   | Method | Route        | Description                        |
| --- | ------ | ------------ | ---------------------------------- |
| Q7  | —      | helpers      | find_menu_item(), calculate_bill() |
| Q10 | GET    | /menu/filter | Filter by category, price          |

🔵 Day 4 — CRUD
| Q   | Method | Route      | Description |
| --- | ------ | ---------- | ----------- |
| Q11 | POST   | /menu      | Add item    |
| Q12 | PUT    | /menu/{id} | Update item |
| Q13 | DELETE | /menu/{id} | Delete item |

🟣 Day 5 — Cart Workflow
| Q   | Method | Route          | Description      |
| --- | ------ | -------------- | ---------------- |
| Q14 | POST   | /cart/add      | Add item to cart |
| Q14 | GET    | /cart          | View cart        |
| Q15 | DELETE | /cart/{id}     | Remove item      |
| Q15 | POST   | /cart/checkout | Checkout order   |


🔴 Day 6 — Advanced APIs
| Q   | Method | Route          | Description   |
| --- | ------ | -------------- | ------------- |
| Q16 | GET    | /menu/search   | Search items  |
| Q17 | GET    | /menu/sort     | Sort items    |
| Q18 | GET    | /menu/page     | Pagination    |
| Q19 | GET    | /orders/search | Search orders |
| Q19 | GET    | /orders/sort   | Sort orders   |
| Q20 | GET    | /menu/browse   | Combined API  |

🧠 Concepts Covered

| Day   | Concept         | Description                |
| ----- | --------------- | -------------------------- |
| Day 1 | GET APIs        | Basic routes and responses |
| Day 2 | POST + Pydantic | Data validation            |
| Day 3 | Helpers         | Business logic functions   |
| Day 4 | CRUD            | Create, Update, Delete     |
| Day 5 | Workflow        | Cart → Checkout            |
| Day 6 | Advanced        | Search, Sort, Pagination   |

🍔 Sample Menu Data
| ID | Name      | Category | Price |
| -- | --------- | -------- | ----- |
| 1  | Pizza     | Food     | 200   |
| 2  | Burger    | Food     | 150   |
| 3  | Pasta     | Food     | 180   |
| 4  | Coke      | Drink    | 50    |
| 5  | Ice Cream | Dessert  | 100   |

🔁 Workflow (Cart System)
POST /cart/add → Add item
GET /cart → View cart
DELETE /cart/{id} → Remove item
POST /cart/checkout → Place order

🔍 Combined Browse API
GET /menu/browse
Supports:

keyword search
sorting
pagination

📸 API Testing

All APIs tested using Swagger UI:
http://127.0.0.1:8000/docs

🏁 Conclusion

This project helped me understand how to build real-world backend systems using FastAPI,
including API design, validation, workflows, and advanced data handling.
