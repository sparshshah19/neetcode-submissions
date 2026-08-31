class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force 
       # max_area = 0
       # curr_area = 0 

        #for i in range(len(heights)):
         #   for j in range(i + 1, len(heights)):
         #       curr_area = min(heights[i], heights[j]) * (j - i)
         #       max_area = max(curr_area, max_area)

        #return max_area

        max_area = 0 
        curr_area = 0 

        #two pointers algo 
        
        left = 0 
        right = len(heights) - 1

        while left < right: 
            curr_area = min(heights[left], heights[right]) * (right - left)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
            max_area = max(curr_area, max_area)
        return max_area
        




























































