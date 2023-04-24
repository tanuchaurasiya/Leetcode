class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        res="" 
        n1=len(w1)
        n2=len(w2)
        i1=0
        i2=0 
        while i1<n1 and i2<n2:
            res+=w1[i1]+w2[i2] 
            i1+=1
            i2+=1 
        while i1<n1:
            res+=w1[i1]
            i1+=1
        while i2<n2:
            res+=w2[i2]
            i2+=1
        return res

