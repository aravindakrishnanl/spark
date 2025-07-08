import sqlite3

conn = sqlite3.connect('products.db')
cur = conn.cursor()

cur.execute("""
CREATE TABLE items (
    id TEXT PRIMARY KEY,
    name TEXT,
    category TEXT
)
""")

items = [
    ("1", "Soap", "Personal Care"),
    ("2", "Shampoo", "Personal Care"),
    ("3", "Toothpaste", "Personal Care"),
    ("4", "Toothbrush", "Personal Care"),
    ("5", "Face Wash", "Personal Care"),
    ("6", "Hair Oil", "Personal Care"),
    ("7", "Comb", "Personal Care"),
    ("8", "Sanitary Napkins", "Hygiene"),
    ("9", "Hand Sanitizer", "Hygiene"),
    ("10", "Detergent Powder", "Cleaning"),
    ("11", "Detergent Bar", "Cleaning"),
    ("12", "Dishwash Liquid", "Cleaning"),
    ("13", "Bleach", "Cleaning"),
    ("14", "Phenyl", "Cleaning"),
    ("15", "Room Freshener", "Cleaning"),
    ("16", "Rice (5kg)", "Grocery"),
    ("17", "Wheat Flour (5kg)", "Grocery"),
    ("18", "Sugar (1kg)", "Grocery"),
    ("19", "Salt (1kg)", "Grocery"),
    ("20", "Turmeric Powder", "Spices"),
    ("21", "Red Chili Powder", "Spices"),
    ("22", "Coriander Powder", "Spices"),
    ("23", "Tea Powder", "Beverages"),
    ("24", "Coffee Powder", "Beverages"),
    ("25", "Milk Powder", "Dairy"),
    ("26", "Ghee", "Dairy"),
    ("27", "Biscuits", "Snacks"),
    ("28", "Chips", "Snacks"),
    ("29", "Noodles", "Snacks"),
    ("30", "Soft Drinks", "Beverages"),
    ("31", "Juice", "Beverages"),
    ("32", "Water Bottle (1L)", "Beverages"),
    ("33", "Cooking Oil (1L)", "Grocery"),
    ("34", "Mustard Oil (1L)", "Grocery"),
    ("35", "Matchbox", "Misc"),
    ("36", "Candle", "Misc"),
    ("37", "Notebook", "Stationery"),
    ("38", "Pen", "Stationery"),
    ("39", "Pencil", "Stationery"),
    ("40", "Eraser", "Stationery"),
    ("41", "Razor", "Personal Care"),
    ("42", "Shaving Cream", "Personal Care"),
    ("43", "Towel", "Home"),
    ("44", "Napkin", "Home"),
    ("45", "Toilet Paper", "Hygiene"),
    ("46", "Mosquito Coil", "Health"),
    ("47", "Insect Spray", "Health"),
    ("48", "Band-Aid", "Health"),
    ("49", "Cotton", "Health"),
    ("50", "Thermometer", "Health"),
]

cur.executemany("""
INSERT OR REPLACE INTO items (id, name, category)
VALUES (?, ?, ?)
""", items)

conn.commit()
conn.close()
