"""
	(2D Dynamic Programming) 10. Regular Expression Matching (hard)

	Link: https://leetcode.com/problems/regular-expression-matching
    
	Tags:  String, Dynamic Programming, Recursion

	Constraints:
		- 1 <= s.length <= 20
		- 1 <= p.length <= 20
		- s contains only lowercase English letters.
		- p contains only lowercase English letters, '.', and '*'.
		- It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
	======================================================================

	Submissions: 
		runtime: 38 ms, beats 97.65%
		memory: 16.37 MB, beats 76.17%
"""
'''
s5 = 'aaa'; p5 = 'ab*ac*a' # true
	0 a b * a c * a
0  t f f f f f f f
a  f t f t f f f f
a  f f f f t f t f
a  f f f f f f f t

s3 = 'ab'; p3 = '.*' # true
	0 . *
0  t f t
a  f t t
b  f f t

s7 = 'abcxxx'; p7 = '.*xxx' # true
	0 . * x x x
0  t f t f f f
a  f t t f f f
b  f f t f f f
c  f f t f f f
x  f f t t f f
x  f f t t t f
x  f f t t t t

dp final [
	[True, False, True, False, False, False],
	[False, True, True, False, False, False],
	[False, False, False, False, False, False],
	[False, False, False, False, False, False],
	[False, False, False, False, False, False],
	[False, False, False, False, False, False],
	[False, False, False, False, False, False],
	[False, False, False, False, False, False],
	[False, False, False, False, False, False],
	[False, False, False, False, False, False],
	[False, False, False, False, False, False]]

	0 a *
0  t f t
a  f t t
a  f f t

dp final [
	[True, False, False],
	[False, True, True],
	[False, False, False]]

	0 c * a * b
0  t f t f t f
a 	f f f t t f
a  f f f f t
b

dp final [
	[True, False, False, False, False, False],
	[False, False, False, False, False, False],
	[False, False, False, False, False, False],
	[False, False, False, False, False, False]]


s9 = 'aaba'; p9 = 'ab*a*c*a' # False
	0 a b * a *     c * a
0  t f f f f f     f f f
a  f t f t f t     f t f
a  f f f f t t     f t t
b  f f f f f [f]t 
a

dp final [
	[True, False, False, False, False, False, False, False, False],
	[False, True, False, True, False, True, False, True, False],
	[False, False, False, False, True, True, False, True, True],
	[False, False, False, False, False, True, False, True, False],
	[False, False, False, False, False, False, False, False, True]
]
	0 b . *
0  t f f f
a
a
b
dp final [
	[True, False, False, True],
	[False, False, False, True],
	[False, False, False, True],
	[False, False, False, True]]
'''


def isMatch(s, p):
	dp = [[True]]
	for i in range(len(p)):
		if p[i] == '*' and dp[0][i-1]:
			dp[0].append(True)
		else: 
			dp[0].append(False)

	for i in range(len(s)):
		dp.append([False])
		for j in range(len(p)):
			if s[i] == p[j] or p[j] == '.':
				if dp[i][j]:
					dp[i+1].append(True)
				else: 
					dp[i+1].append(False)
			elif p[j] == '*':
				if dp[i+1][j-1] or (p[j-1] == '.' or p[j-1] == s[i]) and (dp[i+1][j] or dp[i][j] or dp[i][j+1]):
					dp[i+1].append(True)
				else: 
					dp[i+1].append(False)

			else:
				dp[i+1].append(False)
			print('i', i, 'j', j, 'cur dp',dp[i+1][j+1])

	print('0', dp[0])
	for i in range(1, len(dp)):
		print(s[i-1], dp[i])
	

	return dp[len(s)][len(p)]
