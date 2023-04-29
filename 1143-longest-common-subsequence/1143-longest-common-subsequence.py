class Solution:
    def __init__(self):
        self.res=0
    def longestCommonSubsequence(self, s1: str, s2: str) -> int: 
        def lcs(i1,i2,n1,n2,s1,s2,dp): 
            ans=0
            for i1 in range(n1):
                for i2 in range(n2): 
                    # print(i1,i2,s1[i1],s2[i2])
                    if s1[i1]==s2[i2]:
                        if i1>0 and i2>0:
                            dp[i1][i2]= dp[i1-1][i2-1]+1 
                        else:
                            dp[i1][i2]=1
                        
                    else:       
                        if i1<1 and i2<1:
                            dp[i1][i2]= 0 
                        elif i2<1:
                            dp[i1][i2]=dp[i1-1][i2]
                        elif i1<1:
                            dp[i1][i2]=dp[i1][i2-1]
                        else:
                            dp[i1][i2]=max(dp[i1-1][i2],dp[i1][i2-1])
            print(dp)
            return dp[-1][-1]
        
        dp=[] 
        n1=len(s1)
        n2=len(s2)
        for i in range(n1):
            dp.append([-1]*n2)
        return lcs(0,0,n1,n2,s1,s2,dp) 
       
        



            