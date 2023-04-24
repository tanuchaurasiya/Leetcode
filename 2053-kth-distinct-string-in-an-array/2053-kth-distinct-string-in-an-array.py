class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d=defaultdict(lambda:0)
        for x in arr:
            d[x]+=1 
        c=1
        # print(d)
        for x in arr:
            if d[x]==1:
                if c==k:
                    return x 
                else:
                    c+=1
        return "" 
            