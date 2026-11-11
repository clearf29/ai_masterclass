def protocol_summary(protocol_list):
    unique = list(set(protocol_list))
    summary = {}
    for p in unique:
        summary[p] = protocol_list.count(p)
    return summary

protocols = ["OMAD", "2MAD", "OMAD", "Autophagy Marathon", "OMAD", "2MAD", "OMAD"]
result = protocol_summary(protocols)

print("Protocol breakdown:")
for protocol, days in result.items():
    print(f"  {protocol}: {days} day(s)")