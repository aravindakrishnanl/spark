import os
import sys
import sqlite3 

sys.path.append(os.path.abspath(os.path.join("..")))

#Products Databse init
#items -> id, name, category
products_cur =sqlite3.connect("A:/spark/database/products.db").cursor()

#Mail Databse init
#stocks -> id, stock_level_price
mail_cur = sqlite3.connect("A:/spark/database/mail.db").cursor()

#Stock Level Databse init
# -> id, name, category
stock_cur = sqlite3.connect("A:/spark/database/stock_level.db").cursor()

def product_retrieval(query, db):
    if db == "products":
        products_cur.execute(query)
        return products_cur.fetchall()
    else:
        return None

print(product_retrieval("select * from items", "products"))