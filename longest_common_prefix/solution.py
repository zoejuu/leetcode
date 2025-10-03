class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        'https://leetcode.com/problems/longest-common-prefix/description/'
        'Time - 0ms'
        result = ""

        for i in range(len(min(strs, key=len))):
            target = strs[0][i]
            for j in range(1, len(strs)):
                if target != strs[j][i]:
                    return result
            result += target

        return result
    
    def __init__(self):
        print(self.longestCommonPrefix(["flower","flow","floght"]))

Solution()