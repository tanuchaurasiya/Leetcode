class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def help(idx,s,res,n,l,left,right):
            if idx>=l:
                res.append(s)
                return 
            if left<n:
                help(idx+1,s+"(",res,n,l,left+1,right)
            if right<left:
                help(idx+1,s+")",res,n,l,left,right+1) 
        
        res=[] 
        help(0,"",res,n,n*2,0,0)
        return res
            
        