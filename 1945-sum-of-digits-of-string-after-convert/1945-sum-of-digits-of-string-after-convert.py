class Solution:
    def getLucky(self, st: str, k: int) -> int:
        var=0 
        for x in st:
            y=ord(x)-ord('a')+1
            var=var + y//10+y%10
        st=str(var)
        print(st) 
        res=0 
        k-=1
        while k:
            for x in st:
                res+=int(x) 
            st=str(res) 
            k-=1
            res=0
        return int(st)