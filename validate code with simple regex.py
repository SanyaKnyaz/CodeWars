#validate code with simple regex
'''
https://www.codewars.com/kata/56a25ba95df27b7743000016
Task:
Basic regex tasks. Write a function that takes in a numeric code of any length.
The function should check if the code begins with 1, 2, or 3 and return true if so. Return false otherwise.

You can assume the input will always be a number.
'''

def validate_code(code):
    return True if str(code)[0] == '1' or str(code)[0] == '2' or str(code)[0] == '3' else False
