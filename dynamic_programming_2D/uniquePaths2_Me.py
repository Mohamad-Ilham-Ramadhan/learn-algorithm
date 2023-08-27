"""
	(2D Dynamic Programming) 63. Unique Paths II(medium)

	Link: https://leetcode.com/problems/unique-paths-ii/
    
	Constraints:
	- m == obstacleGrid.length
	- n == obstacleGrid[i].length
	- 1 <= m, n <= 100
	- obstacleGrid[i][j] is 0 or 1.
   
	Tags: Array, Dynamic Programming, Matrix
	======================================================================
   
   Submission:
		runtime: 43 ms, beats 89.00%
      memory: 16.50 MB, beats 53.31%

"""

'''
g3 = [
   [0,1,0,0],
	[0,0,0,1],
	[0,0,0,0],
	[0,1,0,0]
] # 6
0	[0 0 0 0 0]
1  [0,1,0,0,0],
2	[0,1,1,1,0],
3	[0,1,2,3,3],
4	[0,1,0,3,6]
'''
def uniquePathsWithObstacles(obstacleGrid):
	g = obstacleGrid
	if g[0][0] == 1: 
		return 0
	
	dp = [0] * (len(g[0]) + 1)
	dp[1] = 1
	for i in range(len(g)):
		newDp = [0]
		for j in range(len(g[0])): 
			if g[i][j] == 1:  # if obstacle
				newDp.append(-1)
			else: # if path
				if dp[j+1] == -1: 
					newDp.append(newDp[-1])
				elif newDp[-1] == -1: 
					newDp.append(dp[j+1])
				else: 
					newDp.append(dp[j+1] + newDp[-1])
		print('newDp', newDp)
		dp = newDp
	return dp[-1] if dp[-1] >= 0 else 0

g1 = [
   [0,0,0],
	[0,1,0],
	[0,0,0]
] # 2
g2 = [
	[0,1],
	[0,0]
] # 1
g3 = [
   [0,1,0,0],
	[0,0,0,1],
	[0,0,0,0],
	[0,1,0,0]
] # 6
g4 = [[0,0],[0,1]] # 0
print('RESULT:', uniquePathsWithObstacles(g3))