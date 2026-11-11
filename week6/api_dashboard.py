#preview of the three end_points
def fetch_members():
    return [
        {"name": "James Omondi",  "steps": 9200,  "protocol": "OMAD", "sleep": 7.5, "cold_shower": True},
        {"name": "Sandra Weru",   "steps": 10500, "protocol": "2MAD", "sleep": 8.0, "cold_shower": True},
        {"name": "Patrick Njiru", "steps": 8100,  "protocol": "OMAD", "sleep": 6.5, "cold_shower": False},
        {"name": "Grace Achieng", "steps": 11000, "protocol": "OMAD", "sleep": 7.0, "cold_shower": True},
        {"name": "Brian Kamau",   "steps": 7400,  "protocol": "2MAD", "sleep": 9.0, "cold_shower": True},
        {"name": "Kevin Mwangi",  "steps": 10800, "protocol": "OMAD", "sleep": 7.5, "cold_shower": True},
    ]

def fetch_weekly_summary():
    return {
        "week": "2024-W47",
        "daily_totals": [54200, 62000, 58400, 71000, 49600, 68000, 65200],
        "days": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "member_count": 6
    }

def fetch_active_skills():
    return {
        "week": "2024-W47",
        "skills": [
            {"name": "welding",       "instructor": "Patrick Njiru", "enrolled": 8},
            {"name": "tiling",        "instructor": "James Omondi",  "enrolled": 12},
            {"name": "copywriting",   "instructor": "Sandra Weru",   "enrolled": 15},
            {"name": "phone repair",  "instructor": "Kevin Mwangi",  "enrolled": 10},
            {"name": "beekeeping",    "instructor": "Grace Achieng", "enrolled": 6},
        ]
    }

# Preview
members = fetch_members()
weekly = fetch_weekly_summary()
skills = fetch_active_skills()

print(f"Members endpoint: {len(members)} records")
print(f"Weekly endpoint:  {len(weekly['daily_totals'])} days of data")
print(f"Skills endpoint:  {len(skills['skills'])} active skills")
#process_each_endpoint
def process_members(members, step_goal=10000):
    goal_met = [m for m in members if m["steps"] >= step_goal]
    avg_steps = round(sum(m["steps"] for m in members) / len(members))
    shower_count = sum(1 for m in members if m["cold_shower"])
    protocols = {}
    for m in members:
        p = m["protocol"]
        protocols[p] = protocols.get(p, 0) + 1
    return {
        "total": len(members),
        "goal_met": len(goal_met),
        "avg_steps": avg_steps,
        "cold_showers": shower_count,
        "protocols": protocols,
        "top": max(members, key=lambda m: m["steps"])["name"]
    }

def process_weekly(weekly):
    totals = weekly["daily_totals"]
    days = weekly["days"]
    best_idx = totals.index(max(totals))
    return {
        "best_day": days[best_idx],
        "best_total": max(totals),
        "weekly_avg": round(sum(totals) / len(totals)),
        "total_steps": sum(totals)
    }

def process_skills(skills_data):
    skills = skills_data["skills"]
    total_enrolled = sum(s["enrolled"] for s in skills)
    most_popular = max(skills, key=lambda s: s["enrolled"])
    return {
        "active_count": len(skills),
        "total_enrolled": total_enrolled,
        "most_popular": most_popular["name"],
        "top_enrollment": most_popular["enrolled"]
    }

# Run all three
raw_members = [
    {"name": "James Omondi",  "steps": 9200,  "protocol": "OMAD", "sleep": 7.5, "cold_shower": True},
    {"name": "Sandra Weru",   "steps": 10500, "protocol": "2MAD", "sleep": 8.0, "cold_shower": True},
    {"name": "Patrick Njiru", "steps": 8100,  "protocol": "OMAD", "sleep": 6.5, "cold_shower": False},
    {"name": "Grace Achieng", "steps": 11000, "protocol": "OMAD", "sleep": 7.0, "cold_shower": True},
    {"name": "Brian Kamau",   "steps": 7400,  "protocol": "2MAD", "sleep": 9.0, "cold_shower": True},
    {"name": "Kevin Mwangi",  "steps": 10800, "protocol": "OMAD", "sleep": 7.5, "cold_shower": True},
]
raw_weekly = {"week": "2024-W47", "daily_totals": [54200, 62000, 58400, 71000, 49600, 68000, 65200], "days": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"], "member_count": 6}
raw_skills = {"week": "2024-W47", "skills": [{"name": "welding","instructor": "Patrick Njiru","enrolled": 8},{"name": "tiling","instructor": "James Omondi","enrolled": 12},{"name": "copywriting","instructor": "Sandra Weru","enrolled": 15},{"name": "phone repair","instructor": "Kevin Mwangi","enrolled": 10},{"name": "beekeeping","instructor": "Grace Achieng","enrolled": 6}]}

member_stats = process_members(raw_members)
weekly_stats = process_weekly(raw_weekly)
skill_stats = process_skills(raw_skills)

print("Member stats:", member_stats)
print("Weekly stats:", weekly_stats)
print("Skill stats: ", skill_stats)