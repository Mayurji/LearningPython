import re

datePattern = re.compile(r'(\d+)/(\d+)/(\d+)')

#Capture Groups
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
date = '12/12/2022'

dateCaptured = datePattern.match(date)
print(f'groups: {dateCaptured.groups()}')
print(f'group 1: {dateCaptured.group(0)}')
print(f'group 4: {dateCaptured.group(3)}')

for mon, date, year in datePattern.findall(text):
    print('{}-{}-{}'.format(year, mon, date))