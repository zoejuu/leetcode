class Solution:
    def romanToInt(self, s: str) -> int:
        'https://leetcode.com/problems/roman-to-integer/description/'
        'Time - 0ms'
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
        prev = 0

        for ch in s:
            val = roman[ch]
            if prev < val:
                # minus
                result += val - (2 * prev)
            else:
                result += val
            prev = val
        
        return result
    
    def __init__(self):
        print(self.romanToInt('MCMXCIV'))
    
Solution()