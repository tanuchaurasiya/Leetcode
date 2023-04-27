class Solution:
    def __init__(self):
        self.res=0
    def countVowelStrings(self, n: int) -> int:
        def help(i,n,c):
            if c>=n:
                self.res+=1
                return 
            for k in range(5-i):
                help(i+k,n,c+1)
        help(0,n,0)
        return self.res