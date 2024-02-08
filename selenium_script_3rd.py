import datetime

def fetch_today_name():
    today = datetime.date.today()
    day_of_week = today.weekday()
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days_of_week[day_of_week]


