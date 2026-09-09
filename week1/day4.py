steps = 15500
sleep_hours = 6
water_glasses = 5
cold_shower = False
pages_read = 15

# For steps: excellent if above 10000, good if above 7500, needs work otherwise. 
if steps >= 10000 :
    print("Excellent!")
elif steps > 7500:
    print("Good!")
else:
    print("Needs work.")

if sleep_hours >= 7:
    print("Good")
else:
    print("Low")

if water_glasses >= 8:
    print("Good")
else:
    print("Below the recommended amount of water intake")

if cold_shower:
    print("Completed")
else:
    print("Skipped")

if pages_read >= 10:
    print("Good")
else:
    print("Low")
# For pages: good if 10 or more, low if below.