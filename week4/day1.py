#Reading and Writing Files
#Writing to a File
with open("daily_log.txt", "w") as f:
    f.write("Steps: 9200\n")
    f.write("Water: 8 glasses\n")
    f.write("Protocol: OMAD\n")
    f.write("Cold shower: Yes\n")

import io

# Simulating file write using in-memory buffer
file_content = io.StringIO()
file_content.write("Steps: 9200\n")
file_content.write("Water: 8 glasses\n")
file_content.write("Protocol: OMAD\n")
file_content.write("Cold shower: Yes\n")

print("File written. Contents:")
print(file_content.getvalue())

#Reading a File
with open("daily_log.txt", "r") as f:
    content = f.read()
    print(content)

#simulating file read
import io

# Simulate file content
file_data = """Steps: 9200
Water: 8 glasses
Protocol: OMAD
Cold shower: Yes
Sleep hours: 7.5
"""

# Simulate reading the whole file
f = io.StringIO(file_data)
content = f.read()
print("Full file content:")
print(content)

#Reading Line by Line
import io

file_data = """Steps: 9200
Water: 8 glasses
Protocol: OMAD
Cold shower: Yes
Sleep hours: 7.5
"""

f = io.StringIO(file_data)
lines = f.readlines()

print(f"Number of lines: {len(lines)}")
print()
for line in lines:
    line = line.strip()  # Remove newline character at end
    print("Line:", line)



#Appending to a File
with open("daily_log.txt", "a") as f:
    f.write("Pages read: 30\n")
    f.write("Workout: bench press\n")
import io

# Start with existing content
file_data = "Steps: 9200\nWater: 8 glasses\nProtocol: OMAD\n"

# Simulate append
file_data += "Pages read: 30\n"
file_data += "Workout: bench press 5x5 at 80kg\n"

print("File after appending:")
print(file_data)

#Processing File Data
import io

file_data = """Steps: 9200
Water: 8
Protocol: OMAD
Cold shower: Yes
Sleep hours: 7.5
Pages read: 30
"""

log = {}
f = io.StringIO(file_data)
for line in f:
    line = line.strip()
    if ":" in line:
        key, value = line.split(":", 1)
        log[key.strip()] = value.strip()

print("Parsed log:")
for key, value in log.items():
    print(f"  {key}: {value}")


