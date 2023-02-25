"""coding: utf-8 """
import time
from calendar import isleap

def judge_leap_year(year1):
    """Judge Leap year"""
    return bool(isleap(year1))

def month_days(month1, leap_year1):
    """This module returns the number of days corresponding to the month"""
    if month1 in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month1 in [4, 6, 9, 11]:
        return 30
    if month1 == 2 and leap_year1:
        return 29
    if month1 == 2 and (not leap_year1):
        return 28
    return -1

name = input("input your name: ")
age = input("input your age: ")
localtime = time.localtime(time.time())

year = int(age)
month = year * 12 + localtime.tm_mon
DAY = 0

begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

# calculate the days
for y in range(begin_year, end_year):
    if judge_leap_year(y):
        DAY = DAY + 366
    else:
        DAY = DAY + 365

leap_year = judge_leap_year(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    DAY = DAY + month_days(m, leap_year)

DAY = DAY + localtime.tm_mday
print(f"{name}'s age is {year} years or {month} months or {DAY} days")
