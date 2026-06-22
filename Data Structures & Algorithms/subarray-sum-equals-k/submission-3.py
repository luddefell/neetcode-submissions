class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_hash = {}
        result = 0
        prefix_sum_hash[0] = 1
        
        for i in range(len(nums)):
            if i == 0:
                prefix_sum = nums[0]
            else:
                prefix_sum = prefix_sum + nums[i]
            if (prefix_sum - k) in prefix_sum_hash:
                result = result + prefix_sum_hash[prefix_sum-k]
            if prefix_sum not in prefix_sum_hash:
                prefix_sum_hash[prefix_sum] = 1
            else:
                prefix_sum_hash[prefix_sum] = prefix_sum_hash[prefix_sum] + 1
        
        return result