"""
	(2D Dynamic Programming) 115. Distinct Subsequences (hard)

	Link: https://leetcode.com/problems/distinct-subsequences/
    
	Tags: String, Dynamic Programming

	Constraints:
		- 1 <= s.length, t.length <= 1000
		- s and t consist of English letters.
	======================================================================

	Submissions: 
		NeetCode's solution
			runtime: 711 ms, beats 26.77%
			memory: 158.90 MB, beats 25.42%
"""

def numDistinct(s, t):
	cache = {}

	def dfs(i, j):
		if j == len(t):
			return 1
		if i == len(s):
			return 0
		if (i, j) in cache:
			return [cache[(i, j)]]
		
		if s[i] == t[j]:
			cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
		else: 
			cache[(i, j)] = dfs(i + 1, j)
		return cache[(i, j)]
	
	return dfs(0, 0)
s1 = 'rabbbit'; t1 = 'rabbit' # 3
s2 = 'babgbag'; t2 = 'bag' # 5
print('RESULT: ', numDistinct(s2, t2))