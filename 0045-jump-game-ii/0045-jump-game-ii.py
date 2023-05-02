class Solution:
    def jump(self, nums: List[int]) -> int:
        def help(i,n,nums,dp):
            # print(i,c)
            if i>=n-1:
                return 0
            if dp[i]!=-1:
                return dp[i]
            minn=10**9
            for j in range(1,nums[i]+1):
                minn=min(minn,help(i+j,n,nums,dp)+1) 
            dp[i]=minn
            return dp[i]
        n=len(nums)
        dp=[-1]*n
        return help(0,n,nums,dp)
        
            