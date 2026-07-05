class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for ch in logs:
            
            if ch=='../':
                if stack:
                    stack.pop()
            elif ch=='./':
                continue
            else:
                stack.append(ch)  
        count=0
        while stack:
            if len(stack)>0:
                stack.pop()
                count+=1
        return count                   
