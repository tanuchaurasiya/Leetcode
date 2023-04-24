class Solution:
    def __init__(self):
        self.dp=[-1]*31
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n 
        if self.dp[n]!=-1:
            return self.dp[n] 
        self.dp[n]= self.fib(n-1) +self.fib(n-2)
        return self.dp[n]