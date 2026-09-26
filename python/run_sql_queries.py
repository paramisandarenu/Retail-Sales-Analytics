import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_FILE = BASE_DIR / "sql" / "retail_sales.db"


connection = sqlite3.connect(DATABASE_FILE)

cursor = connection.cursor()


# --------------------------------------------
# Total orders
# --------------------------------------------

cursor.execute("""
SELECT COUNT(*)
FROM sales
""")

total_orders = cursor.fetchone()[0]

print(f"Total Orders: {total_orders:,}")


# --------------------------------------------
# Total revenue
# --------------------------------------------

cursor.execute("""
SELECT SUM(TotalSales)
FROM sales
""")

total_revenue = cursor.fetchone()[0]

print(f"Total Revenue: LKR {total_revenue:,.2f}")


# --------------------------------------------
# Average order value
# --------------------------------------------

cursor.execute("""
SELECT AVG(TotalSales)
FROM sales
""")

average_order = cursor.fetchone()[0]

print(f"Average Order Value: LKR {average_order:,.2f}")


# --------------------------------------------
# Sales by category
# --------------------------------------------

print("\nSales by Category")
print("-" * 40)

cursor.execute("""
SELECT
    Category,
    SUM(TotalSales) AS Total_Sales
FROM sales
GROUP BY Category
ORDER BY Total_Sales DESC
""")

category_results = cursor.fetchall()

for category, sales in category_results:
    print(f"{category}: LKR {sales:,.2f}")


# --------------------------------------------
# Sales by city
# --------------------------------------------

print("\nSales by City")
print("-" * 40)

cursor.execute("""
SELECT
    City,
    SUM(TotalSales) AS Total_Sales
FROM sales
GROUP BY City
ORDER BY Total_Sales DESC
""")

city_results = cursor.fetchall()

for city, sales in city_results:
    print(f"{city}: LKR {sales:,.2f}")


# --------------------------------------------
# Top 10 products
# --------------------------------------------

print("\nTop 10 Products by Quantity Sold")
print("-" * 40)

cursor.execute("""
SELECT
    ProductName,
    SUM(Quantity) AS Total_Quantity
FROM sales
GROUP BY ProductName
ORDER BY Total_Quantity DESC
LIMIT 10
""")

product_results = cursor.fetchall()

for product, quantity in product_results:
    print(f"{product}: {quantity:,} units")


# --------------------------------------------
# Close database
# --------------------------------------------

connection.close()

print("\nSQL analysis completed successfully.")