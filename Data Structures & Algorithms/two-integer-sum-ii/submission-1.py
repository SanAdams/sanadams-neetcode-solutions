class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numSet = set(numbers)
        left, right = 0, len(numbers) - 1
        res = []

        while left < right:
            sum = numbers[left] + numbers[right]

            if sum > target:
                right -= 1
            
            if sum < target:
                left += 1

            if sum == target:
                res.append(left + 1)
                res.append(right + 1)
                return res