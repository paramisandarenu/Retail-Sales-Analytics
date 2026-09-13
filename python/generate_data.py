import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from pathlib import Path


# ============================================
# RETAIL SALES ANALYTICS
# Generate realistic retail sales data
# ============================================

# Make the results reproducible
random.seed(42)
np.random.seed(42)


# --------------------------------------------
# 1. Project folders
# --------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(exist_ok=True)


# --------------------------------------------
# 2. Customer data
# --------------------------------------------

first_names = [
    "Amal", "Nimal", "Kasun", "Dinesh", "Tharindu",
    "Chamod", "Isuru", "Ravindu", "Sahan", "Kavindu",
    "Sanduni", "Dilini", "Sachini", "Tharushi", "Nethmi",
    "Ayesha", "Hiruni", "Piumi", "Hasini", "Dinithi"
]

last_names = [
    "Perera", "Fernando", "Silva", "Bandara", "Wijesinghe",
    "Jayasinghe", "Gunawardena", "Rathnayake", "Samarasinghe",
    "Karunaratne"
]

cities = [
    "Colombo",
    "Kandy",
    "Galle",
    "Jaffna",
    "Negombo",
    "Kurunegala",
    "Matara",
    "Anuradhapura",
    "Ratnapura",
    "Batticaloa"
]


# --------------------------------------------
# 3. Product data
# --------------------------------------------

products = [
    ("P001", "Laptop", "Electronics", 180000),
    ("P002", "Smartphone", "Electronics", 95000),
    ("P003", "Tablet", "Electronics", 65000),
    ("P004", "Wireless Headphones", "Electronics", 18000),
    ("P005", "Smart Watch", "Electronics", 25000),

    ("P006", "Office Chair", "Furniture", 35000),
    ("P007", "Office Desk", "Furniture", 55000),
    ("P008", "Bookshelf", "Furniture", 28000),
    ("P009", "Dining Table", "Furniture", 85000),
    ("P010", "Computer Table", "Furniture", 42000),

    ("P011", "T-Shirt", "Clothing", 4500),
    ("P012", "Jeans", "Clothing", 7500),
    ("P013", "Jacket", "Clothing", 12000),
    ("P014", "Sneakers", "Clothing", 15000),
    ("P015", "Backpack", "Clothing", 6500),

    ("P016", "Coffee Maker", "Home Appliances", 22000),
    ("P017", "Electric Kettle", "Home Appliances", 8500),
    ("P018", "Blender", "Home Appliances", 14000),
    ("P019", "Rice Cooker", "Home Appliances", 18000),
    ("P020", "Microwave Oven", "Home Appliances", 48000),

    ("P021", "Notebook", "Stationery", 800),
    ("P022", "Pen Set", "Stationery", 1200),
    ("P023", "Calculator", "Stationery", 2500),
    ("P024", "File Folder", "Stationery", 650),
    ("P025", "Desk Organizer", "Stationery", 1800)
]


# --------------------------------------------
# 4. Generate sales transactions
# --------------------------------------------

number_of_sales = 3000

records = []

start_date = datetime(2025, 1, 1)
end_date = datetime(2026, 8, 28)

date_range = (end_date - start_date).days


for i in range(1, number_of_sales + 1):

    # Order information
    order_id = f"ORD{i:05d}"

    random_days = random.randint(0, date_range)

    order_date = start_date + timedelta(days=random_days)

    # Customer
    customer_id = f"C{random.randint(1, 500):04d}"

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    customer_name = f"{first_name} {last_name}"

    city = random.choice(cities)

    # Product
    product = random.choice(products)

    product_id = product[0]
    product_name = product[1]
    category = product[2]
    unit_price = product[3]

    # Quantity
    quantity = random.choices(
        [1, 2, 3, 4, 5],
        weights=[50, 25, 15, 7, 3]
    )[0]

    # Discount
    discount_percentage = random.choice(
        [0, 0, 0, 5, 5, 10, 10, 15]
    )

    # Calculate values
    gross_amount = quantity * unit_price

    discount_amount = (
        gross_amount * discount_percentage / 100
    )

    total_sales = gross_amount - discount_amount

    # Payment
    payment_method = random.choice([
        "Cash",
        "Credit Card",
        "Debit Card",
        "Online Payment"
    ])

    # Add record
    records.append({
        "OrderID": order_id,
        "OrderDate": order_date.strftime("%Y-%m-%d"),
        "CustomerID": customer_id,
        "CustomerName": customer_name,
        "City": city,
        "ProductID": product_id,
        "ProductName": product_name,
        "Category": category,
        "Quantity": quantity,
        "UnitPrice": unit_price,
        "DiscountPercentage": discount_percentage,
        "DiscountAmount": round(discount_amount, 2),
        "PaymentMethod": payment_method,
        "TotalSales": round(total_sales, 2)
    })


# --------------------------------------------
# 5. Create DataFrame
# --------------------------------------------

df = pd.DataFrame(records)


# --------------------------------------------
# 6. Sort data by order date
# --------------------------------------------

df["OrderDate"] = pd.to_datetime(df["OrderDate"])

df = df.sort_values("OrderDate")

df["OrderDate"] = df["OrderDate"].dt.strftime("%Y-%m-%d")


# --------------------------------------------
# 7. Save CSV file
# --------------------------------------------

output_file = DATA_DIR / "sales_data.csv"

df.to_csv(output_file, index=False)


# --------------------------------------------
# 8. Display information
# --------------------------------------------

print("=" * 50)
print("RETAIL SALES DATA GENERATED SUCCESSFULLY")
print("=" * 50)

print(f"Number of transactions : {len(df)}")
print(f"Number of columns      : {len(df.columns)}")
print(f"Total sales            : LKR {df['TotalSales'].sum():,.2f}")
print(f"Average sale           : LKR {df['TotalSales'].mean():,.2f}")
print(f"CSV file               : {output_file}")

print("=" * 50)

print("\nFirst 5 records:")
print(df.head())