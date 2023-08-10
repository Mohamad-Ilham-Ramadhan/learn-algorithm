'''
    (2D dynamic programming) Leetcode: 309. Best Time to Buy and Sell Stock with Cooldown (medium)

    Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

    Acceptance Rate: 57.0%

    Related topics: Array, Dynamic Programming

    ============================================================    
    
    Submission:
        NeetCode's solution:
            runtime: 50ms, beats 85.36%
            memory: 21.56 MB, beats 26.10%

    ================================

    Input: prices = [1,2,3,0,2]
    Output: 3
    Explanation: transactions = [buy, sell, cooldown, buy, sell]

    [0, 1, 0, 0, 2] => 3
    [0, 0, 1, 0, 0] => 0
    [0, 0, 0]

    [4,6,0,2,9,1,10] => 11
    [[b,4], [s,6,2], [c,0], [b,2], [s,9,7], []]
    [[b1,s10, 9] [b9,s10, 1] [b2, s9, 7] [b2, s10, 8]]
'''

def maxProfit(prices):
    # State: Buying or Selling?
    # If buy: i + 1
    # If sell: i + 2

    dp = {} # key=(i, buying) val=max_profit

    def dfs(i, buying):
        if i >= len(prices):
            return 0
        if (i, buying) in dp: 
            return dp[(i, buying)]
        
        cooldown = dfs(i + 1, buying)
        if buying: 
            buy = dfs(i + 1, not buying) - prices[i]
            dp[(i, buying)] = max(buy, cooldown)
        else: 
            sell = dfs(i + 2, not buying) + prices[i]
            dp[(i, buying)] = max(sell, cooldown)

        return dp[(i, buying)]
    
    return dfs(0, True)
'''
   [4,6,0,2,9,1,10] => 11

   dp {
      (0, True): 11
      (1, False): 15
      (1, True): 11
      (2, False): 11
      (2, True): 9
      (3 False): 11
      (3, True): 9
      (4, False): 1
      (4, True): 9
      (5, False): 1
      (5, True): 9
      (6, False): 10
      (6, True): 0
      (7, True): 0
   }
'''
print('RESULT: ', maxProfit([4,6,0,2,9,1,10]))