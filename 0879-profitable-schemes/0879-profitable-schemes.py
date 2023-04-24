# class Solution:
#     def profitableSchemes(self, n: int, mprofit: int, group: List[int], profit: List[int]) -> int:
#         def help(idx,leng,n,mprofit,group,profit,gcount,cprofit,dp): 
#             print(idx,cprofit,gcount)
#             if idx>=leng: 
#                 if cprofit>=mprofit and gcount<=n:
#                     return 1
#                 return 0
#             if dp[idx]!=-1:
#                 return dp[idx] 
#             dp[idx]=help(idx+1,leng,n,mprofit,group,profit,gcount+group[idx],cprofit+profit[idx],dp)+help(idx+1,leng,n,mprofit,group,profit,gcount,cprofit,dp)
#             return dp[idx] 
        
#         leng=len(group)
#         gcount=0
#         cprofit=0 
#         dp=[-1]*leng
#         res= help(0,leng,n,mprofit,group,profit,gcount,cprofit,dp)
#         print(dp)
#         return res

    
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:    
        l=len(group)
        dp=[[[-1 for _ in range(n+1)] for _ in range(minProfit+1)] for _ in range(l+1)]
        def solve(i,p,ng):
            if ng>n : return 0
            if i>=l:
                if p>=minProfit and ng<=n:
                    return 1
                return 0
            if dp[i][p][ng]!=-1 : return dp[i][p][ng]
            n1=solve(i+1,p,ng) # not pick
            n2=solve(i+1,min(minProfit,p+profit[i]),ng+group[i]) # pick
            #used min(minProfit,p+profit[i]) to avoid using extra space and time of 
            #creating dp table if we will not use this then  while creating dp table
            # for y axix range will be sum(profit)+1 beacuse maximum profit that can 
            #be added is sum of profit array
            dp[i][p][ng]=n1+n2 # storing in dp table
            return n1+n2
        
        return solve(0,0,0)%(10**9+7)
        
            
            