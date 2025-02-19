from app.main import is_leap_year, count_the_days, count_the_days_alt


def test_is_leap_year():
    assert is_leap_year(2019) == 28
    assert is_leap_year(2026) == 28
    assert is_leap_year(2028) == 29
    assert is_leap_year(2100) == 28
    assert is_leap_year(2400) == 29
    assert is_leap_year(2024) == 29


def test_count_the_days():
    assert count_the_days("02/20/2022") == 51
    assert count_the_days("03/16/2028") == 76  # 31+29+16 = 76
    assert count_the_days("12/30/2400") == 365
    assert count_the_days("03/16/2026") == 75  # 31+28+16 = 75
    assert count_the_days("01/16/2019") == 16


"""
Leap Years are any year that can be exactly divided by 4 (such as 2020, 2024, 2028, etc)
not	except if it can be exactly divided by 100, then it isn't (such as 2100, 2200, etc)
yes	except if it can be exactly divided by 400, then it is (such as 2000, 2400)
    
"""


def test_count_the_days_alt():
    assert count_the_days_alt("2022-02-20") == 51  # 31+20
    assert count_the_days_alt("2028-03-16") == 76  # 31+28+16 = 76
    assert count_the_days_alt("2019-01-16") == 16  # 16
    assert count_the_days_alt("2400-12-30") == 365
    assert count_the_days_alt("2026-03-16") == 75  # 31+28+16 = 75


# dateValue = "2026-03-16"  # leap year test date - Expected value is 31+29+16 = 76
# dateValue = "2019-01-16" # non leap year year/100 = Expected value is 16
# dateValue = "2400-12-30" # leap year divided by 400 = 0 Expected value is 31+29+31+30+31+30+31+31+30+31+30+30 = 365
