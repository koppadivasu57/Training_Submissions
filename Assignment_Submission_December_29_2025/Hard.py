import sqlite3

conn = sqlite3.connect("hard.db")
cursor = conn.cursor()

# Drop tables in correct order (child → parent)
cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("DROP TABLE IF EXISTS departments")
cursor.execute("DROP TABLE IF EXISTS companies")

# Create tables
cursor.execute("""
CREATE TABLE companies (
    company_id INTEGER PRIMARY KEY,
    company_name TEXT
)
""")

cursor.execute("""
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT,
    company_id INTEGER
)
""")

cursor.execute("""
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT,
    department_id INTEGER,
    manager_id INTEGER
)
""")

# Insert data
cursor.executemany("INSERT INTO companies VALUES (?, ?)", [
    (1, "TechCorp")
])

cursor.executemany("INSERT INTO departments VALUES (?, ?, ?)", [
    (1, "IT", 1),
    (2, "HR", 1)
])

cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", [
    (1, "Alice", 1, None),
    (2, "Bob", 1, 1),
    (3, "Charlie", 2, None),
    (4, "David", 2, 3)
])

conn.commit()

# Hierarchical join query
query = """
SELECT
    c.company_name,
    d.department_name,
    e.emp_name AS employee,
    m.emp_name AS manager
FROM companies c
JOIN departments d ON c.company_id = d.company_id
JOIN employees e ON d.department_id = e.department_id
LEFT JOIN employees m ON e.manager_id = m.emp_id
ORDER BY d.department_name, employee;
"""

cursor.execute(query)

print("Company Hierarchy:")
for row in cursor.fetchall():
    print(row)

conn.close()
