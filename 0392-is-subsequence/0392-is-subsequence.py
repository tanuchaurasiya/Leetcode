class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def help(i,n,j,m,s,t,dp):
            # print(i,j)
            if i>=n:
                return 1 
            if j>=m:
                return 0 
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==t[j]:
                dp[i][j] = help(i+1,n,j+1,m,s,t,dp)  
            else:
                dp[i][j] = help(i,n,j+1,m,s,t,dp) 
            return dp[i][j] 
        dp=[] 
        n=len(s)
        m=len(t)
        for i in range(n):
            dp.append([-1]*m) 
        return help(0,n,0,m,s,t,dp)