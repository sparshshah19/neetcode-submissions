class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #longest consecutive sequence of elments htat can be formed
        #eactly one greater
        max_streak = 0 

        duplicate_set = set()
        for num in nums: 
            duplicate_set.add(num)
        
       # 2,3,4,5,10,20
        
        streak = 0 
        for num in duplicate_set: 
            if num - 1 not in duplicate_set: #starts count
               curr = 1
               while num + curr in duplicate_set:
                    curr += 1
               max_streak = max(curr, max_streak)
        
        return max_streak

        #the issue with this is that it may not be sorted the set

            