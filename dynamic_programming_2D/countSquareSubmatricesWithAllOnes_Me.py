"""
	(1D Dynamic Programming) 1277. Count Square Submatrices with All Ones (medium)

	Link: https://leetcode.com/problems/count-square-submatrices-with-all-ones/
    
	Tags: Dynamic Programming,

	Constraints:
		- 1 <= arr.length <= 300
		- 1 <= arr[0].length <= 300
		- 0 <= arr[i][j] <= 1
	======================================================================

	Submissions: 
		runtime: 6826 ms, beats 5.12%
		memory: 80.16 MB, beats 80.16%
"""

# slow O(n^3)
def countSquares(matrix):
	ans = 0
	dp = []
	for i in range(len(matrix)):
		dp.append([]) 
		row = matrix[i]
		for j in range(len(row)):
			cell = row[j]
			if cell:
				ans += 1
			else:
				if i-1 >= 0:
					dp[i-1][j] = False
				if i-1 >= 0 and j-1 >= 0:
					dp[i-1][j-1] = False 
				if j-1 >= 0:
					dp[i][j-1] = False
			dp[i].append(bool(cell))

	print('dp', dp, 'ans', ans)
	k = 2 # submatrix length
	while k <= len(matrix) and len(matrix[0]):
		total = 0
		for i in range(len(matrix) - (k-1)):
			row = matrix[i]
			for j in range(len(row) - (k-1)):
				cell = dp[i][j]
				print('k', k, 'i', i, 'j', j, 'cell', cell)
				if cell:
					ans += 1
					total += 1
				else:
					if i-1 >= 0:
						dp[i-1][j] = False
					if i-1 >= 0 and j-1 >= 0:
						dp[i-1][j-1] = False 
					if j-1 >= 0:
						dp[i][j-1] = False
		print('k', k, 'dp', dp.copy(), 'total', total)
		k += 1
	print('dp final', dp, 'ans', ans)
	return ans

'''
	[[1,0,1,1,1],
	 [1,1,1,1,1],
	 [1,1,1,1,0],
	 [1,1,1,0,1],]
ans = 17
dp [[f,f,t,t,t],
	 [t,t,t,f,f],
	 [t,t,f,f,f],
	 [t,t,f,f,t]]
'''
m3 = [[1,0,1,1,1],
  	[1,1,1,1,1],
	 [1,1,1,1,0],
	 [1,1,1,0,1]] # 25
countSquares(m3)