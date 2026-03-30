import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        minRate = right

        # Binary search the solution space
        while left <= right:
            currentRate = (left + right) // 2

            hoursTaken = 0
            for pile in piles:
                hoursTaken += math.ceil(float(pile / currentRate))
            
            if (hoursTaken <= h):
                minRate = currentRate
                right = currentRate - 1
            else:
                left = currentRate + 1


        return minRate