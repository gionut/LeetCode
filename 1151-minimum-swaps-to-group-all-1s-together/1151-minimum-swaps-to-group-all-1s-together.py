# 1,0,1,0,1,0,0,1,1,0,1
#           -----------
# [1,1,0,0,1,1,0,0,1,1],0,1,1,0,1]
# -----------------
# gaps -> gaps*2
# consecutive -> all remaining ones
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        end = 0
        for i in data:
            if i == 1:
                end += 1
        
        crt_window = 0
        for i in range(end):
            if data[i] == 0:
                crt_window += 1

        min_zeros = crt_window
        start = 1
        while end < len(data):
            if data[start-1] == 1 and data[end] == 0:
                crt_window += 1 
            if data[start-1] == 0 and data[end] == 1:
                crt_window -= 1 
                
            min_zeros = min(min_zeros, crt_window)
            start += 1
            end += 1
        
        return min_zeros
        
        
        