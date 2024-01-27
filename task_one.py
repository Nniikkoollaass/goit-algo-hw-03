from datetime import datetime as dtdt

def get_days_from_today(date: str) -> int:
    current_date=dtdt.now().date()
    try:
        parsed_date=dtdt.strptime(date, "%Y-%m-%d").date()
        days=(current_date-parsed_date).days
        return days
    except ValueError:
        print("Please use argument as 'YYYY-mm-dd'")
    except TypeError:
        print("Please use string argument") 
    
print(get_days_from_today("2000-11-03"))
print(get_days_from_today("2033-11-03"))
get_days_from_today("200-11-03")
get_days_from_today(1.25)
get_days_from_today(False)
get_days_from_today(None)