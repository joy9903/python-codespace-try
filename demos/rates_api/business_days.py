# looked up the Python docs for the datetime module
from datetime import date, timedelta
from typing import Generator

import holidays


def business_days(start: date, end: date) -> Generator[date, None, None]:
    us_holidays = holidays.country_holidays("US")
    date_diff = end - start
    for day in range(date_diff.days + 1):
        the_date = start + timedelta(day)
        if (the_date.weekday() < 5) and (the_date not in us_holidays):
            yield the_date


if __name__ == "__main__":
    for business_day in business_days(date(2024, 5, 1), date(2024, 5, 6)):
        print(business_day)


### List Solution

# # Python Docs and Googling for the List generic type
# def business_days(start: date, end: date) -> list[date]:
#     # review the PyPi docs for the holidays package
#     us_holidays = holidays.country_holidays("US")

#     # Pythonic
#     date_diff = end - start

#     business_days_list = []
#     # Pythonic and Type Hint-enabled Code Completion
#     for day in range(date_diff.days + 1):
#         # review the Python docs
#         the_date = start + timedelta(day)
#         # review the Python docs and PyPi package docs
#         if (the_date.weekday() < 5) and (the_date not in us_holidays):
#             business_days_list.append(the_date)

#     return business_days_list