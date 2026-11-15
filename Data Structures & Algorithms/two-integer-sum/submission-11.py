class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, entry in enumerate(nums): 
            if (target-entry) in seen:
                return [seen[target-entry], i]
            else:
                seen[entry] = i
        