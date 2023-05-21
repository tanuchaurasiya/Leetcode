import heapq 
from collections import defaultdict 
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d=defaultdict(int) 
        for x in hand: 
            d[x]+=1 

        h=hand.copy()
        heapq.heapify(h) 
        while h:
            minn=heapq.heappop(h)
            if d[minn]==0:
                continue
            gs=groupSize 
            while gs:
                if d[minn]==0:
                    return False 
                d[minn]-=1 
                minn+=1
                gs-=1 
        return True
