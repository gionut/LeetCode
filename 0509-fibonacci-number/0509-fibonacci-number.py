class Solution:
    def fib(self, n: int) -> int:
        self.memo = {0:0, 1:1}
        return self.f(n)
        
    def f(self, n):
        if n in self.memo:
            return self.memo[n]
        result = self.f(n-2) + self.f(n-1)
        self.memo[n] = result 
        return result