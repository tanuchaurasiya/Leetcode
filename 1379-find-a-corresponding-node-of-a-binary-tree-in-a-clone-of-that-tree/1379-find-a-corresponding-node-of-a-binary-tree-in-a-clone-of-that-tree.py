# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def help(root1,root2,tar):
            if root1==None:
                return None
            if root1.val==tar.val and root2.val==tar.val:
                return root2 
            x = help(root1.left,root2.left,tar) 
            if x!=None:
                return x
            x = help(root1.right,root2.right,tar) 
            if x!=None:
                return x  
            return None 
        return help(original,cloned,target)
            