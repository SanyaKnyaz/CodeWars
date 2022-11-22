'''
Euler Totient Function
https://www.codewars.com/kata/53c9157c689f841d16000c03
'''
def totient(n):
    if not isinstance(n, int) or n<0:
        return 0
    num = n   
    count = 2
    while count*count <= n :  
        if n%count == 0:
            while n%count == 0: 
                n = n // count 
            num *= 1 - (1 / count) 
        count += 1

    if n > 1: 
        num *= 1 - (1 / n) 
    return int(num)