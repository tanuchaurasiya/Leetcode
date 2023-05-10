class Solution:
    def integerReplacement(self, n: int) -> int:
        def help(i,dp):
            if i==1:
                return 0 
            if dp[i]!=-1:
                return dp[i]
            if i%2==0:
                dp[i]=help(i//2,dp)+1 
            else:
                dp[i]=min(help(i+1,dp), help(i-1,dp)) + 1 
            return dp[i]
        dp=defaultdict(lambda :-1)
        return help(n,dp)