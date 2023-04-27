class Solution:
    def addDigits(self, num: int) -> int:
        while(len(str(num))>1): 
            res=0
            while(num!=0): 
                rem=num%10 
                res+=rem 
                num=num//10 
            num=res 
            # print(num)
        return num
            