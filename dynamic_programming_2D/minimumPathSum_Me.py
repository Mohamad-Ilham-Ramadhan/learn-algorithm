"""
	(2D Dynamic Programming) 64. Minimum Path Sum (medium)

	Link: https://leetcode.com/problems/minimum-path-sum
    
	Constraints:
		- m == grid.length
		- n == grid[i].length
		- 1 <= m, n <= 200
		- 0 <= grid[i][j] <= 200
	
	Tags: Array, Dynamic Programming, Matrix
	======================================================================
   
   Submission:
		runtime: 90 ms, beats 87.93%
      memory: 17.08 MB, beats 93.76%

"""

'''
g1 = [[1,3,1],
   	[1,5,1],
   	[4,2,1]] # 7
      
      [1 4 5]
      [2 7 6]
      [6 8 7]
'''
def minPathSum(grid):
	inf = 10000000
	dp = [inf] * (len(grid[0]) + 1)
	dp[1] = 0
	for i in range(len(grid)):
		newDp = [inf]
		for j in range(len(grid[0])):
			c = grid[i][j]
			newDp.append(min(c + dp[j+1], c + newDp[-1]))

		dp = newDp
	return dp[-1]
g1 = [[1,3,1],
   	[1,5,1],
   	[4,2,1]] # 7
g2 = [[1,2,3],
      [4,5,6]] #12

print('RESULT:', minPathSum(g1))