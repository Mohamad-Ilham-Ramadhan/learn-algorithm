"""
	(2D Dynamic Programming) 115. Distinct Subsequences (hard)

	Link: https://leetcode.com/problems/distinct-subsequences/
    
	Tags: String, Dynamic Programming

	Constraints:
		- 1 <= s.length, t.length <= 1000
		- s and t consist of English letters.
	======================================================================

	Submissions: 
		runtime: 348 ms, beats 81.79%
		memory: 73.80 MB, beats 40.01%
"""
'''
s1 = 'rabbbit'; t1 = 'rabbit' # 3
	r a b b b i t
r  1 1 1 1 1 1 1
a  0 1 1 1 1 1 1
b  0 0 1 2 3 3 3
b  0 0 0 2 3 3 3
i  0 0 0 0 0 3 3
t  0 0 0 0 0 0 3

s2 = 'babgbag'; t2 = 'bag' # 5
	0 b a b g b a g
0  1 1 1 1 1 1 1 1
b  0 1 1 2 2 3 3 3
a  0 0 1 1 1 1 4 4
g  0 0 0 0 1 1 1 5
'''
def numDistinct(s, t):
	dp = [[]]
	dp[0] = [1] * (len(s) + 1)
	print('dp', dp)
	for i in range(len(t)):
		dp.append([0])
		for j in range(len(s)):
			if t[i] == s[j]:
				dp[i + 1].append(dp[i + 1][j] + dp[i][j]) # dp[i + 1][j + 1]
			else:
				dp[i + 1].append( dp[i + 1][j] ) # dp[i + 1][j + 1]

	print('dp final', dp)
	return dp[len(t)][len(s)]
s1 = 'rabbbit'; t1 = 'rabbit' # 3
s2 = 'babgbag'; t2 = 'bag' # 5
print('RESULT: ', numDistinct(s2, t2))