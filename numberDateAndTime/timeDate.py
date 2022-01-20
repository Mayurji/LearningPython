from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta

a = timedelta(days=3, hours=5)
b = timedelta(hours=4)
c = a + b

print(f"Hours excluding days, c's Hours: {c.seconds / 3600}")
print(f"Total No. of c's Hours: {c.total_seconds() / 3600}")

#Adding n Days to Date
a = datetime(2022, 9, 23)
add_ten_days = a + timedelta(days=10)
print(f'After 10 Days addition: {add_ten_days}')

#Difference Between Two Dates
b = datetime(2022, 10, 23)
diff_days = b - a 
print(f'Difference between Two Dates: {diff_days}')

# Today's Date
print(f"Today's Date: {datetime.today()}")
print(f"Today's Date plus 10 min: {datetime.today()+timedelta(minutes=10)}")

print(f'Moving the date by months: {a + relativedelta(months=+5)}')