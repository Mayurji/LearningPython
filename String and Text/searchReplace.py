import re

# Search and replace
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
text = text.replace('Today', "Tomorrow")
print(f'String Replacement: {text}')

# Change Date Format using re.sub, \3 refers to capture group numbers.
text_1 = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(f'Change In Date Format: {text_1}')

# If repeated Substitution is performed then use precompilation
pattern = re.compile(r'(\d+)/(\d+)/(\d+)')
text_2 = pattern.sub(r'\3-\2-\1', text)
print(f'Precompile & Substitute: {text_2}')

# To get number of substitution made
text_3, n = pattern.subn(r'\3-\2-\1', text)
print(f'No. of replacements made: {n}')