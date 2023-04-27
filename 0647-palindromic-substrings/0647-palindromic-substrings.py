# Watch neetcode video 
class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        n=len(s)
        for i in range(n):
            # for odd length palindrome
            l=i
            r=i 
            while l>=0 and r<n and s[l]==s[r]:
                res+=1
                l-=1
                r+=1 
            
            # for even length palindrome 
            l=i
            r=i+1  
            while l>=0 and r<n and s[l]==s[r]:
                res+=1
                l-=1
                r+=1 
        return res
        