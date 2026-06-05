from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque()
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack.pop()!=mapping[i]:
                    return False
        return len(stack)==0                    