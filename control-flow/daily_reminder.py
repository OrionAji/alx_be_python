task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        print(f"Reminder set for HIGH priority task: {task}")
    case "medium":
        print(f"Reminder set for MEDIUM priority task: {task}")
    case "low":
        print(f"Reminder set for LOW priority task: {task}")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
if time_bound == "yes":
    print(f"{task} is a high priority task that requires immediate attention today!")
else:
    print(f"{task} is a low priority task. Consider completing it when you have free time.")    