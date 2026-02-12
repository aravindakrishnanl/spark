from fastapi import FastAPI
from pydantic import BaseModel
from .dispatch_agent import dispatch_order

app = FastAPI()

class DispatchRequest(BaseModel):
    product_id: str
    quantity: int
    destination: str

@app.post("/dispatch")
def dispatch(req: DispatchRequest):
    return dispatch_order(req.product_id, req.quantity, req.destination)