import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from db_retrieval import product_retrieval
    
print(product_retrieval("select * from items", "products"))