s1 = 'aa'; p1 = 'a' # false
s2 = 'aa'; p2 = 'a*' # true
s3 = 'ab'; p3 = '.*' # true
s4 = 'aab'; p4 = 'c*a*b' # true
s5 = 'aaa'; p5 = 'ab*ac*a' # true
s6 = 'abcdefg'; p6 = '.*' # true
s7 = 'abcdefgxx'; p7 = '.*xxx' # false
s8 = 'abcdefgxxx'; p8 = '.*xxx' # true
s9 = 'aaba'; p9 = 'ab*a*c*a' # False
s10 = 'aab'; p10 = 'b.*' #  False
s11 = 'a'; p11 = '.*' # True
s12 = 'ab'; p12 = '.*..c*' # True
s13 = 'a'; p13 = '..*' # True
print('RESULT: ', isMatch(s5, p5))
import unittest
import time
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
    
    def tearDown(self) -> None:
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_xxx(self):
        self.assertEqual(isMatch(s1, p1), False) 
        self.assertEqual(isMatch(s2, p2), True) 
        self.assertEqual(isMatch(s3, p3), True) 
        self.assertEqual(isMatch(s4, p4), True) 
        self.assertEqual(isMatch(s5, p5), True) 
        self.assertEqual(isMatch(s6, p6), True) 
        self.assertEqual(isMatch(s7, p7), False) 
        self.assertEqual(isMatch(s8, p8), True) 
        self.assertEqual(isMatch(s9, p9), False) 
        self.assertEqual(isMatch(s10, p10), False) 
        self.assertEqual(isMatch(s11, p11), True) 
        self.assertEqual(isMatch(s12, p12), True) 
        self.assertEqual(isMatch(s13, p13), True) 


# if __name__ == "__main__":
#     unittest.main()
'''
	0 c * a * b
0  t f t f t f
a  f f f t t f
a  f f f f t f
b  f f f f f t
0 [True, False, True, False, True, False]
a [False, False, False, True, True, False]
a [False, False, False, False, True, False]
b [False, False, False, False, False, True]

	0 b . *
0  t f f f
a 	f f f f
a
b

0 [True, False, False, True],
a [False, False, False, True],
a [False, False, False, True],
b [False, False, False, True]]
	0 . *
0  t f t
a  f t t
b  f f t
c  f f t
d
e
f
g
0 [True, False, True],
a [False, True, True],
b [False, False, True],
c [False, False, False],
d [False, False, False],
e [False, False, False],
f [False, False, False],
g [False, False, False]

	0 a a . * b
0  t f f f f f
a	f t f f f f
c	f f f f f f
b  f f f f
	0 a . * b
0  t f f f f
a  f t f t f
c  f f t t f
b  f f f t

	0 a c * b
0  t f f f f
a  f t f t f
b  f f f f t

	0 . . *
0	t f f f
a  f t f t
[True, False, False, True], 
[False, True, False, False]]
	0 . * . . c *
0  t f t f f f f
a  f t t t f f f
b  f f t t t f t


	[True, False, True, False, False, False, False],
	[False, True, True, [False], True, False, False, True],
	[False, False, True, False, True, False, False, True]]

	0 . *
0	t f t
a  f t t
dp final [
	[True, False, True],
	[False, True, False]
]


	0 a b *
0  t f f f
a  f t f t
b  f f t t
b  f f f t
b

	0 a b * a * c * a
0	t f f f f f f f f
a	f t f t f t f t f
a	f f f f t t f t t
b  f f f f
a
dp final [
	[True, False, False, False, False, False, False, False, False],
	[False, True, False, True, False, True, False, True, False],
	[False, False, False, False, True, True, False, True, True],
	[False, False, False, True, False, True, False, True, False],
	[False, False, False, False, True, True, False, True, True]]


	0 b a * b
0  t f f f f
b  f t f t f
a  f f t t f
b  f f f 
dp final [
	[True, False, False, False, False],
	[False, True, False, True, False],
	[False, False, True, False],
	[False, False, False, False, False]
]

	0 b a *
0	t f f f
b 	f t f f
a  f f t t
b  f f f f
'''