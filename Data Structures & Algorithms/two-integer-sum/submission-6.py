class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needthis = {}
        for i,num in enumerate(nums):
            if (target - num) in needthis:
                return [needthis[target-num], i]
            else:
                needthis[num] = i