class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] != target:
            return -1
        middle = len(nums)//2
        print(nums)
        print(middle)
        
        if nums[middle] == target:
            return middle
        if nums[middle] > target:
            return self.search(nums[:middle], target)
        else:
            ans = self.search(nums[middle:],target)
            if ans  == -1:
                return -1
            else:
                return ans + middle
        
