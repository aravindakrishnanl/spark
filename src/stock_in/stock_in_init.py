from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
import sqlite3

app = FastAPI()
DB_PATH = "wallmart.db"

class OrderPayload(BaseModel):
    order_id: str
    products: Dict[str, int]
    manufacturer: str
    warehouse_location: str
    timestamp: str

@app.post("/receive_order")
def receive_order(order: OrderPayload):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for product_id, qty in order.products.items():
        cursor.execute("UPDATE stock SET quantity = quantity + ? WHERE product_id = ?", (qty, product_id))
    
    cursor.execute("UPDATE orders SET status = 'Received' WHERE id = ?", (order.order_id,))
    conn.commit()
    conn.close()

    return {
        "status": "✅ Stock Updated",
        "order_id": order.order_id,
        "received_items": order.products
    }
