class Solution:
    ''' def largestRectangleArea(self, heights: List[int]) -> int:
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
        

        return maxCompositeRectangleArea '''

    # This is the on O(n^2) approach I believe
    # There is a more efficient solution, but we can get back to that later


    # The O(n) solution using a stack

    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        # This will hold tuples of heights and rectangle positions/indexes: (rectanglePos, height)
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
