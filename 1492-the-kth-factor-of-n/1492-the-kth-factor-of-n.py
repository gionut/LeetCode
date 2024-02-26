class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i = 1
        first_half = deque()
        second_half = deque()
        while i*i <= n:
            if n % i == 0:
                first_half.append(i)
                if n//i != i:
                    second_half.appendleft(n//i)
            i+=1
        factors = first_half + second_half
        print(factors)
        return factors[k-1] if len(factors) >= k else -1