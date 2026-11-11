# Simulates what response.json() returns from a fitness API
data = {
    "user_id": 1,
    "name": "James Omondi",
    "date": "2024-11-18",
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5,
    "workout_completed": True
}

print("Name:", data["name"])
print("Steps:", data["steps"])
print("Protocol:", data["fasting_protocol"])
print("Cold shower:", data["cold_shower"])
print("Sleep:", data["sleep_hours"], "hours")

users = [
    {"name": "James Omondi",  "workout": {"bench_press_kg": 80, "duration_minutes": 45}},
    {"name": "Sandra Weru",   "workout": None},   # did not train today
    {"name": "Grace Achieng", "workout": {"bench_press_kg": 60, "duration_minutes": 40}},
]

for user in users:
    name = user["name"]
    workout = user["workout"]
    if workout is None:
        print(f"{name}: rest day")
    else:
        bench = workout.get("bench_press_kg", "not recorded")
        mins = workout.get("duration_minutes", "?")
        print(f"{name}: bench={bench}kg, duration={mins}min")


# Raw API response: list of full user records
raw = [
    {"id": 1, "name": "James Omondi",  "email": "james@smp.ke", "steps": 9200,  "protocol": "OMAD", "sleep": 7.5, "active": True},
    {"id": 2, "name": "Sandra Weru",   "email": "sw@smp.ke",    "steps": 10500, "protocol": "2MAD", "sleep": 8.0, "active": True},
    {"id": 3, "name": "Patrick Njiru", "email": "pn@smp.ke",    "steps": 8100,  "protocol": "OMAD", "sleep": 6.5, "active": False},
    {"id": 4, "name": "Grace Achieng", "email": "ga@smp.ke",    "steps": 11000, "protocol": "OMAD", "sleep": 7.0, "active": True},
    {"id": 5, "name": "Brian Kamau",   "email": "bk@smp.ke",    "steps": 7400,  "protocol": "2MAD", "sleep": 9.0, "active": True},
]

# Extract only active users with name, steps, protocol
clean = [
    {
        "name": r["name"],
        "steps": r["steps"],
        "protocol": r["protocol"]
    }
    for r in raw if r["active"]
]

for record in clean:
    print(f"{record['name']:20} {record['steps']:6} steps  {record['protocol']}")


api_response = {
    "week": "2024-W47",
    "members": [
        {"name": "James Omondi",  "daily_steps": [9200, 10100, 8800, 11000, 9400, 10200, 8600]},
        {"name": "Sandra Weru",   "daily_steps": [10500, 9800, 10200, 11500, 9100, 10800, 10000]},
        {"name": "Patrick Njiru", "daily_steps": [8100, 7900, 8500, 9200, 8800, 7600, 9000]},
        {"name": "Grace Achieng", "daily_steps": [11000, 10800, 9900, 12000, 10500, 11200, 10300]},
    ]
}

print(f"Week: {api_response['week']}")
print("-" * 50)
print(f"{'Name':<20} {'Avg Steps':>10}  {'Days 10k+':>10}  {'Max Steps':>10}")
print("-" * 50)

for member in api_response["members"]:
    steps = member["daily_steps"]
    avg = round(sum(steps) / len(steps))
    days_hit = sum(1 for s in steps if s >= 10000)
    max_steps = max(steps)
    print(f"{member['name']:<20} {avg:>10,}  {days_hit:>10}  {max_steps:>10,}")


raw_members = [
    {
        "profile": {"name": "James Omondi", "city": "Nairobi"},
        "metrics": {"steps": 9200, "sleep_hours": 7.5, "bench_press_kg": 80},
        "discipline": {"cold_shower": True, "protocol": "OMAD"}
    },
    {
        "profile": {"name": "Grace Achieng", "city": "Mombasa"},
        "metrics": {"steps": 11000, "sleep_hours": 7.0, "bench_press_kg": 60},
        "discipline": {"cold_shower": False, "protocol": "OMAD"}
    },
    {
        "profile": {"name": "Brian Kamau", "city": "Kisumu"},
        "metrics": {"steps": 7400, "sleep_hours": 9.0, "bench_press_kg": 70},
        "discipline": {"cold_shower": True, "protocol": "2MAD"}
    },
]

