class Solution:
    def numSquares(self, n: int) -> int:
        def help(i,curr):
            nonlocal n,l,dp
            # print(i,curr,amount)
            if i>=100 or n<curr:
                return 10**9
            if n == curr:
                return 0 
            if dp[i][curr]!=-1:
                return dp[i][curr]
            m1=help(i,curr+l[i])+1
            m2=help(i+1,curr) 
            dp[i][curr]=min(m1,m2)
            return dp[i][curr] 
        l=[i*i for i in range(100,0,-1)]
        dp=[] 
        for i in range(100):
            dp.append([-1]*n)
        x=help(0,0)  
        if x==10**9:
            return -1
        return x