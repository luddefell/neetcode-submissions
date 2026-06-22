class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_hash = {}
        result = 0
        prefix_sum_hash[0] = 1
        prefix_sum = []
        for i in range(len(nums)):
            if i == 0:
                prefix_sum.append(nums[0])
            else:
                prefix_sum.append(prefix_sum[i-1] + nums[i])
            if (prefix_sum[i] - k) in prefix_sum_hash:
                result = result + prefix_sum_hash[prefix_sum[i]-k]
            if prefix_sum[i] not in prefix_sum_hash:
                prefix_sum_hash[prefix_sum[i]] = 1
            else:
                prefix_sum_hash[prefix_sum[i]] = prefix_sum_hash[prefix_sum[i]] + 1
        
        return result