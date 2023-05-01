class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort() 
        n=len(salary) 
        res=0
        for i in range(1,n-1):
            res+=salary[i] 
        return res/(n-2)
        