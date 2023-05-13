class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        def help(i,j):
            nonlocal nums1,nums2,n1,n2,dp
            if i>=n1 or j>=n2:
                return 0 
            if dp[i][j]!=-1:
                return dp[i][j]
            if nums1[i]==nums2[j]:
                dp[i][j]=help(i+1,j+1) +1 
            
            else:
                dp[i][j]=max(help(i+1,j), help(i,j+1))
            return dp[i][j]
        
        n1=len(nums1)
        n2=len(nums2)
        dp=[]
        for i in range(n1):
            dp.append([-1]*n2)
        return help(0,0)
        