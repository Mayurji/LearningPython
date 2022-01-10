from collections import Counter
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
]

"""
Frequency Counter
-> It can take in any hashable input.
-> Counter is dict object, hence maps key to values.
"""
print(f'Word Frequency: {Counter(words)}')

# Top 3 Words
print(f'Top 3 Words: {Counter(words).most_common(3)}')

count_dict = Counter(words)
print(f"Counter As Dict Object: {count_dict['eyes']}")

# Update Counter
newWords = ['eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under']

oldCounter = Counter(words)
oldCounter.update(newWords)
print(f'Counter updated with new words: {oldCounter}')

#Adding two counters
newCounter = Counter(newWords)
currentCounter = newCounter + oldCounter
print(f'Adding two counter: {currentCounter}')

#Subtracting two counters
newCounter = Counter(newWords)
currentCounter = oldCounter - newCounter
print(f'Subtracting two counter: {currentCounter}')