class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSequence = 0

        for n in numSet:
            length = 1
            while(n + length) in numSet:
                length += 1
            longestSequence = max(length, longestSequence)

        return longestSequence