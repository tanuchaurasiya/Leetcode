class Solution:
    def jump(self, nums: List[int]) -> int:
        def help(n,nums,dp):
            dp[0]=0
            for i in range(n-1):
                for j in range(1,nums[i]+1):
                    if i+j<n:
                        dp[i+j]=min(dp[i]+1,dp[j+i])
                # print(dp)
            return dp[-1]
        n=len(nums)
        dp=[10**9]*n
        return help(n,nums,dp)
        
            