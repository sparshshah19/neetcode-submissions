from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #basically here we have to group anagrams together 
        anagram_map = defaultdict(list)
        #count the char for each word, how many a, b, t, or whatever letter

        for word in strs: 
           sorted_word = tuple(sorted(word))
           anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
        


       


