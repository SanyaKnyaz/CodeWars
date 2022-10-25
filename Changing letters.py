#Changing letters
'''
https://www.codewars.com/kata/5831c204a31721e2ae000294
Task
When provided with a String, capitalize all vowels

For example:

Input : "Hello World!"

Output : "HEllO WOrld!"

Note: Y is not a vowel in this kata.
'''

def swap(st):
    vowels = ['a', 'e', 'u', 'i', 'o']
    for ind, item in enumerate(st):
        for i in vowels:
            if item == i:
                st = st.replace(item, st[ind].upper())
    return st
