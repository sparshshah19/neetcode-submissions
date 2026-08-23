class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      num_map = {}
      #needed: val 
      #key: val
      #needed (val): index
      #num_map 
      #target = 7, needed = 4
      for i, n in enumerate(nums):
         needed = target - n
         if needed in num_map: 
            return [num_map[needed], i]
         else: 
            num_map[n] = i
         
