# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0 
        if root.left==None and root.right==None:
            return 1
        queue=[(root,1,1)]
        maxx=-10**9
        currlevel=1
        while queue:
            res=[]
            while queue and queue[0][2]==currlevel:
                tmp,idx,level=queue.pop(0)
                print(tmp.val,idx,level)
                res.append(idx)
                if tmp.left!=None:
                    left=idx*2 
                    queue.append((tmp.left,left,level+1) )
                
                if tmp.right!=None:
                    right=idx*2+1
                    queue.append((tmp.right,right,level+1) )

            currlevel+=1 
            maxx=max(maxx,res[-1]-res[0]+1) 
            
        return maxx
        