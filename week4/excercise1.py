import io

# Simulated file: one line per day with step count
weekly_data = """Monday: 9200
Tuesday: 7500
Wednesday: 10500
Thursday: 8800
Friday: 6900
Saturday: 11000
Sunday: 9600
"""

goal = 8000
days_on_goal = 0

f = io.StringIO(weekly_data)
for line in f:
    line = line.strip()
    if ":" in line:
        day, steps_str = line.split(":", 1)
        steps = int(steps_str.strip())
        status = "Goal hit" if steps >= goal else "Below goal"
        print(f"{day}: {steps} steps - {status}")
        if steps >= goal:
            days_on_goal += 1

print(f"\nDays on goal: {days_on_goal}/7")

import io

# Daily egg collection log: pen, eggs_collected, feed_kg
farm_log = """Pen A,240,12
Pen B,185,10
Pen C,310,15
Pen D,92,8
Pen E,275,13
"""

total_eggs = 0
total_feed = 0
low_pens = []

f = io.StringIO(farm_log)
for line in f:
    line = line.strip()
    if line:
        pen, eggs, feed = line.split(",")
        eggs = int(eggs)
        feed = int(feed)
        efficiency = eggs / feed
        status = "Good" if eggs >= 200 else "Low yield"
        print(f"{pen}: {eggs} eggs | {feed}kg feed | {efficiency:.1f} eggs/kg [{status}]")
        total_eggs += eggs
        total_feed += feed
        if eggs < 200:
            low_pens.append(pen)

print(f"\nTotal eggs: {total_eggs}")
print(f"Total feed used: {total_feed}kg")
print(f"Pens needing attention: {', '.join(low_pens)}")