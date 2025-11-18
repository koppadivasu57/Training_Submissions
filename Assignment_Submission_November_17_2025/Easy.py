import pandas as pd

# ---------------------------------------------
# Create a CSV file inside the script
# ---------------------------------------------
data = {
    "id": [1, 2, 3, 4],
    "name": ["John", "Mary", "Alex", "Sara"],
    "age": [28, 32, 24, 29],
    "salary": [50000, 60000, 45000, 52000]
}

df = pd.DataFrame(data)

# Save the CSV file automatically
csv_path = "sample_data.csv"
df.to_csv(csv_path, index=False)

print(f"CSV file created as: {csv_path}")

# ---------------------------------------------
# Load CSV file into DataFrame
# ---------------------------------------------
df_loaded = pd.read_csv(csv_path)

print("\n=== Loaded Data ===")
print(df_loaded.head())

print("\n=== Data Info ===")
print(df_loaded.info())

print("\n=== Statistical Summary ===")
print(df_loaded.describe())
