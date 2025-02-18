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


def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
