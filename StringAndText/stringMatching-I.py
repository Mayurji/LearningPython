import re

string = "AAPL, 89; 890, SELL"

fields = re.split(r'[;,\s]\s*', string)
print(f"Split On Multiple Delimiter: {fields}")

#capture group
fields = re.split(r'(;|,|\s)\s*', string)
print(f'Including Delimiter: {fields}')

#noncapture group
fields = re.split(r'(?:;|,|\s)\s*', string)
print(f'Excluding Delimiter: {fields}')

#Matching with start and end of a string
filename = "model_1.py"
if filename.endswith('.py'):
    print("It is python file")

if filename.startswith('model'):
    print("It is model file")

filename = "model_1.js"
if filename.endswith(('.py', '.js')):
    print("It is Coding file")

# Using Regex
# url = "http://www.python.org"
# re.match('http:|https:|ftp:', url)
