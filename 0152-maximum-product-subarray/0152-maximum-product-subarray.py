class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        res=-10**9
        prefix=1
        suffix=1
        for i in range(n):
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
            prefix=prefix*nums[i] 
            suffix=suffix*nums[n-i-1]
            res=max(res,max(prefix,suffix))
        return res
                