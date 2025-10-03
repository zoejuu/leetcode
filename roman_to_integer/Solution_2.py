class Solution:
    def romanToInt(self, s: str) -> int:
        'https://leetcode.com/problems/roman-to-integer/description/'
        'Time - 6-8 ms'
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        result = 0

        n = len(s)
        for i, char in enumerate(s):
            if i+1 < n and roman[char] < roman[s[i+1]]:
                result -= roman[char]
            else:
                result += roman[char]
        
        return result
    
    def __init__(self):
        print(self.romanToInt('MCMXCIV'))
    
Solution()