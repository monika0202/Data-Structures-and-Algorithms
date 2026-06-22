# 509. Fibonacci Number
# Recursion
# TC: O(2^n)
# SC: O(n)

class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n

        return self.fib(n-1) +self.fib(n-2)   
        