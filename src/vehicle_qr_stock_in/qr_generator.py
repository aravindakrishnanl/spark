import qrcode
import json
from datetime import datetime
from pathlib import Path

def generate_order_qr(order_id, products, manufacturer, warehouse):
    qr_data = {
        "order_id": order_id,
        "products": products,
        "manufacturer": manufacturer,
        "warehouse_location": warehouse,
        "timestamp": datetime.now().isoformat()
    }

    Path("vehicle_qr_stock_in/generated_qrs").mkdir(exist_ok=True)
    qr_img = qrcode.make(json.dumps(qr_data))
    file_path = f"vehicle_qr_stock_in/generated_qrs/{order_id}.png"
    qr_img.save(file_path)

    print(f"✅ QR Code saved at: {file_path}")
    return file_path

# Example usage
if __name__ == "__main__":
    generate_order_qr(
        order_id="ORD_1001",
        products={"P001": 180},
        manufacturer="ABC Ltd",
        warehouse="Warehouse-A"
    )
