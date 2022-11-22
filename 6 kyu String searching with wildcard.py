'''
String searching with wildcard
https://www.codewars.com/kata/546c7f89bed2e12fb300056f
'''
def find(needle, haystack):
    for i in range(len(haystack)-len(needle)+1):
        a = True
        for j, item in enumerate(needle):
            if item == "_":
                continue
            elif item != haystack[i+j]:
                a = False
                break
        if a:
            return i
    return -1