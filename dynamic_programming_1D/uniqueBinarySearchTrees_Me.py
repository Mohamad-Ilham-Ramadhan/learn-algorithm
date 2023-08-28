"""
	(1D Dynamic Programming) 96. Unique Binary Search Trees (medium)

	Link: https://leetcode.com/problems/unique-binary-search-trees
    
	Constraints:
		- 1 <= n <= 19
	
	Tags: Math, Dynamic Programming, Tree, Binary Search Tree, Binary Tree
	======================================================================
   
   Submission:
		runtime: 31 ms, beats 94.23%
      memory: 16.14 MB, beats 90.76%

"""

'''
1 2 5 14 42 132 429 1430
'''
import math
def numTrees(n):
	dp = [1]
	for i in range(1, n+1):
		dp.append(0)
		h = i // 2
		total = 0
		j = 0
		while j < h: 
			total += (dp[i - j - 1] * dp[j]) * 2
			j += 1
			print('i', i, 'while total', total)
		if i % 2: # current n is odd
			total += dp[i - j - 1] * dp[i - j - 1]
		print('i', i, 'total', total)
		dp[i] = total 
	print('c dp', dp.copy())
	return dp[n]
n1=1 # 1
n2=2 # 2
n3=3 # 5
n4=4 # 14 
n5=5 # 42 
n6=6 # 132 
n7=7 # 429 
n8=8 # 1430 #
n9=19 # 1767263190
print('RESULT: ', numTrees(19))
'''
	n8
	7 = 429 * 2 = 858
	6 = 132 * 2 = 264
	5 = (42 * 2) * 2 = 168
	4 = (14 * 5) * 2 = 140
'''