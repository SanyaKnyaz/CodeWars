'''
Friday the 13ths
https://www.codewars.com/kata/540954232a3259755d000039
'''
from datetime import date

def friday_the_thirteenths(start, end=None):
    res = []
    if end is None:
        end = start
    for y in range(start, end + 1):
        for m in range(1, 13):
            if date(y, m, 13).isoweekday() == 5:
                res.append(f"{m}/13/{y}")
    return ' '.join(res)