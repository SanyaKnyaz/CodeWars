'''
Right Truncatable Harshad numbers
https://www.codewars.com/kata/5c824b7b9775761ada934500/
'''
def harshad(n_digits):
    arr = [[i for i in range(1,10)]]
    for t in range(n_digits): 
        x = []
        for num in arr[-1]:
            for n in '1234567890':
                if int(str(num) + n) % sum([int(d) for d in str(num)] + [int(n)]) == 0:
                    x.append(int(str(num) + n))
        arr.append(sorted(x))
    return arr[1:]

arr=harshad(15)

def rthn_between(a, b):
    r = []
    stop = False
    for i in range(len(arr)):
        if arr[i][-1] >= a:
            for j in range(len(arr[i])):
                if arr[i][j] > b:
                    stop = True 
                    break
                if arr[i][j] >= a:
                    r.append(arr[i][j])
            if stop == True:
                break
    return r