import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "ecommerce_sales.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_FILE, parse_dates=["Order_Date"])

# ---------------------------
# 1. Data quality checks
# ---------------------------
print("DATASET SHAPE:", df.shape)
print("\nMISSING VALUES:\n", df.isnull().sum())
print("\nDUPLICATE ROWS:", df.duplicated().sum())
print("\nDATA TYPES:\n", df.dtypes)

# ---------------------------
# 2. KPI summary
# ---------------------------
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
total_quantity = df["Quantity"].sum()
profit_margin = total_profit / total_sales * 100

print("\nKEY PERFORMANCE INDICATORS")
print(f"Total sales: PKR {total_sales:,.2f}")
print(f"Total profit: PKR {total_profit:,.2f}")
print(f"Total orders: {total_orders:,}")
print(f"Units sold: {total_quantity:,}")
print(f"Profit margin: {profit_margin:.2f}%")

# ---------------------------
# 3. Monthly performance
# ---------------------------
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
monthly = df.groupby("Month", as_index=False).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order_ID", "nunique")
)
monthly.to_csv(OUTPUT_DIR / "monthly_performance.csv", index=False)

# ---------------------------
# 4. Category performance
# ---------------------------
category = df.groupby("Category", as_index=False).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order_ID", "nunique"),
    Quantity=("Quantity", "sum")
).sort_values("Sales", ascending=False)
category.to_csv(OUTPUT_DIR / "category_performance.csv", index=False)

# ---------------------------
# 5. City performance
# ---------------------------
city = df.groupby("City", as_index=False).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order_ID", "nunique")
).sort_values("Sales", ascending=False)
city.to_csv(OUTPUT_DIR / "city_performance.csv", index=False)

# ---------------------------
# 6. Product performance
# ---------------------------
product = df.groupby("Product", as_index=False).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).sort_values("Sales", ascending=False)
product.to_csv(OUTPUT_DIR / "product_performance.csv", index=False)

# ---------------------------
# 7. Payment method analysis
# ---------------------------
payment = df.groupby("Payment_Method", as_index=False).agg(
    Orders=("Order_ID", "nunique"),
    Sales=("Sales", "sum")
).sort_values("Orders", ascending=False)
payment.to_csv(OUTPUT_DIR / "payment_method_analysis.csv", index=False)

# ---------------------------
# 8. Visualizations
# ---------------------------
plt.figure(figsize=(10, 5))
plt.plot(monthly["Month"], monthly["Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (PKR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "monthly_sales_trend.png", dpi=150)
plt.close()

plt.figure(figsize=(9, 5))
plt.bar(category["Category"], category["Sales"])
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales (PKR)")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sales_by_category.png", dpi=150)
plt.close()

plt.figure(figsize=(9, 5))
plt.bar(city["City"], city["Sales"])
plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Sales (PKR)")
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sales_by_city.png", dpi=150)
plt.close()

plt.figure(figsize=(9, 5))
plt.bar(product.head(10)["Product"], product.head(10)["Profit"])
plt.title("Top 10 Products by Profit")
plt.xlabel("Product")
plt.ylabel("Profit (PKR)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "top_products_by_profit.png", dpi=150)
plt.close()

print("\nAnalysis complete. Results saved in the outputs folder.")
