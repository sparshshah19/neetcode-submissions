class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        
        for i in range(len(strs[0])): #going through the chars of first word
            for s in strs: #going through all the words
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result
        
        

                
