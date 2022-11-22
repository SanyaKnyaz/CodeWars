'''
A Simple Music Encoder
https://www.codewars.com/kata/58db9545facc51e3db00000a
'''
def compress(raw):
    raw = list(raw)
    result = []
    while raw:
        diff = None
        l = 0
        i = 0
        for i, n in enumerate(raw[1:], 1):
            if diff is None:
                diff = raw[i] - raw[i-1]
                l = 1
            elif diff != raw[i] - raw[i-1]:
                break
            else:
                l += 1
        if i == 0:
            result.append(str(raw.pop(0)))
        elif diff == 0:
            result.append(f'{raw[0]}*{l + 1}')
            raw = raw[l + 1:]
        elif l == 1:
            result.append(str(raw.pop(0)))
        elif l > 1:
            if diff in [-1, 1]:
                result.append(f'{raw[0]}-{raw[l]}')
            else:
                result.append(f'{raw[0]}-{raw[l]}/{abs(diff)}')
            raw = raw[l + 1:]
    
    return ','.join(result)