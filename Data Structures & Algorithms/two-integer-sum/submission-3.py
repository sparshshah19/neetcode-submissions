class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, n in enumerate(nums): 
            needed = target - n
            if needed in num_map: 
                return [num_map[needed], i]
            else: 
                num_map[n] = i

        #0:3 #needed = 4 num_map = 3:0
        #1:4 #needed = 3 
        #2:5 #needed = 2
        #3:6 #needed = 1          