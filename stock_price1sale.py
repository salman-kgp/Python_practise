

def maxProfit(prices):
    min_so_far = prices[1]
    max_profit = 0
    for i in range(1,len(prices)):
        max_today = prices[i] - min_so_far
        max_profit=max(max_profit,max_today)
        min_so_far = min(min_so_far,prices[i])
        
    if max_profit>0:
        return max_profit
    else:
        return 0