class Solution:
    def __init__(self):
        self.c=1 
    def reachableNodes(self, n: int, edges: List[List[int]], rest: List[int]) -> int: 
        def dfs(graph,node,visited,res):
            visited[node]=1 
            for child in graph[node]:
                if (not visited[child]) and (not res[child]):
                    self.c+=1 
                    dfs(graph,child,visited,res) 
            return self.c
        graph={}
        visited={}
        res={} 
        for i in range(n):
            graph[i]=[] 
            visited[i]=0  
            res[i]=0 
        for x in rest:
            res[x]=1 
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        return dfs(graph,0,visited,res)