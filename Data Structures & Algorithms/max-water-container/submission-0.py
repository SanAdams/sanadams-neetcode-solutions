class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        r = len(heights) - 1
        maxArea = 0

        while left < r:
            maxArea = max(maxArea, min(heights[left], heights[r]) * (r - left))            
            if heights[r] > heights[left]:
                left += 1
            elif heights[left] >= heights[r]:
                r -= 1
    
        return maxArea