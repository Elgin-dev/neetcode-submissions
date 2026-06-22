class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall=r_wall=0
        n=len(height)
        l=[0]*n
        r=[0]*n
        for i in range(n):
            j=-i-1
            l[i]=l_wall
            r[j]=r_wall
            l_wall=max(l_wall,height[i])
            r_wall=max(r_wall,height[j])
        summ=0
        for i in range(n):
            pot=min(l[i],r[i])
            summ+=max(0,pot-height[i])
        return summ    