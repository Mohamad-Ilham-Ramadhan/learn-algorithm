"""
	(2D Dynamic Programming) 1277. Count Square Submatrices with All Ones (medium)

	Link: https://leetcode.com/problems/count-square-submatrices-with-all-ones/
    
	Tags: Dynamic Programming,

	Constraints:
		- 1 <= arr.length <= 300
		- 1 <= arr[0].length <= 300
		- 0 <= arr[i][j] <= 1
	======================================================================

	Submissions: 
		# time O(n^3), space O(n * m)
			runtime: 6826 ms, beats 5.12%
			memory: 80.16 MB, beats 80.16%
		# time: O(n * m), space O(1)
			runtime: 506 ms, beats 85.47%
			memory: 18.76 MB, beats 50.00%
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
	[[1,1,1,1,0],
	 [1,2,2,2,1],
	 [1,2,3,3,0],
	 [1,2,3,4,0],] # 31
ans = 17
dp [[1,1,0,1,1]],
	 [1,2,1,1,1],
	 [1,2,2,1,0],
	 [1,1,1,0,1]]

[[0,1,1,1],
 [1,1,2,2],
 [0,1,2,3]]
'''

# time complexity: O(n * m), space complexity is O(1) 
def faster(matrix):
	ans = 0
	for j in range(len(matrix[0])):
		ans += matrix[0][j]
	
	for i in range(1, len(matrix)):
		for j in range(len(matrix[0])):
			if j >= 1 and matrix[i][j] > 0:
				m = min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1])
				if m > 0:
					matrix[i][j] += m
			ans += matrix[i][j]
	print('matrix', matrix)
	return ans
m1 = [[0,1,1,1],[1,1,1,1],[0,1,1,1]] # 15
m2 = [[1,0,1],[1,1,0],[1,1,0]] # 7
m3 = [[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,0],[1,1,1,1,0]] # 31
'''
	[[1,1,1,1,0],
	 [1,1,1,1,1],
	 [1,1,1,1,0],
	 [1,1,1,1,0]] # 31
	
	[[1,1,1,1,0], 4
	 [1,2,2,2,1], 8
	 [1,2,3,3,1], 10
	 [1,2,3,4,1]] 11 # 33
'''
# countSquares(m3)
print('result: ', faster(m3))