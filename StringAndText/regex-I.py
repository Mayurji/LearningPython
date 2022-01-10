import re

# Date Match
text1='16/09/2022'
text2='16-Nov-2022'

if re.match(r'\d+/\d+/\d+', text1):
    print('Its a date')

if not re.match(r'\d+/\d+/\d+', text2):
    print('Its not a valid date format')

#If lot of matches are done using same pattern, its better to 
# precompile it before into pattern object first.
datePattern = re.compile(r'\d+/\d+/\d+')
if datePattern.match(text1):
    print('cool')

if not datePattern.match(text2):
    print('not cool')

# Finding all occurances of a pattern
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(f'All date in text: {datePattern.findall(text)}')