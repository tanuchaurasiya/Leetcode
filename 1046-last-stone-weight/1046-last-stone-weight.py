class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int: 
        for i in range(len(stones)):
            stones[i]=-stones[i]
        heapq.heapify(stones)
        while(len(stones)>1):
            y=heapq.heappop(stones)
            x=heapq.heappop(stones)
            print(y,x)
            if x!=y:
                heapq.heappush(stones,y-x) 
            print(stones)
                
        if len(stones)==1:
            return -stones[0]
        else:
            return 0
        