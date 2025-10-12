class Solution:
    def isHappy(self, n: int) -> bool:
        'https://leetcode.com/problems/happy-number/description/'
        'Time - 0ms'
        seen_set = set()
        
        target = n
        while True:
            temp = target
            target = 0
            for d in str(temp):
                target += int(d) ** 2
                
            if target == 1:
                return True
            if target in seen_set:
                return False
            
            seen_set.add(target)
    
    def __init__(self):
        print(self.isHappy(19))

Solution()