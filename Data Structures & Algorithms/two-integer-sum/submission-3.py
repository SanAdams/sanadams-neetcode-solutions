class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}
        res = []
        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in idx_map:
                res = [index, idx_map[complement]]
                res.sort()
                return res
            idx_map[nums[index]] = index 
        return res