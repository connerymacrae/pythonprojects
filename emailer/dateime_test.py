import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
""" returns int corresponding to day of week: Monday = 0, Tuesday = 1, etc"""
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1981, month=8, day=10)

print(date_of_birth)