class Solution:
    def numDecodings(self, s: str) -> int:
        
        def dfs(i,n):
            nonlocal d
            if i in d:
                return d[i]
            if s[i]=='0':
                return 0 
            res=0
            res+=dfs(i+1,n) 
            if i+1<n and ((s[i]=='1') or (s[i]=='2' and s[i+1] in '0123456')) :
                res+=dfs(i+2,n) 
            d[i]=res
            return res 
        n=len(s)
        d={n:1}
        return dfs(0,n)
        
        