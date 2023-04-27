class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def help(x,dp):
            # print(x)
            if x==1 :
                return 0
            if x>1000:
                if x%2==0:
                    return help(x//2,dp) + 1 
                else:
                    return help(3*x+1,dp) + 1 
    
            if dp[x]!=-1:
                return dp[x] 
            
            if x%2==0:
                dp[x] = help(x//2,dp) + 1
            else:
                dp[x]=help(3*x+1,dp)+1
            return dp[x]  
        
        res=[] 
        dp=[-1]*1001
        for x in range(lo,hi+1):
            # print("b")
            if x==1:
                res.append([1,1])
            else:
                res.append([x,help(x,dp)]) 
        res=sorted(res,key=lambda x:(x[1],x[0]))
        # print(res)
        return res[k-1][0]