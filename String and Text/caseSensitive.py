import re

text = "It is UPPER CASE. It is lower case."
cases = re.findall('case', text, flags=re.IGNORECASE)
print(f'Cases: {cases}')

case_to_deck = re.sub('case', 'deck', text, flags=re.IGNORECASE)
print(f'Case To Deck: {case_to_deck}')

# Find text inside double quotes
# * does greedy match and ? makes non-greedy match
text_1 = 'Computer says "no."'
str_pat = re.compile(r'\"(.*)\"')
print(f"Double Quoted Text: {str_pat.findall(text_1)}")

text_2 = 'Computer says "no." and phone says "yes."'
print(f"Incorrect text captured: {str_pat.findall(text_2)}")

str_pat = re.compile(r'\"(.*?)\"')
print(f"Double Quoted Text: {str_pat.findall(text_2)}")

# Multi-line pattern
text_1 = '/* this is a comment */'
text_2 = """/* this is 
multi-line comment */
"""
commentPattern = re.compile(r'/\*(.*?)\*/')
print(f'Comment: {commentPattern.findall(text_1)}')
print(f'Failed in multi-line Comment: {commentPattern.findall(text_2)}')

multilineCommentPattern = re.compile(r'/\*((?:.|\n)*?)\*/')
print(f'Multi-line Comment: {multilineCommentPattern.findall(text_2)}')

# Alternative way to handle multiline comment
multilineCommentPattern = re.compile(r'/\*(.*?)\*/', flags=re.DOTALL)
print(f're.DOTALL : {multilineCommentPattern.findall(text_2)}')