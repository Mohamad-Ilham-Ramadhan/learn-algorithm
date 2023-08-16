"""
	(two pointers) Leetcode: 392. Is Subsequence (easy)

	Link: https://leetcode.com/problems/is-subsequence/
    
	Tags: Two pointers, String, Dynamic Programming

	Constraints:
		- 1 <= n <= 10^5
	======================================================================

	Submissions: 
		runtime: 53 ms, beats 21.11%
		memory: 16.3 MB, beats 62.89%
"""

def isSubsequence(s, t):
	i = 0
	j = 0
	while j < len(t) and i < len(s):
		sc = s[i]
		tc = t[j]
		if sc == tc: 
			print('sc', sc, 'tc', tc)
			i += 1
			j += 1
		else: 
			j += 1
	if i == len(s):
		return True
	return False 

s1 = 'abc'; t1 = 'ahbgdc'
s2 = 'axc'; t2 = 'ahbgdc'
isSubsequence(s2, 'ahbgdc')