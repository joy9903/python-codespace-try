'''
creat a funciton named business_days that takes a start date, 
an end date, and a list of holidays, and returns the number of 
business days between the start and end dates, inclusive. 
A business day is any day that is not a weekend or a holiday. 
The function should return an integer.

'''

import holidays as hd
from datetime import datetime, timedelta
import numpy as np


def business_days(start_date: datetime, end_date: datetime  , holidays: list|None = []) -> int:
    business_days = 0
    holidays = [datetime.strptime(holiday, '%Y-%m-%d') for holiday in holidays]
    for day in np.arange(start_date, end_date + timedelta(days=1), timedelta(days=1)):
        if day  not in holidays or  day.weekday() <5:
            business_days += 1
    return business_days


def count_business_days(start_date: str, end_date: str) -> int:
    start_date_object = datetime.strptime(start_date, '%m-%d-%Y').date()
    end_date_object = datetime.strptime(end_date, '%m-%d-%Y').date()
    holidays = hd.US()
    count_business_days = business_days(start_date_object, end_date_object, holidays=holidays)
    return count_business_days

if __name__=="__main__":
    start_date = '12-01-2022'
    end_date = '12-31-2023'
    value = count_business_days(start_date, end_date)
    print(f'Number of business days between {start_date} and {end_date} is {value}')