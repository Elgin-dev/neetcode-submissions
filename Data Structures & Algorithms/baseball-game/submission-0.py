class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for ch in operations:
            if ch=="+":
                a=stack[-1]
                b=stack[-2]
                c=a+b
                stack.append(c)
            elif ch=="C":
                stack.pop()
            elif ch =="D":
                a=stack[-1]
                
                c=2*a
                stack.append(c)
            else:
                i=int(ch)
                stack.append(i)
        return sum(stack)                 
