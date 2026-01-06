import pandas as pd

# Sample Data
data = {
    "Employee": ["A", "B", "C", "D", "E", "F"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Salary": [60000, 45000, 70000, 80000, 52000, 48000]
}

df = pd.DataFrame(data)

# Average salary per department
avg_salary = df.groupby("Department")["Salary"].mean()

# Filter departments with avg salary > 50000
result = avg_salary[avg_salary > 50000]

print(result)
