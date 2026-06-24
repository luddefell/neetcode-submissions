class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = nums[0]
        prefixSum_hash = defaultdict(int)
        output = 0
        prefixSum_hash[0] = 1
        if (prefixSum-k) in prefixSum_hash:
                output += prefixSum_hash[prefixSum-k]
        prefixSum_hash[nums[0]] += 1
        for r in range(len(nums)):
            if r != 0:
                prefixSum += nums[r]
                if (prefixSum-k) in prefixSum_hash:
                    output += prefixSum_hash[prefixSum-k]
                prefixSum_hash[prefixSum] += 1
        return output
            