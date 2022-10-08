class Solution:
    def __init__(self):
        self.c=0
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(graph,node,visited):
            visited[node]=1 
            self.c+=1 
            for child in graph[node]: 
                if not visited[child]: 
                    dfs(graph,child,visited) 
                    
        n=len(rooms) 
        graph={}
        visited={} 
        for i in range(n):
            graph[i]=rooms[i] 
            visited[i]=0  
        print(graph)
        dfs(graph,0,visited)
        if self.c==n:
            return 1
        return 0
        
        
        