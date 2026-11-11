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

#Writing CSV with csv.writer

import csv
import io

output = io.StringIO()
writer = csv.writer(output)

# Write header
writer.writerow(["name", "steps", "protocol", "goal_hit"])

# Write data rows
data = [
    ["James",   9200,  "OMAD",              True],
    ["Sandra",  10500, "2MAD",              True],
    ["Patrick", 7600,  "OMAD",              False],
    ["Grace",   11000, "Autophagy Marathon", True],
]

for row in data:
    writer.writerow(row)

print("Generated CSV:")
print(output.getvalue())

#Reading with DictReader

import csv
import io

csv_data = """name,steps,water,protocol,cold_shower
James Omondi,9200,8,OMAD,True
Sandra Weru,10500,9,2MAD,True
Patrick Njiru,7600,6,OMAD,False
Grace Achieng,11000,8,Autophagy Marathon,True"""

f = io.StringIO(csv_data)
reader = csv.DictReader(f)

for row in reader:
    steps = int(row["steps"])
    status = "Goal hit" if steps >= 8000 else "Below goal"
    print(f"{row['name']}: {steps} steps | {row['protocol']} | {status}")


#Reading CSV with csv.reader

import csv
import io

# Simulated CSV content
csv_data = """name,phone,skill,city
James Omondi,0712345678,welding,Nairobi
Sandra Weru,0723456789,tiling,Mombasa
Patrick Njiru,0734567890,phone repair,Nairobi
Grace Achieng,0745678901,copywriting,Kisumu
Brian Kamau,0756789012,upholstery,Nairobi"""

f = io.StringIO(csv_data)
reader = csv.reader(f)

for row in reader:
    print(row)