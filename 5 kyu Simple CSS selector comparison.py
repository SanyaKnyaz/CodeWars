'''
Simple CSS selector comparison
https://www.codewars.com/kata/5379fdfad08fab63c6000a63
'''
def tokenise(s, split='*#. '):
    buffer = ''
    for c in s:
        if c in split:
            if buffer.strip():
                yield buffer.strip()
                buffer = ''
        buffer += c
    if buffer.strip():
        yield buffer.strip()

def score_selector(selector):
    low, ids, classes, tags = 0, 0, 0, 0
    for part in tokenise(selector):
        if part.startswith('.'):
            classes -= 1
        elif part.startswith('#'):
            ids -= 1
        elif part.startswith('*'):
            low += 1
        else:
            tags -= 1
        
    return low, ids, classes, tags

def compare(a, b):
    return sorted([(score_selector(s), -i, s) for i, s in enumerate([a, b])])[0][-1]