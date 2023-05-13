class Solution:
    def mostPoints(self, ques: List[List[int]]) -> int: 
        def help(i):
            nonlocal n,ques,dp 
            if i>=n:
                return 0 
            if dp[i]!=-1:
                return dp[i]
            m1=help(ques[i][1]+i+1) + ques[i][0]
            m2=help(i+1) 
            dp[i] = max(m1,m2) 
            return dp[i]
        n=len(ques)
        dp=[-1]*n
        return help(0)
        