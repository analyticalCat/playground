""" The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.

Given N, calculate F(N)
 """

class Solution:
    def fib(self, N: int) -> int:
        if N==0: 
            return 0
        elif N==1:
            return 1
        else:

            a=0
            b=1
            for i in range(N):
                if i >= 1:
                    c=b+a
                    a=b
                    b=c
        
            return c

            


a = Solution()
print(a.fib(5))