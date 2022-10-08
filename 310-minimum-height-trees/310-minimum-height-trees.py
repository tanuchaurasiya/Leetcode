class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]: 
        graph={} 
        graph1={} 
        if n==1:
            return [0]
        for i in range(n):
            graph[i]=0 
            graph1[i]=[]
        for x,y in edges:
            graph[x]+=1
            graph[y]+=1 
            graph1[x].append(y)
            graph1[y].append(x)
       
        queue=[] 
        for i in range(n):
            if graph[i]==1:
                queue.append(i) 
        vertices=n 
        while vertices>2:
            vertices-=len(queue)
            for i in range(len(queue)):
                x=queue.pop(0)
                # print(graph1[x])
                for child in graph1[x]:
                    graph[child]-=1 
                    if graph[child]==1:
                        queue.append(child) 
        return queue
        