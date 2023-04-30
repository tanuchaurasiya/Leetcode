class Solution:
    def findLength(self, s1: List[int], s2: List[int]) -> int:
        def lcs(i1,i2,n1,n2,s1,s2,dp): 
            ans=0
            for i1 in range(n1):
                for i2 in range(n2): 
                    if s1[i1]==s2[i2]:
                        if i1>0 and i2>0:
                            dp[i1][i2]= dp[i1-1][i2-1]+1 
                        else:
                            dp[i1][i2]=1 
                        ans=max(ans,dp[i1][i2])
                    else:       
                        dp[i1][i2]=0
            # print(dp)
            return ans
        
        dp=[] 
        n1=len(s1)
        n2=len(s2)
        for i in range(n1):
            dp.append([-1]*n2)
        return lcs(0,0,n1,n2,s1,s2,dp) 
       
    
        