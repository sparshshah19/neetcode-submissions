class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #during anagram questions you can use hashmaps
        return sorted(s) == sorted(t)