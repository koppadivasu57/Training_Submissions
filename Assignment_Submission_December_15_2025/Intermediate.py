import pandas as pd

# Sample data
data = {
    "Employee": ["A", "B", "C"],
    "Department": ["IT", "HR", "IT"],
    "Salary": [60000, 50000, 70000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Transform: increase salary by 10%
df["Updated_Salary"] = df["Salary"] * 1.10

# Save to CSV
df.to_csv("employee_salary.csv", index=False)

print("CSV file created successfully!")
print(df)
