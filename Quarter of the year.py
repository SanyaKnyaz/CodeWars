#Quarter of the year
'''
https://www.codewars.com/kata/5ce9c1000bab0b001134f5af
Task:
Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter;
and month 11 (November), is part of the fourth quarter.
'''

def quarter_of(month):
    res = 1
    if month == 1 or month == 2 or month == 3:
        res = 1
    if month == 4 or month == 5 or month == 6:
        res = 2
    if month == 7 or month == 8 or month == 9:
        res = 3
    if month == 10 or month == 11 or month == 12:
        res = 4
    return res
