class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph={} 
        graph1={}
        for i in range(n):
            graph[i]=0 
            graph1[i]=0
        for x,y in roads:
            graph[x]+=1 
            graph[y]+=1 
        graph=sorted(graph.items(),key=lambda x:x[1],reverse=True) 
        for x,y in graph:
            graph1[x]=n 
            n-=1 
        # print(graph)
        # print(graph1)
        res=0 
        for x,y in roads:
            res=res+graph1[x]+graph1[y] 
        return res

