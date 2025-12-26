

def display_current_datetime():
    ## Explore the datetime module to get the current date and time
    from datetime import datetime
    current_date = datetime.now()
    formatted_date = current_date.strftime("%d-%m-%Y %H:%M:%S")
    print("Current date and time:", formatted_date)

def calculate_future_date():
        days_to_add = int(input("Enter number of days: "))
        from datetime import datetime, timedelta
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        formatted_future_date = future_date.strftime("%d-%m-%Y %H:%M:%S")
        print("Future date and time:", formatted_future_date)

display_current_datetime()
calculate_future_date()
