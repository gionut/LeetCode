class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        extendedNums = [-math.inf] + nums + [-math.inf]
        left = 1
        right = len(nums)
        return self.findPeak(extendedNums, left, right)
    
    def findPeak(self, nums, left, right):
        pivot = (left + right)//2
        
        lhs = pivot-1 
        rhs = pivot+1
        if nums[lhs] < nums[pivot] and nums[pivot] > nums[rhs]:
            return pivot-1
        if nums[rhs] > nums[lhs]:
            return self.findPeak(nums, pivot+1, right)
        else:
            return self.findPeak(nums, left, pivot-1)
        