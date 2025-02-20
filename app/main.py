from datetime import datetime

"""
This function is a very simple approach to calculate the 
the number of days using a delta between two dates and utilizing the
datetime python standard library functions  to calculate the delta.
"""


def count_the_days(dateValue):
    date_format = "%m/%d/%Y"

    year = dateValue.split("/")[2]
    start_of_the_year_date = f"01/01/{year}"
    # convert the two strings to datetime objects
    start_date = datetime.strptime(start_of_the_year_date, date_format)
    end_date = datetime.strptime(dateValue, date_format)

    delta = end_date - start_date
    return delta.days + 1


"""
Alternative to calculating the number of days
uses a dictionary to store the number of days in each month
Note that the list of months is limited to the month specified and since
we use a range function the value of the month is one less than the month specified.
We sum the days for in the stored dictionary and then simply add the day value that 
was passed into the function

"""


def count_the_days_alt(dateValue):
    year = int(dateValue.split("-")[0])
    month = int(dateValue.split("-")[1])
    day = int(dateValue.split("-")[2])

    days: int = 0

    months = list(range(1, month))
    days_in_the_month = [31, is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    combined_months_days = dict((zip(months, days_in_the_month)))
    sum_days = sum(v for v in combined_months_days.values())
    print(combined_months_days)

    days += sum_days + day

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


print(count_the_days_alt("2025-12-28"))
