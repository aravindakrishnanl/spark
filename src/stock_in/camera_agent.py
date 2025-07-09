import cv2
from pyzbar.pyzbar import decode
import json
import requests
import time

API_URL = "http://127.0.0.1:8000/receive_order"

def camera_watchdog():
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            continue

        for code in decode(frame):
            try:
                qr_data = code.data.decode('utf-8')
                payload = json.loads(qr_data)
                print(f"📦 Order Detected: {payload['order_id']}")

                response = requests.post(API_URL, json=payload)
                print("✅ Updated:", response.json())
                time.sleep(5)
            except Exception as e:
                print("❌ QR decode error:", e)

        cv2.imshow("QR Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    camera_watchdog()
