#Switch/Case - Bug Fixing #6
'''
https://www.codewars.com/kata/55c933c115a8c426ac000082
Task:
Switch/Case - Bug Fixing #6
Oh no! Timmy's evalObject function doesn't work. He uses Switch/Cases to evaluate the given properties of an object,
can you fix timmy's function?
'''

def eval_object(v):
    res = 0
    match v.get('operation'):
        case "+":
            res =  v.get('a') + v.get('b')
        case "-":
            res = v.get('a') - v.get('b')
        case "/":
            res = v.get('a') / v.get('b')
        case "*":
            res = v.get('a') * v.get('b')
        case "%":
            res = v.get('a') % v.get('b')
        case "**":
            res = v.get('a') ** v.get('b')
        case _:
            res = 1
    return res
