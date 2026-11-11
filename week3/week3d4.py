clients = [
    {"name": "James",   "goal": "fat loss",    "sessions": 4},
    {"name": "Mwangi",  "goal": "muscle gain", "sessions": 5},
    {"name": "Sandra",  "goal": "endurance",   "sessions": 3},
    {"name": "Patrick", "goal": "fat loss",    "sessions": 4},
    {"name": "Grace",   "goal": "fat loss",    "sessions": 3},
]

# Get names of all fat loss clients
fat_loss_names = [c["name"] for c in clients if c["goal"] == "fat loss"]
print("Fat loss clients:", fat_loss_names)

# Get all clients with 4 or more sessions per week
active_clients = [c for c in clients if c["sessions"] >= 4]
print("Active clients:", [c["name"] for c in active_clients])

weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

# Build a list of status strings for each day
statuses = ["Goal hit" if s >= 8000 else "Below goal" for s in weekly_steps]

for i, status in enumerate(statuses):
    print(f"Day {i+1}: {weekly_steps[i]} steps - {status}")




people = [
    {"name": "James",   "steps": [9200, 10500, 8800, 11000, 7600, 9400, 10200]},
    {"name": "Sandra",  "steps": [7000, 7500, 6800, 8000, 7200, 8500, 7800]},
    {"name": "Mwangi",  "steps": [10000, 11500, 9800, 12000, 10500, 11000, 10800]},
    {"name": "Patrick", "steps": [8500, 9000, 8800, 9200, 8600, 9400, 9100]},
]

# 1. All step counts above 10,000 across all people
all_steps = [s for p in people for s in p["steps"]]
high_steps = [s for s in all_steps if s > 10000]
print("Steps above 10,000:", high_steps)

# 2. Names with average steps above 9,000
high_avg_names = [p["name"] for p in people if sum(p["steps"]) / len(p["steps"]) > 9000]
print("High average performers:", high_avg_names)