class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                print(f"This is what i + j = {nums[i] + nums[j]} \n Also i, j {i, j}")
                if((nums[i] + nums[j]) == target):
                    if(i == j):
                        continue
                    print("Yes we is target")
                    res.append(i)
                    res.append(j)
                    return res
        