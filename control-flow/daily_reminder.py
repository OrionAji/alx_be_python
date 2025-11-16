task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        print(f"Reminder: You have a HIGH priority task: {task}")
    case "medium":
        print(f"Reminder: You have a MEDIUM priority task: {task}")
    case "low":
        print(f"Reminder: You have a LOW priority task: {task}")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
if time_bound == "yes":
    print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
else:
    print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")    