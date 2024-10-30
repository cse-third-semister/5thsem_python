from datetime import datetime, timedelta

def date():
    
    today_date = input("Enter today's date (in format YYYY-MM-DD): ")
    num_days = int(input("Enter the number of days to add: "))

    
    current_date = datetime.strptime(today_date, "%Y-%m-%d")

    
    new_date = current_date + timedelta(days=num_days)

    
    print(f"New date: {new_date.strftime('%Y-%m-%d')}")
    print(f"New day: {new_date.strftime('%A')}")  


date()
