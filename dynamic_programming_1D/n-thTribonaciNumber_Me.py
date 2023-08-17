"""
	(1D Dynamic Programming) leetcode: 1137. N-th Tribonacci Number (easy)

	Link: https://leetcode.com/problems/n-th-tribonacci-number/
    
	Tags: Dynamic Programming,

	Constraints:
		- 0 <= n <= 37
		- The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
	======================================================================

	Submissions: 
		runtime: 41 ms, beats 65.40%
		memory: 16.11 MB, beats 91.96%
"""

def tribonacci(n):
	dp = []
	dp.append(0)
	dp.append(1)
	dp.append(1)
	if n <= 2: return dp[n]

	for i in range(3, n+1):
		dp.append( dp[i-3] + dp[i-2] + dp[i-1] )
	
	return dp[n]
