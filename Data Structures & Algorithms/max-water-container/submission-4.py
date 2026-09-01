class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0 
        left = 0 
        right = len(heights) - 1

        #we alr have max width 
        #as right moves left so -= 1, height must be getting higher otherwise its min
        while left < right: 
            curr_area = min(heights[left], heights[right]) * (right - left)
            max_area = max(curr_area, max_area)
            if heights[left] <= heights[right]:
                left += 1
            else: 
                right -= 1

        return max_area