import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================
# RETAIL SALES ANALYTICS
# Create Sales Charts
# ============================================

# Find project folders
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "clean_sales_data.csv"
CHART_DIR = BASE_DIR / "dashboard" / "charts"

# Create charts folder if it does not exist
CHART_DIR.mkdir(parents=True, exist_ok=True)

# Load cleaned sales data
df = pd.read_csv(DATA_FILE)

# Convert OrderDate into date format
df["OrderDate"] = pd.to_datetime(df["OrderDate"])


# ============================================
# CHART 1 - MONTHLY SALES TREND
# ============================================

monthly_sales = (
    df.groupby(df["OrderDate"].dt.to_period("M"))["TotalSales"]
    .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales (LKR)")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    CHART_DIR / "monthly_sales_trend.png",
    dpi=300
)

plt.close()


# ============================================
# CHART 2 - SALES BY CATEGORY
# ============================================

category_sales = (
    df.groupby("Category")["TotalSales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

plt.bar(
    category_sales.index,
    category_sales.values
)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales (LKR)")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    CHART_DIR / "sales_by_category.png",
    dpi=300
)

plt.close()


# ============================================
# CHART 3 - SALES BY CITY
# ============================================

city_sales = (
    df.groupby("City")["TotalSales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

plt.barh(
    city_sales.index,
    city_sales.values
)

plt.title("Sales by City")
plt.xlabel("Total Sales (LKR)")
plt.ylabel("City")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig(
    CHART_DIR / "sales_by_city.png",
    dpi=300
)

plt.close()


# ============================================
# CHART 4 - TOP 10 PRODUCTS BY QUANTITY
# ============================================

top_products = (
    df.groupby("ProductName")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))

plt.barh(
    top_products.index,
    top_products.values
)

plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Quantity Sold")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig(
    CHART_DIR / "top_10_products.png",
    dpi=300
)

plt.close()


# ============================================
# COMPLETION MESSAGE
# ============================================

print("=" * 50)
print("SALES CHARTS CREATED SUCCESSFULLY")
print("=" * 50)

print(f"Charts saved to: {CHART_DIR}")

print("\nCreated charts:")
print("1. Monthly Sales Trend")
print("2. Sales by Category")
print("3. Sales by City")
print("4. Top 10 Products by Quantity")

print("=" * 50)