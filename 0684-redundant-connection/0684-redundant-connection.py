class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]: 
        def find(graph,node):
            if graph[node]<0:
                return node 
            else:
                temp=find(graph,graph[node]) 
                graph[node]=temp 
                return temp 
        
        def union(n1,n2,graph):
            f1=find(graph,n1) 
            f2=find(graph,n2)
            if f1==f2:
                return 0 
            else:
                if graph[f1]==graph[f2] or abs(graph[f1])>abs(graph[f2]):
                    graph[f1]=graph[f1]+graph[f2] 
                    graph[f2]=f1 
                else:
                    graph[f2]=graph[f1]+graph[f2] 
                    graph[f1]=f2 
            # print(graph)
            return 1   
        n=len(edges)
        graph = {} 
        for i in range(1,n+1):
            graph[i]=-1
        res=[[]]
        for i in range(n):
            if union(edges[i][0],edges[i][1],graph)==0:
                res.append(edges[i]) 
        return res[-1] 
        
