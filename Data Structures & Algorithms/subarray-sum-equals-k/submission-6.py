class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        output = 0
        hashmap[0] = 1
        prefixSum = 0
        for i in nums:
            prefixSum = prefixSum + i
            if (prefixSum-k) in hashmap:
                output += hashmap[prefixSum-k]
            hashmap[prefixSum] += 1
        return output

