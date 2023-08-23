"""
	(2D Dynamic Programming) 329. Longest Increasing Path in a Matrix (hard)

	Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
    
	Tags: Array, Dynamic Programming, Depth-first search, breadth-first search, graph, topological sort, memoization, matrix

	Constraints:
		- m == matrix.length
		- n == matrix[i].length
		- 1 <= m, n <= 200
		- 0 <= matrix[i][j] <= 2^31 - 1
	======================================================================

	Submissions: 
		runtime: 350 ms, beats 85.43%
		memory: 17.45 MB, beats 77.27%
"""
'''
	[5 4 3]
	[9 1 2]
	[9 0 9]

dp []
	[]
   []
'''
def longestIncreasingPath(matrix):
	dp = [] # 2D array

	for i in range(len(matrix)):
		dp.append([])
		for j in range(len(matrix[0])):
			dp[i].append(0)
	
	# print('dp initial', dp)
	def dfs(n, x, y, vis): 
		print('y', y, 'x', x, 'n', n)
		if dp[y][x]:
			return dp[y][x]

		vis.add((x,y))
		'''
			[5 4 3]
			[9 1 2]
			[9 0 9]

		'''
		# 4 direction
		top, right, bottom, left = 0,0,0,0
		if y-1 >= 0 and (x,y-1) not in vis and matrix[y-1][x] > n: # top
			top = dfs(matrix[y-1][x], x, y-1, vis)

		if x + 1 < len(matrix[0]) and (x+1, y) not in vis and matrix[y][x+1] > n: # right
			right = dfs(matrix[y][x+1], x+1, y, vis)

		if y+1 < len(matrix) and (x, y+1) not in vis and matrix[y+1][x] > n: # bottom 
			bottom = dfs(matrix[y+1][x], x, y+1, vis)

		if x-1 >= 0 and (x-1, y) not in vis and matrix[y][x-1] > n: # left
			left = dfs(matrix[y][x-1], x-1, y, vis)

		# print('dfs curretn dp', dp.copy())
		# print('y', y, 'x', x, 'top', top, 'right', right, 'bottom', bottom, 'left', left)
		dp[y][x] = max(top, right, bottom, left) + 1
		vis.remove((x,y))
      
		if top == 0 and right == 0 and bottom == 0 and left == 0: 
			return 1
		else: 
			return dp[y][x]
	ans = 1
	for y in range(len(matrix)):
		for x in range(len(matrix[0])):
			ans = max(ans, dfs(matrix[y][x], x, y, set()) )
			# print('y', y, 'x', x, 'ans', ans)
			# print('current dp', dp.copy())
	return ans

m1 = [[5, 4, 3],
		[9, 1, 2],
		[9, 0, 9],]
m2 = [[9, 9, 4],
      [6, 6, 8],
		[2, 1, 1]]
m3 = [[3, 4, 5],
      [3, 2, 6],
		[2, 2, 1]]
print('RESULT: ', longestIncreasingPath(m1) )