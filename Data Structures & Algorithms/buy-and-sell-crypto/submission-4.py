class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        #we want to basically buy low, sell high 
        max_profit = 0

        #slidingwindowquestion 

        #brute force solution 
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)

        return max_profit 

        #slidingwindow

        max_profit = 0 
        left = 0 
        right = 1
        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            else: 
                left = right 
            right += 1
        
        return max_profit