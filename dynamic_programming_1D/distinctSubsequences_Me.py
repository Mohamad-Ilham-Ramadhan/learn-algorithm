"""
	(1D Dynamic Programming) 115. Distinct Subsequences (hard)

	Link: https://leetcode.com/problems/distinct-subsequences/
    
	Tags: String, Dynamic Programming

	Constraints:
		- 1 <= s.length, t.length <= 1000
		- s and t consist of English letters.
	======================================================================

	Submissions: 
		runtime: 222 ms, beats 90.92%
		memory: 16.63 MB, beats 89.95%
"""
'''
s1 = 'rabbbit'; t1 = 'rabbit' # 3
	r a b b b i t
r  1 1 1 1 1 1 1
a  0 1 1 1 1 1 1
b  0 0 1 2 3 3 3
b  0 0 0 1 3 3 3
i  0 0 0 0 0 3 3
t  0 0 0 0 0 0 3

s2 = 'babgbag'; t2 = 'bag' # 5
	0 b a b g b a g
0  1 1 1 1 1 1 1 1
b  0 1 1 2 2 3 3 3
a  0 0 1 1 1 1 4 4
g  0 0 0 0 1 1 1 5
'''
# 1 row of 2D array, 2D dynamic programming
def numDistinct(s, t):
	dp = [1] * (len(s) + 1)
	for i in range(len(t)):
		newDp = [0]
		for j in range(len(s)):
			if t[i] == s[j]:
				newDp.append( newDp[j] + dp[j] )
			else:
				newDp.append( newDp[j])
		dp = newDp 

	return dp[len(s)]

s1 = 'rabbbit'; t1 = 'rabbit' # 3
s2 = 'babgbag'; t2 = 'bag' # 5
print('RESULT: ', numDistinct(s2, t2))