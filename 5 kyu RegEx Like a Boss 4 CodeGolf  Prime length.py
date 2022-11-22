'''
RegEx Like a Boss #4 CodeGolf : Prime length
https://www.codewars.com/kata/5c2cea87b0aea22f8181757c
'''
import re, math

compile = re.compile

class DummyPattern():
    def init(self, pattern, *_):
        self.pattern = compile(pattern)

    def match(self, s):
        m = self.pattern.match(s)
        if m and self.is_prime(len(s)):
            return m

    @staticmethod
    def is_prime(num):
        if num == 2:
            return True
        if num < 2 or num % 2 == 0:
            return False
        n = 3
        sqrt = math.sqrt(num)
        while n <= sqrt:
            if num % n == 0:
                return False
            n += 2
        return True


REGEX = r'(?!(xx+)\1+$)\S[x]+$'