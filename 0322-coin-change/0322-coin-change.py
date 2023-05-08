class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def help(i,curr):
            nonlocal amount,n,coins,dp
            # print(i,curr,amount)
            if i>=n or amount<curr:
                return 10**9
            if amount == curr:
                return 0 
            if dp[i][curr]!=-1:
                return dp[i][curr]
            m1=help(i,curr+coins[i])+1
            m2=help(i+1,curr) 
            dp[i][curr]=min(m1,m2)
            return dp[i][curr]
        n=len(coins)
        dp=[] 
        for i in range(n):
            dp.append([-1]*(10**4+1))
        x=help(0,0)  
        if x==10**9:
            return -1
        return x
        