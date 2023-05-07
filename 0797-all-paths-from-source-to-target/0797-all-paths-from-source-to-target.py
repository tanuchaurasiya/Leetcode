class Solution: 
    def __init__(self):
        self.res=[]
    def allPathsSourceTarget(self, g: List[List[int]]) -> List[List[int]]:
        def dfs(graph,visited,node,arr,n):
            visited[node]=1 
            arr.append(node) 
            if node==n-1: 
                visited[node]=0
                self.res.append(arr.copy()) 
                # print(arr,self.res)
            for child in graph[node]:
                if not visited[child]:
                    dfs(graph,visited,child,arr,n) 
                    visited[child]=0
            arr.pop(-1)
            # print(res)
        graph={} 
        n=len(g)
        visited={} 
        for i in range(n):
            graph[i]=g[i]
            visited[i]=0  
        arr=[]
        dfs(graph,visited,0,arr,n)
        return self.res
            
        