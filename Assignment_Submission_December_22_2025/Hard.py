import pandas as pd

# Load dataset
file_path = r"C:\Users\vasu\Training_Submissions\employee_salary.csv"
df = pd.read_csv(file_path)

# Hard: Top 5 highest-paid employees (based on Salary)
top_5 = df.sort_values(by="Salary", ascending=False).head(5)

print("=== HARD: Top 5 Highest-Paid Employees ===")
print(top_5)
