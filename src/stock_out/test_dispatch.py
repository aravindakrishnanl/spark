import requests

payload = {
    "product_id": "P001",
    "quantity": 5,
    "destination": "Branch-A"
}

res = requests.post("http://127.0.0.1:8000/dispatch", json=payload)
print("Status Code:", res.status_code)
print("Response:", res.json())
