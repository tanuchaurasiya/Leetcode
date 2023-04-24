# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def help(root,turn,c,dp):
            if root==None:
                return c
            if dp[root]!=-1:
                return dp[root] 
            if turn==-1:
                dp[root] = max(help(root.left,1,0,dp),help(root.right,0,0,dp)) 
            if turn==0:
                dp[root] = max(help(root.left,1,c+1,dp) ,help(root,-1,0,dp) )
            if turn==1:
                dp[root] = max(help(root.right,0,c+1,dp) ,help(root,-1,0,dp) ) 
            return dp[root] 

        def inorder(root,dp):
            if root==None:
                return 
            else:
                dp[root]=-1 
                inorder(root.left,dp) 
                inorder(root.right,dp)
        dp={} 
        inorder(root,dp)
        return help(root,-1,0,dp) 