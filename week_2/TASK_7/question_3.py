# Identifying the Users inputs
days = ("Monday", "Tuesday", "Friday")
activities =[]
for day in days:
    activity = input(f"Enter an activity for {day}:")
    activities.append(activity)
    schedule ={day: activity for day, activity in zip(days, activities)}

    print("\n---Days & Activities ---")
    print(schedule)