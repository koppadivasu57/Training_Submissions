import sqlite3

conn = sqlite3.connect("easy.db")
cursor = conn.cursor()

# Drop tables if they already exist
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS customers")

# Create tables
cursor.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    city TEXT
)
""")

cursor.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    amount REAL
)
""")

# Insert data
cursor.executemany("""
INSERT INTO customers VALUES (?, ?, ?)
""", [
    (1, "Alice", "New York"),
    (2, "Bob", "Chicago")
])

cursor.executemany("""
INSERT INTO orders VALUES (?, ?, ?, ?)
""", [
    (101, 1, "2025-12-01", 250.00),
    (102, 2, "2025-12-03", 400.00)
])

conn.commit()

# Join query
query = """
SELECT 
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.order_date,
    o.amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;
"""

cursor.execute(query)

print("Customer Orders:")
for row in cursor.fetchall():
    print(row)

conn.close()
