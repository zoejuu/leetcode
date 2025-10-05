class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        https://leetcode.com/problems/merge-sorted-array/
        Do not return anything, modify nums1 in-place instead.
        Time - 3ms
        """
        while n > 0:
            target = nums2.pop(0)
            for i in range(max(1,m)):
                if target <= nums1[i]:
                    nums1.insert(i, target)
                    m += 1
                    break
                elif i >= m-1:
                    nums1[m] = target
                    m += 1
                    break
            n -= 1
        
        while len(nums1) != m:
            nums1.pop()
        
        print(nums1)
                
    def __init__(self):
        self.merge([0], 0, [1], 1)

Solution()