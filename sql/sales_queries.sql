-- ============================================
-- RETAIL SALES ANALYTICS
-- SQL BUSINESS ANALYSIS
-- ============================================

-- View the first 10 sales records

SELECT *
FROM sales
LIMIT 10;

-- Count total orders

SELECT COUNT(*) AS Total_Orders
FROM sales;

-- Calculate total revenue

SELECT 
    SUM(TotalSales) AS Total_Revenue
FROM sales;

-- Calculate average order value

SELECT 
    AVG(TotalSales) AS Average_Order_Value
FROM sales;

-- Calculate total quantity sold

SELECT 
    SUM(Quantity) AS Total_Quantity_Sold
FROM sales;

-- Total sales by product category

SELECT
    Category,
    SUM(TotalSales) AS Total_Sales
FROM sales
GROUP BY Category
ORDER BY Total_Sales DESC;

-- Top 10 best-selling products

SELECT
    ProductName,
    SUM(Quantity) AS Total_Quantity_Sold
FROM sales
GROUP BY ProductName
ORDER BY Total_Quantity_Sold DESC
LIMIT 10;

-- Total sales by city

SELECT
    City,
    SUM(TotalSales) AS Total_Sales
FROM sales
GROUP BY City
ORDER BY Total_Sales DESC;

-- Sales by payment method

SELECT
    PaymentMethod,
    SUM(TotalSales) AS Total_Sales
FROM sales
GROUP BY PaymentMethod
ORDER BY Total_Sales DESC;

-- Monthly sales analysis

SELECT
    SUBSTR(OrderDate, 1, 7) AS Sales_Month,
    SUM(TotalSales) AS Monthly_Sales
FROM sales
GROUP BY Sales_Month
ORDER BY Sales_Month;

-- Top 10 highest-value orders

SELECT
    OrderID,
    CustomerName,
    ProductName,
    TotalSales
FROM sales
ORDER BY TotalSales DESC
LIMIT 10;

-- Top 10 customers by revenue

SELECT
    CustomerID,
    CustomerName,
    SUM(TotalSales) AS Total_Spent
FROM sales
GROUP BY CustomerID, CustomerName
ORDER BY Total_Spent DESC
LIMIT 10;

-- Top 10 products by revenue

SELECT
    ProductName,
    Category,
    SUM(TotalSales) AS Total_Revenue
FROM sales
GROUP BY ProductName, Category
ORDER BY Total_Revenue DESC
LIMIT 10;

