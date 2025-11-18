import pandas as pd

# -----------------------------------------------------
# Create Orders DataFrame
# -----------------------------------------------------
orders_data = {
    "OrderID": [1, 2, 3, 4, 5],
    "CustomerID": [101, 102, 101, 103, 104],
    "Product": ["Laptop", "Phone", "Phone", "Tablet", "Laptop"],
    "Amount": [800, 500, 300, 450, 900]
}

df_orders = pd.DataFrame(orders_data)

print("=== Orders Data ===")
print(df_orders)


# -----------------------------------------------------
# Create Customers DataFrame
# -----------------------------------------------------
customers_data = {
    "CustomerID": [101, 102, 103, 104],
    "CustomerName": ["John D", "Mary S", "Alex K", "Sarah W"],
    "Region": ["East", "West", "East", "South"]
}

df_customers = pd.DataFrame(customers_data)

print("\n=== Customers Data ===")
print(df_customers)


# -----------------------------------------------------
# Merge both DataFrames on CustomerID
# -----------------------------------------------------
merged_df = pd.merge(df_orders, df_customers, on="CustomerID", how="inner")

print("\n=== Merged DataFrame ===")
print(merged_df)


# -----------------------------------------------------
# Create Pivot Table
# -----------------------------------------------------
pivot_table = merged_df.pivot_table(
    values="Amount",
    index="Region",
    columns="Product",
    aggfunc="sum",
    fill_value=0
)

print("\n=== Pivot Table: Region vs Product Sales ===")
print(pivot_table)
