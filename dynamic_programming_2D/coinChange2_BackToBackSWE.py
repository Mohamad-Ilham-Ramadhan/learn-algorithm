'''
    (2D dynamic programming) Leetcode: 518. Coin Change II (medium)

    Link: https://leetcode.com/problems/coin-change-ii/

    Acceptance Rate: 61.4%

    Related topics: Array, Dynamic Programming

    Constraints:
        - 1 <= coins.length <= 300
        - 1 <= coins[i] <= 5000
        - All the values of coins are unique.
        - 0 <= amount <= 5000

    ============================================================    
    
    Submission:
        Back to Back SWE's idea:
            runtime: 347 ms, beats 56.83%
            memory: 32.16 MB, beats 40.12%

    ================================

    Input: amount = 5, coins = [1,2,5]
    Output: 4
    Explanation: there are four ways to make up the amount:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1

'''
def change(amount, coins): 
    dp = []
    dp.append([]) 
    dp[0].append(1)
    for i in range(1, amount + 1): 
        dp[0].append(0)

    for i in range(1, len(coins)+1) :
        c = coins[i-1]
        dp.append([])
        dp[i].append(1)
        for j in range(1, amount + 1):
            dp[i].append(dp[i-1][j])
            if (j - c) >= 0: 
                dp[i][j] = dp[i][j - c] + dp[i-1][j]
    return dp[len(coins)][amount]



print('RESULT: ', change(12, [1,4,5,8]))