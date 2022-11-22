'''
4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def my_sort(nums):
            if len(nums) > 1: 
                mid = len(nums)//2
                left = nums[:mid] 
                right = nums[mid:]
                my_sort(left) 
                my_sort(right) 
                i = j = k = 0
                while i < len(left) and j < len(right): 
                    if left[i] < right[j]: 
                        nums[k] = left[i] 
                        i+=1
                    else: 
                        nums[k] = right[j] 
                        j+=1
                    k+=1
                while i < len(left): 
                    nums[k] = left[i] 
                    i+=1
                    k+=1
                while j < len(right): 
                    nums[k] = right[j] 
                    j+=1
                    k+=1
            return nums
        def median(data):
            mid = len(data) // 2
            return (data[mid] + data[~mid]) / 2
        res = []
        for i in range(len(nums1)):
            res.append(nums1[i])
        for i in range(len(nums2)):
            res.append(nums2[i])
        res = my_sort(res)
        return median(res) 