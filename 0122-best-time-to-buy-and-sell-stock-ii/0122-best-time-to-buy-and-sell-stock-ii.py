class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        max_profit = 0
        for i in range(len(prices)):
            if stack and prices[i] > stack[-1]:
                curr = stack.pop()
                pro =  prices[i] - curr 
                max_profit += pro
            stack.append(prices[i])
        return max_profit
