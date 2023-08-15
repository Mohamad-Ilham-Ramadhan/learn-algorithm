"""
	(1D dynamic programming) Leetcode: 338. Counting Bits (easy)

	Link: https://leetcode.com/problems/counting-bits/
    
	Tags: Dynamic programming, Bit manipulation

	Constraints:
		- 1 <= n <= 10^5
	======================================================================

	Submissions: 
		#1 my math (dynamic programming)
			runtime: 99 ms, beats 51.56%
			memory: 23.02 MB, beats 68.03%
		#2 python built-in bit_count
			runtime: 65 ms, beats 96.90%
			memory: 23.14 MB, beats 27.16%
"""
# O(n)
import math
def countBits(n):
	dp = []
	dp.append(0)
	for i in range(1, n+1):
		dp.append(dp[i - pow(2, math.floor(math.log2(i)))] + 1)
	return dp
print('RESULT: ', countBits(5))

# using builtin int.bit_count
def builtin(n):
	dp = []
	for i in range(n+1): 
		dp.append(int.bit_count(i))
	return dp


print('RESULT: ', builtin(5))
