class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hist = {}
        for i in range(len(nums)):
            if (target - nums[i]) in hist:
                return [hist[(target - nums[i])], i]
            else:
                hist[nums[i]] = i
        
