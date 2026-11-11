import math

def estimate_calories(steps, calories_per_step=0.04):
    calories = steps * calories_per_step
    return math.floor(calories)

weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]
daily_cals = [estimate_calories(s) for s in weekly_steps]

print("Estimated daily calories burned from walking:")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for day, cals in zip(days, daily_cals):
    print(f"  {day}: {cals} kcal")
print(f"  Total: {sum(daily_cals)} kcal")