import sqlite3, qrcode, uuid, datetime

def dispatch_order(product_id, quantity, destination):
    conn = sqlite3.connect("wallmart.db")
    cursor = conn.cursor()

    cursor.execute("SELECT quantity FROM inventory WHERE product_id=?", (product_id,))
    row = cursor.fetchone()
    if not row or row[0] < quantity:
        return {"error": "Insufficient stock"}

    # Deduct stock
    cursor.execute("UPDATE inventory SET quantity = quantity - ? WHERE product_id=?", (quantity, product_id))

    # Create dispatch record
    dispatch_id = str(uuid.uuid4())
    timestamp = str(datetime.datetime.now())
    cursor.execute("INSERT INTO dispatches VALUES (?, ?, ?, ?, ?, ?)",
                   (dispatch_id, product_id, quantity, destination, "IN_TRANSIT", timestamp))

    conn.commit()
    conn.close()

    # Generate QR
    data = {
        "dispatch_id": dispatch_id,
        "product_id": product_id,
        "quantity": quantity,
        "destination": destination,
        "timestamp": timestamp
    }
    qr = qrcode.make(str(data))
    qr.save("order_qr.png")
    import os
    os.makedirs("vehicle_qr_stock_out/dispatch_qrs", exist_ok=True)
    qr_path = f"vehicle_qr_stock_out/dispatch_qrs/{dispatch_id}.png"
    qr.save(qr_path)


    return {"message": "Dispatch successful", "dispatch_id": dispatch_id}