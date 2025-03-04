import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sales data
df = pd.read_csv("sales_data.csv")

# Convert date column to datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Calculate revenue per order
df['revenue'] = df['price'] * df['quantity']

# Monthly Revenue Trend
df_monthly = df.resample('M', on='order_date')['revenue'].sum()

plt.figure(figsize=(10, 5))
df_monthly.plot(kind='line', marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid()
plt.show()

# Top 5 Best-Selling Products
top_products = df.groupby("product_name")["revenue"].sum().nlargest(5)

plt.figure(figsize=(8, 5))
top_products.plot(kind="bar", color="skyblue")
plt.title("Top 5 Best-Selling Products")
plt.xlabel("Product Name")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()
