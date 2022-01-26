from datetime import date, datetime
from difflib import diff_bytes

text = "2021-10-20"
dateType = datetime.strptime(text, "%Y-%m-%d")
nowDate = datetime.now()
diffTime = nowDate - dateType
print(f'Difference Between Two Dates: {diffTime}')

date = datetime.now()
dateStr = datetime.strftime(date, '%A %B %d, %Y')
print(dateStr)
