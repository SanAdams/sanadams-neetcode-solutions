class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, firstNumber in enumerate(nums):
            # Skip trying positive numbers as the first number
            if firstNumber > 0:
                break

            if index > 0 and firstNumber == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                threeSum = firstNumber + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1

                if threeSum < 0:
                    left += 1

                if threeSum == 0:
                    res.append([firstNumber, nums[left], nums[right]])
                    left += 1
                    right -= 1
                
                    # Skip the numbers we've already tried as the second number and
                    # make sure the left pointer doesn't keep infinitely incrementing or go
                    # out of bounds
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res

        