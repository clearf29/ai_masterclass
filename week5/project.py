
import csv, io
csv_data = """name, score1,score2,score3
James Omondi, 85,90,78   
Sandra Weru, 72,,88
Patrick Njiru,91,87,94
Grace Achieng, 60,bad data,70
Brian Kmanu, 55,48,62"""

f = io.StringIO(csv_data)
reader = csv.DictReader(f)

for row in reader:
    print(dict(row))
#Parse scores Safely
def parse_scores(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None
#Calculate Average and Letter Grade
def calculate_average(scores):
    valid = [s for s in scores if s is not None]
    if not valid:
        return None
    return round(sum(valid) / len(valid), 1)

def letter_grade(avg):
    if avg is None:
        return "N/A"
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# Test
scores_a = [85, 90, 78]
scores_b = [72, None, 88]
scores_c = [60, None, None]

for s in [scores_a, scores_b, scores_c]:
    avg = calculate_average(s)
    print(f"Scores: {s} | Avg: {avg} | Grade: {letter_grade(avg)}")
    # name = row["name"]
    # scores = []
    # for key in ["score1", "score2", "score3"]:
    #     try:
    #         score = int(row[key])
    #         scores.append(score)
    #     except (ValueError, TypeError):
    #         print(f"Warning: Invalid score '{row[key]}' for {name} in {key}. Skipping this score.")
