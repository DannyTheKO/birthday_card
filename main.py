import datetime, bday_message

def day_to_ymd(days):
    years = days // 365
    remaining_days = days % 365
    months = remaining_days // 30
    days = remaining_days % 30
    return years, months, days

today = datetime.date.today()

next_birthday = datetime.date(2025, 8, 8)
pervious_birthday = next_birthday - datetime.timedelta(days = 365)

days_away = next_birthday - today
days_away_years, days_away_months, days_away_days = day_to_ymd(days_away.days)

days_before = today - pervious_birthday
days_before_years, days_before_months, days_before_days = day_to_ymd(days_before.days)

if today == next_birthday:
    print(bday_message.random_messages)
else:
    print(f"My next birthday is {days_away.days} days aways and that is ({days_away_months} Months and {days_away_days} Days) left")
    print(f"My previous birthday is {days_before.days} days befores and it been ({days_before_months} Months and {days_before_days} Days)")