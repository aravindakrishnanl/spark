import sqlite3, cv2
from pyzbar.pyzbar import decode

def start_camera():
    cap = cv2.VideoCapture(0)
    print("Camera scanning started...")

    while True:
        success, frame = cap.read()
        if not success:
            continue

        for qr in decode(frame):
            data = eval(qr.data.decode("utf-8"))
            dispatch_id = data.get("dispatch_id")

            if dispatch_id:
                conn = sqlite3.connect("wallmart.db")
                cursor = conn.cursor()
                cursor.execute("UPDATE dispatches SET status='DELIVERED' WHERE dispatch_id=?", (dispatch_id,))
                conn.commit()
                conn.close()
                print(f"Updated: {dispatch_id} -> DELIVERED")

        cv2.imshow("QR Scanner", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start_camera()
