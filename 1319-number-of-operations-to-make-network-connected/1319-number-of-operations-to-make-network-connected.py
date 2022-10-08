class Solution:
    def makeConnected(self, n: int, conn: List[List[int]]) -> int:  
        def connec_comp(graph,visited,i):
            visited[i]=1 
            for child in graph[i]:
                if not visited[child]:
                    connec_comp(graph,visited,child)
        l=len(conn) 
        # print(l)
        if n-1>l:
            return -1 
        else:
            graph={} 
            visited={}
            for i in range(n):
                graph[i]=[] 
                visited[i]=0
            for x,y in conn:
                graph[x].append(y)
                graph[y].append(x) 
            res=0
            for i in range(n):
                if visited[i]==0:
                    res+=1
                    connec_comp(graph,visited,i) 
            return res-1
            