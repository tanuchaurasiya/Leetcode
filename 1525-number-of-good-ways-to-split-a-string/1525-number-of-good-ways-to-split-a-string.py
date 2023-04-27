class Solution:
    def numSplits(self, s: str) -> int:
        import collections 

        d_left = collections.defaultdict(int)
        d_right = collections.defaultdict(int)

        for i in s:
            d_right[i] += 1
        
        dp = [0 for i in range(len(s))]
        for i in range(len(s)):
            
            d_left[s[i]] += 1
            try:
                d_right[s[i]] -= 1
                if d_right[s[i]] ==0:
                    d_right.pop(s[i])
            except:
                pass


            if len(d_left.keys()) == len(d_right.keys()):

                dp[i] = dp[i-1] + 1

        return max(dp)
            
        