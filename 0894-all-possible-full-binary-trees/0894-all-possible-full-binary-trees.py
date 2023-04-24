# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Watch neetcode video
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        def help(n,dp):
            if n==0:
                return [] 
            if n==1:
                return [TreeNode()] 
            if n in dp:
                return dp[n] 
            res=[] 
            for left in range(n):
                right=n-left-1
                lefttrees, righttrees=help(left,dp), help(right,dp) 
                for t1 in lefttrees:
                    for t2 in righttrees: 
                        res.append(TreeNode(0,t1,t2)) 
            dp[n]=res
            return dp[n]
        dp={} 
        return help(n,dp)
            
