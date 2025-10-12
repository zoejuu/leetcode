def isPalindrome(s: str) -> bool:
    from collections import deque
    dq = deque(s)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

class Solution:
    def longestPalindrome(self, s: str) -> str:
        from collections import Counter

        # edge case
        if len(s) < 1:
            return ""

        longest = s[:1]
        char_counter = Counter(s)

        for char in char_counter.keys():
            if char_counter[char] >= 2:
                indices = [i for i,c in enumerate(s) if c==char]
                for i in indices:
                    for j in reversed(indices):
                        if j <= i:
                            continue
                        if (j - i + 1) <= len(longest):
                            break
                        
                        target = s[i:j+1]
                        if isPalindrome(target) and (len(target) > len(longest)):
                            longest = target
                            break
        
        return longest