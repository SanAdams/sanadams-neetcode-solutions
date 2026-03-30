class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxCompositeRectangleArea = heights[0]

        for i in range(len(heights)):
            width = 1
            left, right = i - 1, i + 1
            compositeHeight = heights[i]
            
            # Look to the left
            while left >= 0:
                if heights[left] < compositeHeight:
                   break
                
                width += 1
                left -= 1

            # Look to the right
            while right < len(heights):
                if heights[right] < compositeHeight:
                    break

                width += 1
                right += 1

            currentCompositeArea = compositeHeight * width
            maxCompositeRectangleArea = max(currentCompositeArea, maxCompositeRectangleArea)
        

        return maxCompositeRectangleArea

    # This is the on O(n^2) approach I believe
    # There is a more efficient solution, but we can get back to that later