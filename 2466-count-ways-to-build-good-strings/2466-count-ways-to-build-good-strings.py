class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int: 
        def help(i):
            nonlocal low,high, zero,one,dp
            if i>high+1:
                return 0 
            if dp[i]!=-1:
                return dp[i]
            m1=0
            m2=0
            if low<=i+zero<=high:
                m1=help(i+zero) +1 
            else:
                m1=help(i+zero)  
            
            if low<=i+one<=high:
                m2=help(i+one) +1 
            else:
                m2=help(i+one)  
            
            dp[i]=(m1+m2)%(10**9+7) 
            return dp[i]
        dp=[-1]*(low+high+1) 
        return help(0)
            
            
            
            
        