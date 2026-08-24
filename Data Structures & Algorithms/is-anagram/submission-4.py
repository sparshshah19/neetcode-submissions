class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #using sorting 

       return sorted(s) == sorted(t)