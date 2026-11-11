contacts = [
    {"name": "James Omondi",  "phone": "0712345678", "skill": "welding",      "city": "Nairobi"},
    {"name": "Sandra Weru",   "phone": "0723456789", "skill": "tiling",       "city": "Mombasa"},
    {"name": "Patrick Njiru", "phone": "0734567890", "skill": "phone repair", "city": "Nairobi"},
    {"name": "Grace Achieng", "phone": "0745678901", "skill": "copywriting",  "city": "Kisumu"},
    {"name": "Brian Kamau",   "phone": "0756789012", "skill": "upholstery",   "city": "Nairobi"},
]

# Add one more contact
contacts.append({
    "name": "Kevin Mwangi",
    "phone": "0767890123",
    "skill": "beekeeping",
    "city": "Nakuru"
})

# Display all contacts
print("===== CONTACT BOOK =====")
for i, contact in enumerate(contacts):
    print(f"\n{i+1}. {contact['name']}")
    print(f"   Phone : {contact['phone']}")
    print(f"   Skill : {contact['skill']}")
    print(f"   City  : {contact['city']}")

# Search by city
print("\n===== NAIROBI CONTACTS =====")
for contact in contacts:
    if contact["city"] == "Nairobi":
        print(f"  {contact['name']} | {contact['skill']}")

# Summary
print(f"\nTotal contacts: {len(contacts)}")