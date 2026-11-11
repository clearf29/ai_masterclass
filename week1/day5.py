daily_steps =[8200, 5100, 11300, 6800, 9400, 4200, 10100]
target =8000

for steps in daily_steps:
    print(f"Checking: {steps} steps")
    if steps >= target:
        print(f"Target hit on this day: {steps} steps. Let's rest.")
        continue


total = 0
valid_days = 0
minimum = 5000

for steps in daily_steps:
    if steps < minimum:
        print(f"Skipping {steps} (below minimum)")
        continue   # skip this day, go to next
    total += steps
    valid_days += 1

print(f"\nValid days: {valid_days}")
print(f"Total steps (valid days): {total}")
print(f"Average: {total // valid_days}")


# 3. While loop: consecutive streak from start
streak = 0
i = 0
while i < len(daily_steps) and daily_steps[i] >= target:
    streak += 1
    i += 1

# 4. Weekly summary
print("\nWeekly Summary:")
print(f"Total valid days (>=5000 steps): {valid_days}")
print(f"Average steps (valid days only): {total // valid_days}")
print(f"Consecutive streak from start hitting target: {streak}")