import os
import sys
import sqlite3 

sys.path.append(os.path.abspath(os.path.join("..")))

#Products Databse init
#items -> id, name, category
products_cur =sqlite3.connect("A:/spark/database/products.db").cursor()

#Mail Databse init
#items -> id, mail
mail_cur = sqlite3.connect("A:/spark/database/mail.db").cursor()

#Stock Level Databse init
#stocks -> id, name, category
stock_cur = sqlite3.connect("A:/spark/database/stock_level.db").cursor()

def retrieval(query, db):
    if db == "products":
        products_cur.execute(query)
        return products_cur.fetchall()
    
    elif db == "mail":
        mail_cur.execute(query)
        return mail_cur.fetchall()

    elif db == "stocks":
        stock_cur.execute(query)
        return stock_cur.fetchall()

    else:
        return None

# Sample retrieval
# i = 2
# print(product_retrieval(f"select stock_level from stocks where id = {str(i)}", "stocks"))