class Solution:
    def __init__(self):
        self.c=0
    
    def minReorder(self, n: int, conn: List[List[int]]) -> int: 
        def bfs(graphD,graphUnD,reach,queue): 
            while queue:
                temp=queue.pop(0) 
                reach[temp]=1
                for child in graphUnD[temp]:
                    if not reach[child]:
                        if 0 not in graphD[child] and temp not in graphD[child]:
                            self.c+=1
                            # print(child)
                            graphD[child].append(0) 
                            reach[child]=1 
                        queue.append(child) 
            
                 
            return self.c
            
        graphD={} 
        reach={} 
        queue=[0]
        graphUnD={}
        for i in range(n):
            graphD[i]=[] 
            graphUnD[i]=[] 
            reach[i]=0  
        for x,y in conn:
            graphD[x].append(y) 
            graphUnD[x].append(y)
            graphUnD[y].append(x)
        # print(graphD)
        # print(graphUnD)
        return bfs(graphD,graphUnD,reach,queue)