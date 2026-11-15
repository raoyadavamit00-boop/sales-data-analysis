import pandas as pd
import matplotlib.pyplot as plt

print("SALES DATA ANALYSIS PROJECT")
print("---------------------------")

print("Libraries imported successfully!")
import pandas as pd
import matplotlib.pyplot as plt

# Create sales dataset
data = {
    "Date": [
        "2026-01-01", "2026-01-02", "2026-01-03",
        "2026-01-04", "2026-01-05", "2026-01-06",
        "2026-01-07", "2026-01-08", "2026-01-09",
        "2026-01-10"
    ],
    "Product": [
        "Laptop", "Mobile", "Headphones", "Laptop",
        "Mouse", "Mobile", "Keyboard", "Headphones",
        "Laptop", "Mouse"
    ],
    "Category": [
        "Electronics", "Electronics", "Accessories",
        "Electronics", "Accessories", "Electronics",
        "Accessories", "Accessories", "Electronics",
        "Accessories"
    ],
    "Quantity": [2, 3, 5, 1, 10, 2, 4, 6, 1, 8],
    "Price": [50000, 20000, 1500, 50000, 500, 20000,
              1000, 1500, 50000, 500]
}

df = pd.DataFrame(data)

# Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Save dataset
df.to_csv("sales_data.csv", index=False)

print("Sales Dataset Created Successfully!")
print(df)

# Basic Sales Analysis

total_revenue = df["Total_Sales"].sum()

total_orders = len(df)

total_quantity = df["Quantity"].sum()

average_sales = df["Total_Sales"].mean()

print("\n------ SALES SUMMARY ------")

print("Total Revenue:", total_revenue)

print("Total Orders:", total_orders)

print("Total Quantity Sold:", total_quantity)

print("Average Sales:", average_sales)

# Best Selling Product

best_product = df.groupby("Product")["Quantity"].sum()

print("\n------ PRODUCT ANALYSIS ------")
print(best_product)

print("\nBest Selling Product:",
      best_product.idxmax())

# PRODUCT ANALYSIS

print("\n==============================")
print("       PRODUCT ANALYSIS")
print("==============================")

product_sales = df.groupby("Product")["Quantity"].sum()

print("\nProduct-wise Sales:")
print(product_sales)

best_product = product_sales.idxmax()

print("\nBest Selling Product:", best_product)

# PRODUCT SALES GRAPH

product_sales = df.groupby("Product")["Quantity"].sum()

plt.figure(figsize=(8, 5))

product_sales.plot(kind="bar")

plt.title("Product Wise Sales Analysis")
plt.xlabel("Product Name")
plt.ylabel("Quantity Sold")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# CATEGORY WISE SALES GRAPH

category_sales = df.groupby("Category")["Total_Sales"].sum()

plt.figure(figsize=(7, 5))

category_sales.plot(kind="bar", color="orange")

plt.title("Category Wise Sales Analysis")
plt.xlabel("Category")
plt.ylabel("Total Revenue")

plt.tight_layout()
plt.show()

# DAILY SALES TREND

df["Date"] = pd.to_datetime(df["Date"])

daily_sales = df.groupby("Date")["Total_Sales"].sum()

plt.figure(figsize=(9, 5))

daily_sales.plot(kind="line", marker="o")

plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Revenue")

plt.grid(True)
plt.tight_layout()
plt.show()

# PRODUCT REVENUE ANALYSIS

product_revenue = df.groupby("Product")["Total_Sales"].sum()

print("\n===== REVENUE ANALYSIS =====")

print(product_revenue)

print("\nHighest Revenue Product:",
      product_revenue.idxmax())

print("Highest Revenue:",
      product_revenue.max())

# FINAL SALES REPORT

print("\n================================")
print("       FINAL SALES REPORT")
print("================================")

print("Total Revenue: Rs.", df["Total_Sales"].sum())

print("Total Orders:", len(df))

print("Total Products:", df["Product"].nunique())

print("Total Quantity Sold:", df["Quantity"].sum())

print("Average Order Value: Rs.",
      round(df["Total_Sales"].mean(), 2))

print("Best Selling Product:",
      df.groupby("Product")["Quantity"].sum().idxmax())

print("Highest Revenue Product:",
      df.groupby("Product")["Total_Sales"].sum().idxmax())

print("================================")
print("       REPORT COMPLETED")
print("================================")