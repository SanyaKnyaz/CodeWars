'''
WordSquare
https://www.codewars.com/kata/578e07d590f2bb8d3300001d
'''
from collections import Counter
def word_square(letters):
    n = int(len(letters) ** 0.5)
    if n*n != len(letters):
        return False
    else:
        return sum(x % 2 for x in Counter(letters).values()) <= n