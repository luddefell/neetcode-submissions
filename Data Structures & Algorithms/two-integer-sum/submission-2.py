class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        for i in range(len(nums)):
            for j in range(len(nums)):
                i_val = nums[i]
                j_val = nums[j]
                if i != j:
                    if ((i_val + j_val) == target):
                       return_val = []
                       return_val.append(i)
                       return_val.append(j)
                       return return_val