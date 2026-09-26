import pandas as pd
import json
from pathlib import Path


# Project folder
BASE_DIR = Path(__file__).resolve().parent.parent


# Input and output files
DATA_FILE = BASE_DIR / "data" / "clean_sales_data.csv"
OUTPUT_FILE = BASE_DIR / "dashboard" / "dashboard_data.json"


# Load cleaned sales data
df = pd.read_csv(DATA_FILE)

# Convert OrderDate to datetime
df["OrderDate"] = pd.to_datetime(df["OrderDate"])


# --------------------------------------------------
# KPI DATA
# --------------------------------------------------

total_revenue = df["TotalSales"].sum()
total_orders = len(df)
average_order_value = df["TotalSales"].mean()
total_quantity = df["Quantity"].sum()


# --------------------------------------------------
# MONTHLY SALES
# --------------------------------------------------

monthly_sales = (
    df.groupby(df["OrderDate"].dt.to_period("M"))["TotalSales"]
    .sum()
)

monthly_sales = {
    str(month): float(value)
    for month, value in monthly_sales.items()
}


# --------------------------------------------------
# SALES BY CATEGORY
# --------------------------------------------------

category_sales = (
    df.groupby("Category")["TotalSales"]
    .sum()
    .sort_values(ascending=False)
)

category_sales = {
    str(category): float(value)
    for category, value in category_sales.items()
}


# --------------------------------------------------
# SALES BY CITY
# --------------------------------------------------

city_sales = (
    df.groupby("City")["TotalSales"]
    .sum()
    .sort_values(ascending=False)
)

city_sales = {
    str(city): float(value)
    for city, value in city_sales.items()
}


# --------------------------------------------------
# TOP 10 PRODUCTS
# --------------------------------------------------

top_products = (
    df.groupby("ProductName")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_products = {
    str(product): int(quantity)
    for product, quantity in top_products.items()
}


# --------------------------------------------------
# CREATE DASHBOARD DATA
# --------------------------------------------------

dashboard_data = {

    "kpis": {
        "totalRevenue": float(total_revenue),
        "totalOrders": int(total_orders),
        "averageOrderValue": float(average_order_value),
        "totalQuantity": int(total_quantity)
    },

    "monthlySales": monthly_sales,

    "categorySales": category_sales,

    "citySales": city_sales,

    "topProducts": top_products
}


# --------------------------------------------------
# SAVE JSON FILE
# --------------------------------------------------

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(dashboard_data, file, indent=4)


print("=" * 50)
print("DASHBOARD DATA CREATED SUCCESSFULLY")
print("=" * 50)

print(f"Output file: {OUTPUT_FILE}")

print("\nDashboard KPIs:")
print(f"Total Revenue: LKR {total_revenue:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Average Order Value: LKR {average_order_value:,.2f}")
print(f"Total Quantity: {total_quantity:,}")

print("=" * 50)