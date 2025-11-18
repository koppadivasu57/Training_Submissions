import pandas as pd

# ---------------------------------------------
# Create sales data directly inside the script
# ---------------------------------------------
sales_data = {
    "Region": ["East", "West", "East", "South", "North", "West", "South", "East"],
    "Sales": [200, 150, 300, 400, 220, 180, 350, 250]
}

df_sales = pd.DataFrame(sales_data)

print("=== Original Sales Data ===")
print(df_sales)

# ---------------------------------------------
# Group by Region and calculate total sales
# ---------------------------------------------
grouped_totals = df_sales.groupby("Region")["Sales"].sum()

print("\n=== Total Sales by Region ===")
print(grouped_totals)
