"""
	(1D dynamic programming) Leetcode: 119. Pascal's Triangle II (easy)

	Link: https://leetcode.com/problems/pascals-triangle-ii/
    
	Tags: Array, Dynamic programming

	Constraints:
		- 1 <= n <= 33
	======================================================================

	Submissions: 
			runtime: 47 ms, beats 43.52%
			memory: 16.23 MB, beats 70.53%
"""
def getRow(rowIndex):
	if rowIndex == 0: [1]
	dp = [1] 
	
	for i in range(1, rowIndex+1):
		newDp = [1]
		for j in range(1, i):
			newDp.append(dp[j-1] + dp[j])
		newDp.append(1)
		dp = newDp

	return dp

print('RESULT: ', getRow(3))

