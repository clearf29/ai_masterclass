import csv
import io

csv_data = """day,steps,protocol
Monday,9200,OMAD
Tuesday,7500,2MAD
Wednesday,10500,OMAD
Thursday,4200,OMAD
Friday,8800,Autophagy Marathon
Saturday,11000,2MAD
Sunday,9600,OMAD"""

f = io.StringIO(csv_data)
reader = csv.DictReader(f)

valid_steps = []
for row in reader:
    steps = int(row["steps"])
    if steps >= 7000:
        valid_steps.append(steps)
        print(f"{row['day']}: {steps} steps ({row['protocol']})")
    else:
        print(f"{row['day']}: {steps} steps - flagged as invalid")

avg = sum(valid_steps) / len(valid_steps)
print(f"\nAverage (valid days): {round(avg)} steps")


import csv, io

harvest_csv = """field,crop,bags_harvested,target_bags
North Plot,Maize,48,50
South Plot,Beans,22,30
East Plot,Wheat,61,55
West Plot,Maize,35,50
Centre Plot,Sorghum,44,40
"""

reader = csv.DictReader(io.StringIO(harvest_csv))

print(f"{'Field':<15} {'Crop':<10} {'Harvested':>10} {'Target':>8} {'Status':>12}")
print("-" * 58)

for row in reader:
    harvested = int(row["bags_harvested"])
    target = int(row["target_bags"])
    pct = (harvested / target) * 100
    status = "On target" if harvested >= target else f"Short by {target - harvested} bags"
    print(f"{row['field']:<15} {row['crop']:<10} {harvested:>10} {target:>8} {status:>12}")


    