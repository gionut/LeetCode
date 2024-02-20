class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = 0
        summ = 0
        for num in nums:
            summ += num
            count += 1
        
        gauss = count * (count+1) // 2
        
        return gauss-summ