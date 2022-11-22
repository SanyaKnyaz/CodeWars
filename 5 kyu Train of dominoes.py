'''
Train of dominoes
https://www.codewars.com/kata/5c356d3977bd7254d7191403
'''
def domino_train(n):
    n += 1
    val = 0
    res = [0]
    lst = list(range(n))
    for i in range(n * n - n):
        if lst[val] == val and val: 
            res.append(val)
        res.append(val)
        lst[val] = (lst[val] + 1) %n
        val = lst[val]
    res.append(0)
    return res