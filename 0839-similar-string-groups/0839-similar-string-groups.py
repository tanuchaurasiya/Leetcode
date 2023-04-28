class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def areNeighbors(a,b):
            dif = 0
            for i in range(len(a)): 
                if a[i]!=b[i]: 
                    dif += 1 
            return dif==0 or dif==2 
        
        def find(graph,node): 
            if type(graph[node])==int and graph[node]<0:
                return node
            else:
                temp=find(graph,graph[node])
                graph[node]=temp
                return temp 
        
        def union(graph,node1,node2):
            node1=find(graph,node1)
            node2=find(graph,node2)
            if node1==node2:
                return 
            else:
                if abs(graph[node1])>=abs(graph[node2]):
                    graph[node1]==graph[node2]+graph[node1]
                    graph[node2]=node1
                else:
                    graph[node2]==graph[node2]+graph[node1]
                    graph[node1]=node2
                    
        
        graph = {} 
        for x in strs:
            graph[x]=-1 
        
        print(graph)
        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                if areNeighbors(strs[i],strs[j]): 
                    union(graph,strs[i],strs[j])
        print(graph) 
        res=0 
        for key,val in graph.items():
            if val==-1:
                res+=1 
        return res

        
        