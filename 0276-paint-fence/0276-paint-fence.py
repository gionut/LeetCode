class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        
        secondLast = k
        last = k*k
        
        for i in range(2, n):
            crt = (k-1)*(last + secondLast)
            secondLast = last
            last = crt
        
        return last