class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, val in enumerate(nums):
            if val not in hashmap:
                hashmap[val] = i
            if (target - val) in hashmap and hashmap[target-val] != i:
                return [hashmap[target-val], i]
