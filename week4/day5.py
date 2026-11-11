import json

# This is what an API response might look like
api_response = '{"steps": 9200, "water_glasses": 8, "cold_shower": true, "protocol": "OMAD"}'

# Convert JSON string to Python dictionary
data = json.loads(api_response)

print("Type:", type(data))
print("Steps:", data["steps"])
print("Cold shower:", data["cold_shower"])
print("Protocol:", data["protocol"])

import json

# A welding workshop stores job records as JSON
job_json = '''
{
  "workshop": "Kamau Metalworks",
  "location": "Gikomba, Nairobi",
  "jobs": [
    {"client": "Wanjiru",  "item": "gate",        "material": "mild steel", "quote_kes": 28000, "paid": true},
    {"client": "Otieno",   "item": "window grills","material": "angle iron", "quote_kes": 14500, "paid": false},
    {"client": "Mwangi",   "item": "door frame",   "material": "hollow tube","quote_kes": 9800,  "paid": true}
  ]
}
'''

data = json.loads(job_json)
print("Workshop:", data["workshop"])
print("Location:", data["location"])
print()

total = 0
paid = 0
for job in data["jobs"]:
    status = "PAID" if job["paid"] else "PENDING"
    print(f"  {job['client']}: {job['item']} - KES {job['quote_kes']:,} [{status}]")
    total += job["quote_kes"]
    if job["paid"]:
        paid += job["quote_kes"]

print(f"\nTotal quoted: KES {total:,}")
print(f"Collected:    KES {paid:,}")
print(f"Outstanding:  KES {total - paid:,}")

import json

week_report = {
    "name": "James",
    "steps": [9200, 10500, 8800, 11000, 7600],
    "protocols": ["OMAD", "2MAD", "OMAD", "Autophagy Marathon", "OMAD"]
}

# Convert to JSON
json_str = json.dumps(week_report, indent=2)
print("JSON output:")
print(json_str)

# Load back and calculate average
loaded = json.loads(json_str)
avg = sum(loaded["steps"]) / len(loaded["steps"])
print(f"\nAverage steps for {loaded['name']}: {round(avg)}")