class Solution:
    def fib(self, n: int) -> int:
        self.memo = {0:0, 1:1}
        return self.f(n)
        
    def f(self, n):
        if n in self.memo:
            return self.memo[n]
        two = self.memo[n-2] if n-2 in self.memo else self.f(n-2)
        one = self.memo[n-1] if n-1 in self.memo else self.f(n-1)
        result = one + two
        self.memo[n] = result 
        return result