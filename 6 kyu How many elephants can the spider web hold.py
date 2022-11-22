'''
How many elephants can the spider web hold?
https://www.codewars.com/kata/5830e55fa317216de000001b
'''
def breakTheWeb (strength, width):
    total = 0
    res = 0
    for item in range(width, 0, -1):
        for i in range(item):
            total += (width - item + 1) * 1000
            if total > strength: 
                return res
            res+=1
    return res