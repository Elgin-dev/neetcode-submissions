class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            val=s[i]
            if val not in a:
                a[val]=1 
            else:
                a[val]+=1
        for i in range(len(s)):
            val=t[i]
            if val in a and a[val] > 0:
                a[val]-=1
            else:
                return False    
        return True