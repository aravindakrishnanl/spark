import os
import sys
from math import ceil

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from db_retrieval import retrieval
from forecasting.item_forecasting import predict_sales

def should_reorder(predicted_demand, current_stock, reorder_threshold = 50):
    return (predicted_demand >= reorder_threshold) and (current_stock <= reorder_threshold)
    
store = 1
reorder_list = []
for i in range(1, 51):
    base = retrieval(f"select stock_level from stocks where id = {str(i)}", "stocks")[0][0]
    # current_stock = base.fetchall()
    demand = predict_sales(store, i)
    out = should_reorder(demand, base)
    reorder_list.append([i, out, ceil(demand)])
print(reorder_list)