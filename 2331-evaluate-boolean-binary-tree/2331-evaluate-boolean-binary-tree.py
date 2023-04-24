# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def help(root):
            if root.val==1 or root.val==0:
                return root.val 
            if root.val==2:
                l=help(root.left) 
                r= help(root.right)
                if l==1 or r==1:
                    root.val= 1 
                else:
                    root.val=0 
            if root.val==3:
                l=help(root.left) 
                r= help(root.right)
                if l==1 and r==1:
                    root.val= 1 
                else:
                    root.val=0 
            return root.val
        return help(root)
        