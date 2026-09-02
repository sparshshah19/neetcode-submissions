class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #for the longest substring without duplicates
        left = 0 
        right = 0
        max_count = 0 

        seen = set()

        while right < len(s):
            while s[right] in seen: 
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            max_count = max(right - left + 1, max_count)
            right += 1 

        return max_count