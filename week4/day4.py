# A dairy farmer records daily milk output (litres) from 3 cows.
# Some days the entry is wrong or missing.

def calculate_daily_average(milk_records):
    try:
        total = sum(milk_records)
        avg = total / len(milk_records)
        return round(avg, 2)
    except ZeroDivisionError:
        print("Error: No records found. Cannot calculate average.")
        return 0
    except TypeError:
        print("Error: Records contain non-numeric values.")
        return 0

print("Average litres:", calculate_daily_average([18.5, 20.0, 17.8, 19.2]))
print("Average litres:", calculate_daily_average([]))
print("Average litres:", calculate_daily_average([18.5, "missing", 17.8]))

#else and finally
# A tiling contractor calculates cost per tile for each job.
# If zero tiles are entered by mistake, the program should not crash.

def cost_per_tile(total_cost, num_tiles):
    try:
        result = total_cost / num_tiles
    except ZeroDivisionError:
        print("Cannot divide: zero tiles entered.")
    else:
        print(f"KES {total_cost} / {num_tiles} tiles = KES {result:.2f} per tile")
    finally:
        print("(Calculation attempted)")
    print()

cost_per_tile(45000, 300)
cost_per_tile(30000, 0)
cost_per_tile(62400, 480)

#Raising my own errors
def log_steps(steps):
    if not isinstance(steps, int):
        raise TypeError("Steps must be an integer.")
    if steps < 0:
        raise ValueError("Steps cannot be negative.")
    print(f"Steps logged: {steps}")

try:
    log_steps(9200)
    log_steps("nine thousand")
except ValueError as e:
    print("ValueError:", e)
except TypeError as e:
    print("TypeError:", e)
#Error Handling With Data Processing
daily_logs = [
    {"day": "Monday",    "steps": "9200"},
    {"day": "Tuesday",   "steps": "not recorded"},
    {"day": "Wednesday", "steps": "10500"},
    {"day": "Thursday",  "steps": None},
    {"day": "Friday",    "steps": "8800"},
]

valid_steps = []
for log in daily_logs:
    try:
        steps = int(log["steps"])
        valid_steps.append(steps)
        print(f"{log['day']}: {steps} steps")
    except (ValueError, TypeError):
        print(f"{log['day']}: invalid data - skipped")

if valid_steps:
    avg = sum(valid_steps) / len(valid_steps)
    print(f"\nAverage from valid days: {round(avg)} steps")

#excersise 
def safe_log_entry(data):
    try:
        steps = int(data["steps"])
    except (ValueError, TypeError, KeyError):
        print("Invalid steps data. Skipping entry.")
        return None

    water    = data.get("water", 0)
    protocol = data.get("protocol", "Unknown")

    print(f"Steps: {steps} | Water: {water} glasses | Protocol: {protocol}")
    return steps

entries = [
    {"steps": "9200", "water": 8,   "protocol": "OMAD"},
    {"steps": "bad",  "water": 7,   "protocol": "2MAD"},
    {"steps": "8800", "protocol": "OMAD"},
    {"steps": "11000","water": 9},
]

results = [safe_log_entry(e) for e in entries]
valid = [r for r in results if r is not None]
print(f"\nValid entries: {len(valid)}")    


import json

daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5
}

# Convert to JSON string
json_text = json.dumps(daily_log)
print("Type:", type(json_text))
print("JSON:", json_text)

# Pretty print with indentation
pretty = json.dumps(daily_log, indent=2)
print("\nPretty JSON:")
print(pretty)