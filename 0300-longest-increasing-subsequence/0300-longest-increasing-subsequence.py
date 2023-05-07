class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[]
        for i in range(n+1):
            dp.append([0]*(n+1)) 
        for i in range(n-1,-1,-1):
            for j in range(i-1,-2,-1):
                l=dp[i+1][j+1];
                if(j==-1 or nums[i]>nums[j]):
                    l=max(l, 1+dp[i+1][i+1])
                
                dp[i][j+1]=l;
            
        
        return dp[0][0];
    
