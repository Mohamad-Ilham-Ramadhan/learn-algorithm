"""
	(2D Dynamic Programming) 518. Coin Change II (medium)

	Link: https://leetcode.com/problems/coin-change-ii
    
	Tags: Dynamic Programming,

	Constraints:
		- 1 <= coins.length <= 300
		- 1 <= coins[i] <= 5000
		- All the values of coins are unique.
		- 0 <= amount <= 5000
	======================================================================

	Submissions: 
      #1
         runtime: 710 ms, beats 18.33%
         memory: 167.54 MB, beats 6.95%
      #2 
         runtime: 387 ms, beats 37.63%
         memory: 26.68 MB, beats 47.74%
      #3
         runtime: 255 ms, beats 54.08%
         memory: 16.74 MB, beats 55.87%

"""
'''
	1 2 3 4 5
1  1 1 1 1 1
2  1 2 2 3 3
5  1 2 3 3 4

	1 2 3 4 5 6 7 8 9 10
1  1 1 1 1 1 1 1 1 1 1
2  1 2 2 3 3 4 4 5 5 6
5  1 2 3 3 4 5 6 8 8 10
'''
# NeetCode's solution
# #1 2D dynamic programming
def change(amount, coins):
   cache = {}

   def dfs(i,a):
      if a == amount:
         return 1
      if a > amount:
         return 0
      if i == len(coins):
         return 0
      if (i, a) in cache:
         return cache[(i,a)]
      
      cache[(i,a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
      return cache[(i,a)]
   return dfs(0,0)

# #2 2D dynamic programming
def second(amount, coins):
   dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
   dp[0] = [1] * (len(coins) + 1)

   for a in range(1, amount + 1):
      for i in range(len(coins) - 1, -1, -1):
         dp[a][i] = dp[a][i + 1]
         if a - coins[i] >= 0:
            dp[a][i] += dp[a - coins[i]][i]
   return dp[amount][0]
   
# #3 1D dynamic programming
def third(amount, coins):
   dp = [0] * (amount + 1)
   dp[0] = 1

   for i in range(len(coins) -1, -1, -1):
      nextDP = [0] * (amount + 1)
      nextDP[0] = 1

      for a in range(1, amount + 1):
         nextDP[a] = dp[a]
         if a - coins[i] >= 0:
            nextDP[a] += nextDP[a - coins[i]]
      dp = nextDP
   return dp[amount]

a1 = 5; c1 = [1,2,5] # 4
a2 = 3; c2 = [2] # 0
a3 = 10; c3 = [10] # 1
a4 = 10; c4 = [1,2,5] # 10
print('RESULT: ', change(a4, c4))