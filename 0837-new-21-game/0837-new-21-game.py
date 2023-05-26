from collections import deque

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if n == 0 or k == 0:
            return 1

        dq = deque([(0, 1.0)])
        dq_sum = 1.0 
        a = 1/maxPts
        for i in range(1, k):
            fi = a * dq_sum
            dq.append((i, fi))
            dq_sum += fi
            if len(dq) > maxPts:
                dq_sum -= dq.popleft()[1]

        ans = 0
        for i in range(k, min(n+1, k+maxPts)):
            ans += a * dq_sum
            pair = dq[0]
            idx, f = pair
            if i - idx >= maxPts:
                dq_sum -= dq.popleft()[1]

        return ans