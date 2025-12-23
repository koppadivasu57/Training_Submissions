import pandas as pd

# Load dataset
file_path = r"C:\Users\vasu\Training_Submissions\employee_salary.csv"
df = pd.read_csv(file_path)

# Retrieve all records
print("=== EASY: All Employee Records ===")
print(df)
