class Solution:
    def longestObstacleCourseAtEachPosition(self, o: List[int]) -> List[int]:
        dp=list()
        res=list()
        for i in o:
            if not dp or i >= dp[-1]:
                dp.append(i)
                res.append(len(dp))
            else:
                pos = self.binarySearch(dp, i)
                dp[pos] = i
                res.append(pos + 1)
        return res
    
    def binarySearch(self, dp: List[int], target: int) -> int:
        l, r = 0, len(dp) - 1
        while l < r:
            mid = (l + r) // 2
            if dp[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l