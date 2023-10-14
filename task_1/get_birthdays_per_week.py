from collections import defaultdict
from datetime import datetime

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
weekends = ["Saturday", "Sunday"]


def get_birthdays_per_week(users):
    today_date = datetime.today().date()

    grouped_birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today_date.year)

        if birthday_this_year < today_date:
            birthday_this_year = birthday.replace(year=today_date.year + 1)

        delta_days = (birthday_this_year - today_date).days

        if delta_days < 7:
            birthday_weekday = birthday_this_year.strftime("%A")
            if birthday_weekday in weekends:
                grouped_birthdays["Monday"].append(name)
            else:
                grouped_birthdays[birthday_weekday].append(name)

    sorted_keys = sorted(grouped_birthdays.keys(), key=weekdays.index)

    for key in sorted_keys:
        formatted_birthdays = "{:<10}:  {}".format(
            key, ", ".join(grouped_birthdays[key])
        )
        print(formatted_birthdays)
