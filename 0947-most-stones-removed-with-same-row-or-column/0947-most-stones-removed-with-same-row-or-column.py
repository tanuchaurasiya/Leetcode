class Solution:
    def removeStones(self, stones: List[List[int]]) -> int: 
        def find(node,graph):
            if graph[node]<0:
                return node 
            else:
                temp=find(graph[node],graph) 
                graph[node]=temp 
                return temp 
        def union(n1,n2,graph):
            node1=find(n1,graph) 
            node2=find(n2,graph) 
            if node1==node2:
                return 0 
            else:
                if abs(graph[node1])>=abs(graph[node2]):
                    graph[node1]=graph[node1]+graph[node2] 
                    graph[node2]=node1 
                else:
                    graph[node2]=graph[node1]+graph[node2] 
                    graph[node1]=node2 
            return 1 
        n=len(stones) 
        graph={}
        print(graph)
        for i in range(n):
            graph[i]=-1
        for i in range(n):
            for j in range(i+1,n): 
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    union(i,j,graph) 
        print(graph)
        res=0 
        for x in graph.values():
            if x<0:
                res+=1
        return n-res 
