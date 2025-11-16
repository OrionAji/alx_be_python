task = input("Enter your task: ")
priority = input("Enter the priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority.lower():
    case "high":
        print(f"Reminder set for HIGH priority task: {task}. Please complete it as soon as possible.")
    case "medium":
        print(f"Reminder set for MEDIUM priority task: {task}. Try to complete it in due time.")
    case "low":
        print(f"Reminder set for LOW priority task: {task}. You can complete it at your convenience.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
if time_bound.lower() == "yes":
    print(f"{task} is a high priority task that requires immediate attention today!")
else:
    print(f"{task} is a low priority task. Consider completing it when you have free time.")