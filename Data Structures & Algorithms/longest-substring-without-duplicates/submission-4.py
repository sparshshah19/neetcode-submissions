class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0 
        left = 0 
        right = 0
        seen = set()
        count = 0

        while right < len(s):
            while s[right] in seen: 
                count -= 1
                seen.remove(s[left]) 
                left += 1 
            
            
            seen.add(s[right])
            count += 1
            max_count = max(max_count, count)
            right += 1
        
        return max_count
#seen
#count 0 mcount 2


             


