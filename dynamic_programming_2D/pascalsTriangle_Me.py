"""
	(1D dynamic programming) Leetcode: 118. Pascal's Triangle (easy)

	Link: https://leetcode.com/problems/pascals-triangle/
    
	Tags: Array, Dynamic programming

	Constraints:
		- 1 <= n <= 30
	======================================================================

	Submissions: 
			runtime: 46 ms, beats 58.18%
			memory: 16.34 MB, beats 41.90%
"""
def generate(numRows):
	if numRows == 1: [[1]]
	dp = [] 
	for i in range(numRows): dp.append([])
	dp[0] = [1]
	
	for i in range(1, numRows):
		dp[i].append(1)
		for j in range(1, i):
			dp[i].append(dp[i-1][j-1] + dp[i-1][j])
		dp[i].append(1)

	return dp

print('RESULT: ', generate(8))

