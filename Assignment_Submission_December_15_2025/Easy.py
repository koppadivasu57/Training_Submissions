import json

# Sample JSON data
json_data = '''
{
  "name": "Vasu",
  "role": "Data Analyst",
  "skills": ["Python", "SQL", "Pandas"],
  "experience": 3
}
'''

# Load JSON
data = json.loads(json_data)

# Print keys
print("Keys in JSON:")
for key in data.keys():
    print(key)
