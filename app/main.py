from datetime import datetime


def count_the_days(dateValue):
    date_format = "%m/%d/%Y"

    year = dateValue.split("/")[2]
    start_of_the_year_date = f"01/01/{year}"
    # convert the two strings to datetime objects
    start_date = datetime.strptime(start_of_the_year_date, date_format)
    end_date = datetime.strptime(dateValue, date_format)

    delta = end_date - start_date
    return delta.days + 1


def count_the_days_alt(dateValue):
    year = int(dateValue.split("-")[0])
    month = int(dateValue.split("-")[1])
    day = int(dateValue.split("-")[2])
    days: int = 0

    months = list(range(1, 13))
    days_in_the_month = [31, is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    combined_months_days = list(zip(months, days_in_the_month))

    return days


def is_leap_year(year: int) -> int:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 29
            else:
                return 28
        else:
            return 29
    else:
        return 28
