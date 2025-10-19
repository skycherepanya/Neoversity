from datetime import datetime, date, timedelta
def get_upcoming_birthdays(users):
    today = date.today()
    period = today + timedelta(days = 7) 
    result = []
   
    for user in users: 

        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        this_year = birthday.replace(year=today.year)

        if this_year < today:
            this_year = birthday.replace(year=today.year + 1)
        
        if today <= this_year <= period:
            if this_year.weekday() == 5:
                this_year = this_year + timedelta(days=2)
            elif this_year.weekday == 6:
                this_year = this_year + timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": this_year.strftime("%Y.%m.%d")
            })


            return result

users = [
    {"name": "John Doe", "birthday": "1985.10.22"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)