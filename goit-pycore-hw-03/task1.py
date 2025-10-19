from datetime import datetime, date
def get_days_from_today(date_string):
    try:
        input_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    except Exception:
        return None

    today = date.today()
    return (today - input_date).days

test1 = get_days_from_today("2021-02-02")
print(test1)