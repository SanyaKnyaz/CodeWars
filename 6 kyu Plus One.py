'''
66. Plus One
https://leetcode.com/problems/plus-one/
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return digits
        index = len(digits)-1
        while index >= 0:
            if index == 0:
                if digits[index] == 9:
                    digits[index] = 0
                    return [1] + digits
                else:
                    digits[index] += 1
                    return digits
            if digits[index] == 9:
                    digits[index] = 0
                    index -= 1
            elif digits[index] != 9:
                digits[index] += 1
                return digits