class Solution:
    def romanToInt(self, s: str) -> int:
        'https://leetcode.com/problems/roman-to-integer/description/'
        'Time - 7ms'
        from collections import Counter
        
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        roman_special = {
            'IV' : 4,
            'IX' : 9,
            'XL' : 40,
            'XC' : 90,
            'CD' : 400,
            'CM' : 900
        }
        result = 0
        for rom_special in roman_special.keys():
            if s.find(rom_special) >= 0:
                result += roman_special[rom_special]
                s = s.replace(rom_special,'')

        target = Counter(s)

        for rom in target.keys():
            result += target[rom] * roman[rom]
        
        return result
    
    def __init__(self):
        print(self.romanToInt('IV'))
    
Solution()