import matplotlib.pyplot as plt

# ▶ Embedded sales dataset (no external file needed)
sales_data = {
    "North": 72000,
    "South": 68000,
    "East": 70000,
    "West": 74000
}

# Extract keys and values
regions = list(sales_data.keys())
sales = list(sales_data.values())

# Create bar chart
plt.figure(figsize=(7,5))
plt.bar(regions, sales)

# Title and labels
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales Amount ($)")
plt.tight_layout()

# Show chart
plt.show()
