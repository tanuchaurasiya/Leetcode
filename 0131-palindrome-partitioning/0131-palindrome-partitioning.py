class Solution:
    def __init__(self):
        self.res=[]
    def partition(self, s: str) -> List[List[str]]:
        def help(i,n,temp,s,var): 
            print(temp, var)
            if i>=n:
                if temp!="" and temp==temp[::-1]:
                    self.res.append(var+[temp])
                return  
            
            if temp!="" and temp==temp[::-1]: 
                help(i+1,n,s[i],s,var+[temp])
                help(i+1,n,temp+s[i],s,var) 
            else:
                help(i+1,n,temp+s[i],s,var) 
                
        n=len(s)
        help(1,n,s[0],s,[]) 
        print(self.res)
        return self.res
            
            