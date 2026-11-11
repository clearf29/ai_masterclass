import micropip
await micropip.install("scikit-learn")
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Train
X = np.array([[7.5,7,80],[8.0,8,82],[6.5,6,78],[7.0,9,85],[9.0,8,80],[7.5,7,83],[8.0,8,84],[6.0,6,81],[8.5,9,85],[7.0,8,80],[7.5,8,86],[9.0,7,79],[7.0,9,84],[7.5,8,83],[7.0,7,82],[8.0,8,86],[6.5,6,79],[7.5,9,88],[8.0,8,81],[7.0,7,85],[8.5,9,87],[7.0,8,82],[7.5,8,86],[6.5,6,80],[8.0,9,87],[9.5,7,79],[7.0,8,84],[8.0,9,86]])
steps_y = np.array([9200,10500,8800,11000,7600,9400,10200,8900,10800,9100,11200,7900,10000,9700,9500,10300,8600,11500,8200,9800,10600,9000,10100,8400,10900,7500,9600,10400])
y = (steps_y >= 10000).astype(int)
clf = RandomForestClassifier(n_estimators=20, random_state=42)
clf.fit(X, y)

# Reusable function
def predict_day(sleep_hours, water_glasses, bench_kg):
    """
    Predict whether today will be a 10k step day.
    Returns: dict with prediction, confidence, and recommendation.
    """
    inputs = np.array([[sleep_hours, water_glasses, bench_kg]])
    pred = clf.predict(inputs)[0]
    proba = clf.predict_proba(inputs)[0]
    confidence = max(proba)

    result = {
        "hit_goal": bool(pred),
        "confidence": round(confidence * 100, 1),
        "recommendation": ""
    }

    if pred == 0 and confidence > 0.7:
        result["recommendation"] = "Low step day likely. Schedule a walk this afternoon."
    elif pred == 1 and confidence > 0.7:
        result["recommendation"] = "High step day likely. Good conditions today."
    else:
        result["recommendation"] = "Borderline day. Stay intentional about movement."

    return result

# Test with three different days
scenarios = [
    (8.0, 8, 84, "James Omondi"),
    (6.0, 5, 78, "Brian Kamau"),
    (9.0, 9, 87, "Grace Achieng"),
]

for sleep, water, bench, name in scenarios:
    r = predict_day(sleep, water, bench)
    outcome = "Goal hit" if r["hit_goal"] else "Below goal"
    print(f"{name}: {outcome} ({r['confidence']}% confidence)")
    print(f"  {r['recommendation']}")
    print()



import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Training data: [feed_kg_per_day, lactation_day]
# Label: 1 = above 15L that day, 0 = below
X = np.array([
    [6.5, 30],[7.0, 45],[5.5, 20],[7.5, 60],[6.0, 25],
    [8.0, 75],[5.0, 15],[7.2, 50],[6.8, 40],[7.8, 70],
    [5.8, 22],[7.3, 55],[6.2, 28],[8.1, 80],[5.3, 18],
    [7.1, 48],[6.6, 35],[7.6, 65],[5.7, 21],[7.9, 72],
])
y = np.array([1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1])

clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X, y)

def predict_cow_yield(feed_kg, lactation_day):
    inputs = np.array([[feed_kg, lactation_day]])
    pred = clf.predict(inputs)[0]
    proba = clf.predict_proba(inputs)[0]
    confidence = max(proba) * 100
    status = "Above 15L target" if pred == 1 else "Below target"
    return status, round(confidence, 1)

cows = [
    ("Cow 1 (Kamau farm)", 7.2, 50),
    ("Cow 2 (Wanjiku farm)", 5.5, 20),
    ("Cow 3 (Mwangi farm)", 7.8, 70),
]
print("Githunguri Dairy: Daily Yield Predictions")
print()
for name, feed, day in cows:
    status, conf = predict_cow_yield(feed, day)
    print(f"  {name}")
    print(f"    Feed={feed}kg  Lactation day={day}")
    print(f"    => {status} ({conf:.0f}% confidence)")
    print()