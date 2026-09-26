import pandas as pd
import sqlite3
from pathlib import Path


# ============================================
# RETAIL SALES ANALYTICS
# Create SQLite Database
# ============================================


# --------------------------------------------
# 1. Find project folders
# --------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
SQL_DIR = BASE_DIR / "sql"


# Make sure the SQL folder exists
SQL_DIR.mkdir(exist_ok=True)


# --------------------------------------------
# 2. File locations
# --------------------------------------------

input_file = DATA_DIR / "clean_sales_data.csv"

database_file = SQL_DIR / "retail_sales.db"


# --------------------------------------------
# 3. Load cleaned CSV data
# --------------------------------------------

df = pd.read_csv(input_file)


print("=" * 60)
print("CREATING RETAIL SALES SQL DATABASE")
print("=" * 60)

print(f"Rows loaded from CSV : {len(df):,}")
print(f"Columns loaded       : {len(df.columns)}")


# --------------------------------------------
# 4. Connect to SQLite database
# --------------------------------------------

connection = sqlite3.connect(database_file)


# --------------------------------------------
# 5. Store data in SQL table
# --------------------------------------------

df.to_sql(
    "sales",
    connection,
    if_exists="replace",
    index=False
)


# --------------------------------------------
# 6. Check number of records
# --------------------------------------------

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM sales")

row_count = cursor.fetchone()[0]


# --------------------------------------------
# 7. Close database connection
# --------------------------------------------

connection.close()


# --------------------------------------------
# 8. Display result
# --------------------------------------------

print()
print("DATABASE CREATED SUCCESSFULLY")
print("-" * 60)

print(f"Database file : {database_file}")
print(f"Table name    : sales")
print(f"Rows inserted : {row_count:,}")

print("-" * 60)
print("SQL database creation completed.")
print("=" * 60)