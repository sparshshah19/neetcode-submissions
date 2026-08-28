class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #during anagram questions you can use hashmaps
        #or sorting 

        if len(t) != len(s): 
            return False 

        #len function in python is o(1)

        count_t, count_s = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        
        return count_t == count_s 
