class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}
        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in idx_map:
                return [idx_map[complement], index]
            idx_map[nums[index]] = index 
        return res