import pandas as pd
from pathlib import Path


# ============================================
# RETAIL SALES ANALYTICS
# Data Cleaning and Validation
# ============================================


# --------------------------------------------
# 1. Find project folders
# --------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


# --------------------------------------------
# 2. Define input and output files
# --------------------------------------------

input_file = DATA_DIR / "sales_data.csv"
output_file = DATA_DIR / "clean_sales_data.csv"


# --------------------------------------------
# 3. Load the raw sales data
# --------------------------------------------

print("=" * 60)
print("LOADING SALES DATA")
print("=" * 60)

df = pd.read_csv(input_file)

print(f"Rows loaded    : {len(df)}")
print(f"Columns loaded : {len(df.columns)}")


# --------------------------------------------
# 4. Check missing values
# --------------------------------------------

print("\n" + "=" * 60)
print("CHECKING MISSING VALUES")
print("=" * 60)

missing_values = df.isnull().sum()

print(missing_values)


# --------------------------------------------
# 5. Check duplicate records
# --------------------------------------------

print("\n" + "=" * 60)
print("CHECKING DUPLICATE RECORDS")
print("=" * 60)

duplicate_count = df.duplicated().sum()

print(f"Duplicate rows found: {duplicate_count}")


# Remove duplicate rows if any exist
df = df.drop_duplicates()


# --------------------------------------------
# 6. Convert OrderDate to date format
# --------------------------------------------

df["OrderDate"] = pd.to_datetime(
    df["OrderDate"],
    errors="coerce"
)


# --------------------------------------------
# 7. Check invalid dates
# --------------------------------------------

invalid_dates = df["OrderDate"].isnull().sum()

print("\n" + "=" * 60)
print("CHECKING INVALID DATES")
print("=" * 60)

print(f"Invalid dates found: {invalid_dates}")


# Remove rows with invalid dates
df = df.dropna(subset=["OrderDate"])


# --------------------------------------------
# 8. Check numeric columns
# --------------------------------------------

numeric_columns = [
    "Quantity",
    "UnitPrice",
    "DiscountPercentage",
    "DiscountAmount",
    "TotalSales"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# --------------------------------------------
# 9. Check invalid quantities
# --------------------------------------------

invalid_quantity = (
    (df["Quantity"] <= 0)
).sum()

print("\n" + "=" * 60)
print("CHECKING QUANTITY")
print("=" * 60)

print(f"Invalid quantities found: {invalid_quantity}")


# Keep only valid quantities
df = df[df["Quantity"] > 0]


# --------------------------------------------
# 10. Check invalid prices
# --------------------------------------------

invalid_prices = (
    df["UnitPrice"] <= 0
).sum()

print("\n" + "=" * 60)
print("CHECKING PRODUCT PRICES")
print("=" * 60)

print(f"Invalid prices found: {invalid_prices}")


# Keep only valid prices
df = df[df["UnitPrice"] > 0]


# --------------------------------------------
# 11. Check invalid sales values
# --------------------------------------------

invalid_sales = (
    df["TotalSales"] < 0
).sum()

print("\n" + "=" * 60)
print("CHECKING SALES VALUES")
print("=" * 60)

print(f"Invalid sales values found: {invalid_sales}")


# Keep only valid sales
df = df[df["TotalSales"] >= 0]


# --------------------------------------------
# 12. Check required text fields
# --------------------------------------------

required_columns = [
    "OrderID",
    "CustomerID",
    "CustomerName",
    "City",
    "ProductID",
    "ProductName",
    "Category",
    "PaymentMethod"
]

print("\n" + "=" * 60)
print("CHECKING REQUIRED FIELDS")
print("=" * 60)

for column in required_columns:

    missing = df[column].isnull().sum()

    print(f"{column}: {missing} missing values")


# --------------------------------------------
# 13. Remove rows missing important information
# --------------------------------------------

df = df.dropna(
    subset=required_columns
)


# --------------------------------------------
# 14. Remove impossible discount values
# --------------------------------------------

df = df[
    (df["DiscountPercentage"] >= 0)
    &
    (df["DiscountPercentage"] <= 100)
]


# --------------------------------------------
# 15. Sort data
# --------------------------------------------

df = df.sort_values(
    by="OrderDate"
)


# --------------------------------------------
# 16. Save cleaned dataset
# --------------------------------------------

df.to_csv(
    output_file,
    index=False
)


# --------------------------------------------
# 17. Final report
# --------------------------------------------

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("=" * 60)

print(f"Original rows : 3000")
print(f"Clean rows    : {len(df)}")
print(f"Removed rows  : {3000 - len(df)}")

print(f"\nClean file:")
print(output_file)

print("\nFinal dataset information:")
print(df.info())

print("\nFirst 5 cleaned records:")
print(df.head())

print("=" * 60)