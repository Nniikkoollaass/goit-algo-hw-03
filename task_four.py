import datetime as dt
from datetime import datetime as dtdt

users = [
    {"name": "Hugh Foll", "birthday": "1965.02.02"},
    {"name": "Jane Gagu", "birthday": "1999.01.27"},
    {"name": "Samantha Brick", "birthday": "1989.01.28"},
    {"name": "Bill Smith", "birthday": "1975.01.29"}
]

def get_upcoming_birthdays(users=None):
    today_date=dtdt.today().date()
    upcoming_birthdays=[]
    for user in users:
        birthday_date=user["birthday"]
        birthday_date=str(today_date.year)+birthday_date[4:]
        birthday_date=dtdt.strptime(birthday_date, "%Y.%m.%d").date()
        day_of_week=birthday_date.isoweekday()
        days_difference=(birthday_date-today_date).days
        if 0<=days_difference<7:
            if day_of_week<6:
                upcoming_birthdays.append({'name':user['name'], 'congratulation_date':birthday_date.strftime("%Y.%m.%d")}) 
            else:
                if (birthday_date+dt.timedelta(days=1)).weekday()==0:
                    upcoming_birthdays.append({'name':user['name'], 'congratulation_date':(birthday_date+dt.timedelta(days=1)).strftime("%Y.%m.%d")})
                elif (birthday_date+dt.timedelta(days=2)).weekday()==0:
                    upcoming_birthdays.append({'name':user['name'], 'congratulation_date':(birthday_date+dt.timedelta(days=2)).strftime("%Y.%m.%d")})
    return upcoming_birthdays

print(get_upcoming_birthdays(users))