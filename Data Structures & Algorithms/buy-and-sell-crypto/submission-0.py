class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pr=0
        min_pr=float('inf')
        for i in range(len(prices)):
            if prices[i]<min_pr:
                min_pr=prices[i]
            
            profit=prices[i]-min_pr
            if profit>max_pr:
                max_pr=profit
        return max_pr                   
