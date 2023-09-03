from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    if not users:
        return {}

    weekdays = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }
    today = date.today()
    birthdays_per_week = {day: [] for day in weekdays.values()}

    current_week_start = today - timedelta(days=today.weekday())
    current_week_end = current_week_start + timedelta(days=6)

    next_week_start = current_week_start + timedelta(days=7)
    next_week_end = next_week_start + timedelta(days=6)

    for user in users:
        user_birthday = user["birthday"]

        if today > user_birthday.replace(year=today.year):
            user_birthday = user_birthday.replace(year=today.year + 1)

        if (current_week_start <= user_birthday <= current_week_end) or (
            next_week_start <= user_birthday <= next_week_end
        ):
            day_of_week = user_birthday.strftime("%A")

            if day_of_week in ["Saturday", "Sunday"]:
                day_of_week = "Monday"

            if day_of_week in birthdays_per_week:
                birthdays_per_week[day_of_week].append(user["name"])

    birthdays_per_week = {
        day: names for day, names in birthdays_per_week.items() if names
    }

    return birthdays_per_week


if __name__ == "__main__":
    users1 = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]
    result1 = get_birthdays_per_week(users1)
    print("users1 1:")
    print(result1)

    users2 = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]
    result2 = get_birthdays_per_week(users2)
    print("users2 2:")
    print(result2)

    users3 = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]
    result3 = get_birthdays_per_week(users3)
    print("users3 3:")
    print(result3)

    users4 = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]
    result4 = get_birthdays_per_week(users4)
    print("users4 4:")
    print(result4)

    users5 = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]
    result5 = get_birthdays_per_week(users5)
    print("users5 5:")
    print(result5)
