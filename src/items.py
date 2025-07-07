from dataclasses import dataclass

@dataclass
class Item:
    id: str
    name: str
    category: str
    quantity: int
    price: float

items = [
    Item("001", "Soap", "Personal Care", 120, 25.0),
    Item("002", "Shampoo", "Personal Care", 80, 120.0),
    Item("003", "Toothpaste", "Personal Care", 100, 40.0),
    Item("004", "Toothbrush", "Personal Care", 150, 20.0),
    Item("005", "Face Wash", "Personal Care", 60, 90.0),
    Item("006", "Hair Oil", "Personal Care", 70, 60.0),
    Item("007", "Comb", "Personal Care", 90, 15.0),
    Item("008", "Sanitary Napkins", "Hygiene", 50, 75.0),
    Item("009", "Hand Sanitizer", "Hygiene", 100, 30.0),
    Item("010", "Detergent Powder", "Cleaning", 200, 45.0),
    Item("011", "Detergent Bar", "Cleaning", 180, 10.0),
    Item("012", "Dishwash Liquid", "Cleaning", 90, 35.0),
    Item("013", "Bleach", "Cleaning", 40, 25.0),
    Item("014", "Phenyl", "Cleaning", 60, 50.0),
    Item("015", "Room Freshener", "Cleaning", 30, 80.0),
    Item("016", "Rice (5kg)", "Grocery", 70, 250.0),
    Item("017", "Wheat Flour (5kg)", "Grocery", 60, 180.0),
    Item("018", "Sugar (1kg)", "Grocery", 90, 42.0),
    Item("019", "Salt (1kg)", "Grocery", 100, 18.0),
    Item("020", "Turmeric Powder", "Spices", 40, 30.0),
    Item("021", "Red Chili Powder", "Spices", 35, 45.0),
    Item("022", "Coriander Powder", "Spices", 30, 40.0),
    Item("023", "Tea Powder", "Beverages", 50, 120.0),
    Item("024", "Coffee Powder", "Beverages", 45, 140.0),
    Item("025", "Milk Powder", "Dairy", 55, 200.0),
    Item("026", "Ghee", "Dairy", 40, 520.0),
    Item("027", "Biscuits", "Snacks", 130, 10.0),
    Item("028", "Chips", "Snacks", 100, 20.0),
    Item("029", "Noodles", "Snacks", 90, 25.0),
    Item("030", "Soft Drinks", "Beverages", 70, 35.0),
    Item("031", "Juice", "Beverages", 60, 30.0),
    Item("032", "Water Bottle (1L)", "Beverages", 150, 20.0),
    Item("033", "Cooking Oil (1L)", "Grocery", 80, 120.0),
    Item("034", "Mustard Oil (1L)", "Grocery", 50, 110.0),
    Item("035", "Matchbox", "Misc", 200, 5.0),
    Item("036", "Candle", "Misc", 120, 10.0),
    Item("037", "Notebook", "Stationery", 100, 30.0),
    Item("038", "Pen", "Stationery", 200, 10.0),
    Item("039", "Pencil", "Stationery", 150, 5.0),
    Item("040", "Eraser", "Stationery", 140, 3.0),
    Item("041", "Razor", "Personal Care", 90, 25.0),
    Item("042", "Shaving Cream", "Personal Care", 50, 65.0),
    Item("043", "Towel", "Home", 40, 85.0),
    Item("044", "Napkin", "Home", 70, 25.0),
    Item("045", "Toilet Paper", "Hygiene", 100, 15.0),
    Item("046", "Mosquito Coil", "Health", 60, 30.0),
    Item("047", "Insect Spray", "Health", 45, 90.0),
    Item("048", "Band-Aid", "Health", 80, 12.0),
    Item("049", "Cotton", "Health", 70, 20.0),
    Item("050", "Thermometer", "Health", 25, 150.0),
]
