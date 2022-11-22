'''
Running Average
https://www.codewars.com/kata/589e4d646642d144a90000d8
'''
def running_average():
    counter = 0
    res = 0
    def rnd_arg(r_avg):
        nonlocal counter, res
        counter += 1
        res += r_avg
        return round(res / counter, 2)
    return rnd_arg