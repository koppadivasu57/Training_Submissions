import pandas as pd

# Sample Data
data = {
    "Employee": ["A", "B", "C", "D", "E", "F", "G"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT"],
    "Salary": [60000, 45000, 70000, 80000, 52000, 48000, 65000]
}

df = pd.DataFrame(data)

# Summary report
summary = df.groupby("Department").agg(
    Employee_Count=("Employee", "count"),
    Average_Salary=("Salary", "mean"),
    Minimum_Salary=("Salary", "min"),
    Maximum_Salary=("Salary", "max"),
    Total_Salary=("Salary", "sum")
)

print(summary)
