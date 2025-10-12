class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        https://leetcode.com/problems/merge-sorted-array/
        Do not return anything, modify nums1 in-place instead.
        Time - 0ms
        """
        i = m - 1
        j = n - 1
        k = m + n - 1 # Target length - 1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
       

                
    def __init__(self):
        self.merge([0,1,2,3,0,0,0,0,0,0], 4, [1,4,5,5,6,6], 6)

Solution()