"""
	(1D Dynamic Programming) 518. Coin Change II (medium)

	Link: https://leetcode.com/problems/coin-change-ii
    
	Tags: Dynamic Programming,

	Constraints:
		- 1 <= coins.length <= 300
		- 1 <= coins[i] <= 5000
		- All the values of coins are unique.
		- 0 <= amount <= 5000
	======================================================================

	Submissions: 
		runtime: 191 ms, beats 60.48%
		memory: 16.57 MB, beats 68.09%
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
# O(n^2)
def change(amount, coins):
	dp = [0] * (amount + 1)
	dp[0] = 1

	# for i in range(len(coins)):
	for c in coins: 
		for j in range(1, amount + 1):
			if j - c >= 0:
				dp[j] = dp[j - c] + dp[j]
	# print('dp', dp)
	return dp[amount]

a1 = 5; c1 = [1,2,5] # 4
a2 = 3; c2 = [2] # 0
a3 = 10; c3 = [10] # 1
a4 = 10; c4 = [1,2,5] # 10
print('RESULT: ', change(a4, c4))