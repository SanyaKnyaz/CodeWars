#Beginner - Lost Without a Map
'''
https://www.codewars.com/kata/57f781872e3d8ca2a000007e
Task:
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
'''

def maps(a):
    res = []
    for item in range(len(a)):
        res.append(a[item]*2)
    return res
