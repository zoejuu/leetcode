class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        s_count = Counter(s)
        t_count = Counter(t)
        
        if s_count == t_count:
            return True
        else:
            return False
    
    def __init__(self):
        print(self.isAnagram('hello', 'hello'))

Solution()