# dates
print('########################## datetime')
from datetime import datetime

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

now = datetime.now()
print_date(now)

year_2024 = datetime(2024, 1, 1) # anio, mes y dia como minimo
print_date(year_2024)


## time
print('########################## time')
from datetime import time

current_time = time(10, 30, 15)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


## date
print('########################## date')
from datetime import date

current_date = date.today()
current_date = date(2022, 10, 23)

print(current_date.year)
print(current_date.month)
print(current_date.day)


## operaciones
print('########################## operations')
# current_date.year = current_date.year + 1 # no es posible modificar asi # se deberia hacer una nueva instancia a date
# print(current_date)

# deben ser del mismo tipo
diff = year_2024 - now
print(diff)
diff = year_2024.date() - current_date
print(diff)


## timedelta
print('########################## timedelta')
from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
# print(end_timedelta * start_timedelta)
print(end_timedelta / start_timedelta)