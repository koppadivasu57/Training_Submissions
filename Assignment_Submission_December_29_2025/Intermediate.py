import sqlite3

conn = sqlite3.connect("intermediate.db")
cursor = conn.cursor()

# Drop table if it already exists
cursor.execute("DROP TABLE IF EXISTS employees")

# Create table
cursor.execute("""
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT,
    department TEXT,
    salary REAL
)
""")

# Insert data
cursor.executemany("""
INSERT INTO employees VALUES (?, ?, ?, ?)
""", [
    (1, "Alice", "IT", 70000),
    (2, "Bob", "IT", 50000),
    (3, "Charlie", "HR", 60000),
    (4, "David", "HR", 40000)
])

conn.commit()

# Subquery
query = """
SELECT emp_name, department, salary
FROM employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department = e.department
);
"""

cursor.execute(query)

print("Employees earning above department average:")
for row in cursor.fetchall():
    print(row)

conn.close()
