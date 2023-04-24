class Solution:
    def lcs(self,i1,i2,n1,n2,s1,s2,dp): 
        if i1>=n1 or i2>=n2: 
            return 0
        if dp[i1][i2]!=-1:
            return dp[i1][i2]
        m1=-10**9
        m2=-10**9
        if s1[i1]==s2[i2]:
            return self.lcs(i1+1,i2+1,n1,n2,s1,s2,dp) + 1
        else:       
            m1=self.lcs(i1+1,i2,n1,n2,s1,s2,dp) 
            m2=self.lcs(i1,i2+1,n1,n2,s1,s2,dp)  
        dp[i1][i2]=max(m1,m2)  
        return dp[i1][i2]

    def minInsertions(self, s1: str) -> int: 
        n1=len(s1)
        s2=s1[::-1]
        dp=[] 
        for i in range(n1):
            dp.append([-1]*n1)
        res= self.lcs(0,0,n1,n1,s1,s2,dp)  
        print(res)
        return n1-res
                