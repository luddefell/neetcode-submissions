class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_left = {}
        for i in range(len(nums)):
            ## if opposite exits
            if (target-nums[i]) in nums_left:
                return [nums_left[target-nums[i]],i]
            ## else 
            nums_left[nums[i]] = i
        

