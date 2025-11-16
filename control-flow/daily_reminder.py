task = input("Enter your task: ")
priority = input("Enter the priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match (priority.lower(), time_bound.lower()):
    case ("high", "yes"):
        print(f"Reminder: You have a high priority task '{task}' that is time-bound. Please address it immediately!")
    case ("high", "no"):
        print(f"Reminder: You have a high priority task '{task}'. Please prioritize it soon.")
    case ("medium", "yes"):
        print(f"Reminder: You have a medium priority task '{task}' that is time-bound. Don't forget to complete it on time.")
    case ("medium", "no"):
        print(f"Reminder: You have a medium priority task '{task}'. Try to get to it when you can.")
    case ("low", "yes"):
        print(f"Reminder: You have a low priority task '{task}' that is time-bound. Schedule it accordingly.")
    case ("low", "no"):
        print(f"Reminder: You have a low priority task '{task}'. It can be done at your convenience.")
    case _:
        print("Invalid input. Please ensure you enter the correct priority and time-bound status.")
        if time_bound == "yes":
            print(f"Also, remember that your task '{task}' that requires immediate attention today!")
        else:
            print(f"Also, remember your task '{task}' is a low priority task. Consider completing it when you have free time.")