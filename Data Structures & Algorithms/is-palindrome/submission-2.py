class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for char in s: 
            if char.isalnum():
                new_str += char.lower()

        left = 0 
        right = len(new_str) - 1

        while left < right: 
            if new_str[left] == new_str[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
