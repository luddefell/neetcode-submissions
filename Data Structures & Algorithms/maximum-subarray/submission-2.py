class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        maxx = nums[0]
        for i in range(len(nums)):
            if i != 0:
                curr = max(nums[i], curr + nums[i])
                maxx = max(curr, maxx)
        return maxx