# Flatten each nested record into one clean dict
flattened = []
for m in raw_members:
    record = {
        "name":       m["profile"]["name"],
        "city":       m["profile"]["city"],
        "steps":      m["metrics"]["steps"],
        "sleep":      m["metrics"]["sleep_hours"],
        "bench":      m["metrics"]["bench_press_kg"],
        "protocol":   m["discipline"]["protocol"],
        "cold_shower": m["discipline"]["cold_shower"],
    }
    flattened.append(record)

for r in flattened:
    shower = "yes" if r["cold_shower"] else "no"
    print(f"{r['name']}, {r['city']}: {r['steps']} steps, {r['protocol']}, shower={shower}")


# This is what the X API v2 returns when you fetch a post
# Structure: data (the post) + includes (the author details)
x_response = {
    "data": {
        "id": "2076589716036608320",
        "text": "Live by a code:\n\n* Loyalty.\n* Strength.\n* Honour.\n* Discipline.\n\nIf you stand for nothing, you fall for anything.",
        "created_at": "2026-07-14T05:30:00Z",
        "author_id": "748352990",
        "public_metrics": {
            "retweet_count": 2104,
            "reply_count":    487,
            "like_count":   11380,
            "quote_count":    319,
            "bookmark_count": 4251
        }
    },
    "includes": {
        "users": [
            {
                "id": "748352990",
                "name": "Amerix",
                "username": "amerix",
                "public_metrics": {
                    "followers_count": 1200000,
                    "following_count": 487
                }
            }
        ]
    }
}

# Parse it exactly as you have been parsing all lesson
post    = x_response["data"]
author  = x_response["includes"]["users"][0]
metrics = post["public_metrics"]

print("POST")
print(f"  Author:    @{author['username']} ({author['name']})")
print(f"  Text:      {post['text'][:60]}...")
print(f"  Posted:    {post['created_at']}")
print()
print("ENGAGEMENT")
print(f"  Likes:     {metrics['like_count']:,}")
print(f"  Retweets:  {metrics['retweet_count']:,}")
print(f"  Replies:   {metrics['reply_count']:,}")
print(f"  Bookmarks: {metrics['bookmark_count']:,}")
print()
print(f"AUTHOR: @{author['username']} has {author['public_metrics']['followers_count']:,} followers")
print(f"Read more at: https://x.com/{author['username']}")


# Simulated response from a commodity prices API
commodity_response = {
    "status": "ok",
    "market": "Wakulima Market, Nairobi",
    "date": "2026-08-13",
    "prices": [
        {"commodity": "Maize",       "unit": "90kg bag", "price_kes": 3200, "change_pct": -2.1, "available": True},
        {"commodity": "Beans (Dry)", "unit": "90kg bag", "price_kes": 9800, "change_pct":  4.5, "available": True},
        {"commodity": "Milk (Raw)",  "unit": "litre",    "price_kes":   62, "change_pct":  1.2, "available": True},
        {"commodity": "Tea Leaf",    "unit": "kg",        "price_kes":   28, "change_pct": -0.8, "available": False},
        {"commodity": "Wheat Flour", "unit": "50kg bag", "price_kes": 2900, "change_pct":  0.0, "available": True},
    ]
}

market = commodity_response["market"]
date   = commodity_response["date"]
print(f"Market: {market}  |  Date: {date}")
print("-" * 55)
print(f"{'Commodity':<15} {'Unit':<12} {'Price (KES)':>12}  {'Change':>8}  Status")
print("-" * 55)

for item in commodity_response["prices"]:
    if not item["available"]:
        status = "OUT OF STOCK"
    elif item["change_pct"] > 0:
        status = "rising"
    elif item["change_pct"] < 0:
        status = "falling"
    else:
        status = "stable"
    change = f"{item['change_pct']:+.1f}%"
    print(f"{item['commodity']:<15} {item['unit']:<12} {item['price_kes']:>12,}  {change:>8}  {status}")