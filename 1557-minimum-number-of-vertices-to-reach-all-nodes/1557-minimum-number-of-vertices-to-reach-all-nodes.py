class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph={} 
        indegree={} 
        for i in range(n): 
            indegree[i]=0 
            graph[i]=0
        for x,y in edges:
            graph[y]+=1 
        vert=[] 
        for i in range(n):
            if graph[i]==0:
                vert.append(i)
        return vert