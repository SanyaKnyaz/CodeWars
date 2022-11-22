'''
Basic DeNico
https://www.codewars.com/kata/596f610441372ee0de00006e
'''
def de_nico(key,msg):
    numbers = [sorted(key).index(item) for item in key]
    split_msg = [msg[i:i+len(key)] for i in range(0, len(msg), len(key))]
    decoded_msg = ''
    for item in split_msg:
        for index in numbers:
            if index < len(item):
                decoded_msg += item[index]
    return decoded_msg.rstrip()