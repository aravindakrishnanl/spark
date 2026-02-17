# qr_scanner.py

import cv2
from pyzbar.pyzbar import decode
import requests

def scan_qr():
    cap = cv2.VideoCapture(0)
    scanned = False

    print("📷 Scanning for QR... Press Q to quit.")
    
    while not scanned:
        success, frame = cap.read()
        if not success:
            continue

        for code in decode(frame):
            order_id = code.data.decode('utf-8')
            print(f"📦 Detected Order ID: {order_id}")

            # Send to backend
            res = requests.post("http://127.0.0.1:8000/receive_order", json={"order_id": order_id})
            print("📬 Backend Response:", res.json())
            scanned = True
            break

        cv2.imshow("Scan Vehicle QR", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr()
