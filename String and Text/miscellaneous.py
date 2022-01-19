import html
from html.parser import HTMLParser
import re
from collections import namedtuple

text = 'Text has html tag "<tag>text<tag>".'
print(f'Escaping < and > symbol: {html.escape(text)}')
print(f'Escaping <, >, quotes: {html.escape(text, quote=False)}')

# To encode non-ascii characters
s = 'Spicy Jalapeño'
encoded_s = s.encode("ascii", errors='xmlcharrefreplace')
print(f"Encoded Non-ASCII characters: {encoded_s}")

# Checkout HTMLParser(), XML.SAX

# Tokenization
text = 'foo = 23 + 42 * 10'

# Text into column represent as follows
# tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
# ('NUM', '42'), ('TIMES', '*'), ('NUM', 10')]

#?P<TOKENNAME> used for assigning name to pattern
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pattern = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
scanner = master_pattern.scanner('foo = 42')
#print(scanner.match().group())

token = namedtuple('Token', ['type', 'value'])
def generate_token(pattern, text):
    scanner = pattern.scanner(text)
    for m in iter(scanner.match, None):
        yield token(m.lastgroup, m.group())

for tok in generate_token(master_pattern, 'foo = 42'):
    print(tok)

# Order of the pattern "Matters"

LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'
master_pattern_1 = re.compile("|".join(LE|LT|EQ)) #Correct
master_pattern_2 = re.compile("|".join(LT|LE|EQ)) #Incorrect

"""
master_pattern_2 is incorrect, because it will match the text
<= as LT (less than) followed by EQ.
"""