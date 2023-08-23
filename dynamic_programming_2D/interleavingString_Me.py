"""
	(2D Dynamic Programming) 97. Interleaving String (medium)

	Link: https://leetcode.com/problems/interleaving-string/
    
	Tags: String, Dynamic Programming

	Constraints:
		- 0 <= s1.length, s2.length <= 100
		- 0 <= s3.length <= 200
		- s1, s2, and s3 consist of lowercase English letters.
	======================================================================

	Submissions: 
      Tushar Roy's intuition
         runtime: 51 ms, beats 51.56%
         memory: 16.46 MB, beats 79.58%
"""
'''
s11 = 'aabcc'; s21 = 'dbbca'; s31 = 'aadbbcbcac' # True

	aadbbcbcac
	0 d b b c a
0  t f f f f f
a  t f f f f f
a  t t t t t f
b  f t t f f f
c  f f t t t t
c  f f t t f t

s12 = 'aabcc'; s22 = 'dbbca'; s32 = 'aadbbbaccc' # False
aadbbbaccc
	0 a a b c c
0  t t t f f f
d  f 
b
b
c
a
'''
def isInterleave(s1, s2, s3):
	if len(s3) != (len(s1) + len(s2)): return False

	dp = [[True]]

	for i in range(len(s1)):
		dp[0].append(True if s1[i] == s3[i] and dp[0][i] else False)

	print('dp initial', dp)
	for i in range(len(s2)):
		c2 = s2[i]
		dp.append([True if c2 == s3[i] and dp[i][0] else False])
		
		for j in range(len(s1)):
			c1 = s1[j]
			c3 = s3[i + j + 1]
			if c1 == c3 and dp[i + 1][j]: 
				dp[i + 1].append( True )
			elif c2 == c3 and dp[i][j + 1]: 
				dp[i + 1].append(True)
			else:
				dp[i + 1].append( False )

			print('dp 0', dp[i+1][0], 'c1', c1, 'c2', c2, 'c3', c3, 'dp[i+1][j+1]', dp[i+1][j+1])
	print('dp final', dp)
	return dp[len(s2)][len(s1)]



   
s11 = 'aabcc'; s21 = 'dbbca'; s31 = 'aadbbcbcac' # True
s12 = 'aabcc'; s22 = 'dbbca'; s32 = 'aadbbbaccc' # False
s13 = ''; s23 = ''; s33 = '' # True
s14 = 'aab'; s24 = 'cca'; s34 = 'acacab' # True
s15 = 'a'; s25 = 'b'; s35 = 'aba' # False
s16 = 'db'; s26 = 'b'; s36 = 'cbb' # False
s17 = ''; s27 = 'abc'; s37 = 'abc' # True
s18 = 'ab'; s28 = 'ccd'; s38 = 'acdab' # False
'''
s18 = 'ab'; s28 = 'ccd'; s38 = 'acdab' # False

	ac dab
	0 a b
0  t t f
c  f t f
c  t
d
dp final [
	[True, True, False],
	[False, True, False],
	[True, False, False],
	[True, True, True]]
'''
print('RESULT: ', isInterleave(s18, s28, s38))