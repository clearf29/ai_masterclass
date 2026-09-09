# Store your values
exercises = 6
sets_per_excercise = 4
total_sets = exercises * sets_per_excercise 
reps_per_set = 10
#calculate total reps and total volume
total_reps = reps_per_set * total_sets 
average_weight_per_set = 60
total_volume = average_weight_per_set * total_reps 

session_duration =45
#calculate reps per minute
reps_per_minute = total_reps/session_duration
target = 10000
int(target)


print(f"Total Vol: {total_volume}", "kg")
print(f"Total Reps: {total_reps}",  "reps")
print(f"Reps per Minute: {reps_per_minute}", "minutes")
print("Volume Exceeded:", total_volume > target)

