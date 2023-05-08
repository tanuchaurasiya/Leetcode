class Solution:
    def integerBreak(self, n: int) -> int:
        def help(i,summ): 
            nonlocal n,dp
            # print(i,summ,n)
            if i>=n or summ>n:
                return -10**9
            if summ==n:
                return 1 
            if dp[i][summ]!=-1:
                return dp[i][summ]
            m1=help(i,i+summ)*i 
            m2=help(i+1,summ)
            dp[i][summ]=max(m1,m2) 
            return dp[i][summ]
        dp=[] 
        for i in range(n):
            dp.append([-1]*n)
        return help(1,0)
        
            
        