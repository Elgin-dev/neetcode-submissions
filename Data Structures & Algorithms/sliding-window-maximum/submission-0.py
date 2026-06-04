class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        for i in range(len(nums)-k+1):
            
            a=self.maxichecker(nums,i,k)
            ans.append(a)
        return ans    


    def maxichecker(self,nums,start,k):
        maxi=nums[start]
        for i in range(start, start + k):
            if nums[i] > maxi:
                maxi = nums[i]
        return maxi        