class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            "}":"{", 
            "]":"[", 
            ")":"("
        }

        for char in s: 
            #if char is open then only we can go, 
            #in stack we are going to be having closed stuff
            
            if char in close_to_open: 
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else: 
                    return False
                
            else: 
                stack.append(char)
            
        if stack: 
            return False
        else: 
            return True