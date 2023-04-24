class Solution:
    def tribonacci(self, n: int) -> int:
        def help(dp,n):
            if n==0 :
                return 0 
            if n==1:
                return 1
            if n==2:
                return 1 
            if dp[n]!=-1:
                return dp[n] 
            dp[n]=help(dp,n-1) + help(dp,n-2) + help(dp,n-3) 
            return dp[n] 
        dp=[-1]*38 
        return help(dp,n)