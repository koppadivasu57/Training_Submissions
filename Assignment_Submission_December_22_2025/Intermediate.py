import pandas as pd

# Load dataset
file_path = r"C:\Users\vasu\Training_Submissions\employee_salary.csv"
df = pd.read_csv(file_path)

# Intermediate: Filter records by conditions
# Condition: Salary > 60000 and Department = IT
filtered_df = df[
    (df["Salary"] > 60000) &
    (df["Department"] == "IT")
]

print("=== INTERMEDIATE: Filtered Employee Records ===")
print(filtered_df)
