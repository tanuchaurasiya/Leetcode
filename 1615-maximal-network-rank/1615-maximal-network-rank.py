class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        s=list()
        graph={}
        count={}
        if len(roads)==1:
            return 1
        for i in range(n):
            graph[i]=[] 
            count[i]=0
        for x,y in roads:
            graph[x].append(y)
            count[x]+=1
            graph[y].append(x) 
            count[y]+=1 
        for i in range(n):
            for j in range(i+1,n):
                if i in graph[j] and j in graph[i]:
                    s.append(count[i]+count[j]-1)
                else:
                    s.append(count[i]+count[j]) 
        # print(s)
        return max(s)