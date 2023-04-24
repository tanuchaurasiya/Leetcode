class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        el_sum = d_sum = 0
        for i in nums:
            el_sum += i
            d_sum += self.digit_sum(i)
        return abs(el_sum - d_sum)
    
    def digit_sum(self, n: int) -> int:
        sum = 0
        while n:
            sum += int(n % 10)
            n //= 10
        return sum
        
        