"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node': 
        if node==None:
            return None 
        clone=Node(1)
        res=clone
        queue=[(node,clone)]  
        visited=[None]*101 
        visited[1]=clone
        while queue:
            par,clone=queue.pop(0)
            for child in par.neighbors: 
                if not visited[child.val]:
                    temp=Node(child.val)
                    visited[child.val]=temp  
                    clone.neighbors.append(temp) 
                    queue.append((child,temp))  
                else: 
                    clone.neighbors.append(visited[child.val]) 
        return res
        
            
        