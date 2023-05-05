class Solution:
    def maxVowels(self, s: str, k: int) -> int: 
        vow=0
        vowel=['a','e','i','o','u']
        for i in range(min(k,len(s))):
            if s[i] in vowel: 
                vow+=1
        res=-10**9 
        res=max(res,vow)  
        for i in range(k,len(s)):
            if s[i-k] in vowel: 
                vow-=1
            if s[i] in vowel:
                vow+=1
            res=max(res,vow)  
        return res
        