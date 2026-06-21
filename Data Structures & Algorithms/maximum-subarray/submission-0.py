class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray_max = 0
        global_max = nums[0]
        for i in range(len(nums)):
            current_subarray_max = max(nums[i] + current_subarray_max, nums[i])
            if current_subarray_max > global_max:
                global_max = current_subarray_max
        return global_max