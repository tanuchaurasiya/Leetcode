class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res=[] 
        for i in range(len(expression)):
            if expression[i]=='-' or expression[i]=='+' or expression[i]=='*': 
                al=self.diffWaysToCompute(expression[:i])
                bl=self.diffWaysToCompute(expression[i+1:]) 
                for x in al:
                    for y in bl:
                        if expression[i]=='-':
                            res.append(x-y) 
                        elif expression[i]=='+':
                            res.append(x+y)
                        elif expression[i]=='*':
                            res.append(x*y) 
        if res==[] : 
            val=""
            for i in range(len(expression)):
                val+=expression[i]
            res.append(int(val)) 
        # print(res)
        return res