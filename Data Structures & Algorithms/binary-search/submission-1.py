class Solution:
    def search(self, nums: List[int], target: int) -> int:
         #sorted array 
         #searching for target within nums
         #output is to return the index 

         #binary search question 
         #we want to essentially split the nums in half 

         left = 0 
         right = len(nums) - 1

         while left <= right: 
            middle = (left + right) // 2
            if nums[middle] == target: 
                return middle
            elif nums[middle] > target: 
                right = middle - 1
            else: 
                left = middle + 1
        
         return -1
            