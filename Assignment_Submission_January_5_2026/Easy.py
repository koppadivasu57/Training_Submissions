import pandas as pd

# Sample Data
data = {
    "Employee": ["A", "B", "C", "D", "E"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"]
}

df = pd.DataFrame(data)

# Count employees per department
result = df.groupby("Department")["Employee"].count()

print(result)
