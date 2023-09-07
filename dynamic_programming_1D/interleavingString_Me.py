"""
	(1D dynamic programming) 97. Interleaving String (medium)

	Link: https://leetcode.com/problems/interleaving-string/
    
	Tags:  String, String Matching

	Constraints:
		- 0 <= s1.length, s2.length <= 100
		- 0 <= s3.length <= 200
		- s1, s2, and s3 consist of lowercase English letters.
	======================================================================

	Submissions: 
		runtime: 45 ms, beats 70.97%
		memory: 16.35 MB, beats 89.13%
"""
"""  1 2 3 4 5 6 7 8 9 10
	  a a d b b c b c a c

	0 a a b c c
0  t t t f f f
d  f f t t f f
b  f f t t t f
b  f f t f t t
c  f f t t t f
a  f f f f t t
[True, True, True, False, False, False],
[False, False, True, True, False, False],
[False, False, True, True, True, False],
[False, False, True, False, True, True],
[False, False, True, True, True, False],
[False, False, False, False, True, True]]
"""


def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    dp = []
    dp.append(True)
    for i in range(len(s1)):
        dp.append(True if s1[i] == s3[i] and dp[i] else False)

    for i in range(len(s2)):
        newDp = []
        newDp.append(True if dp[0] and s3[i] == s2[i] else False)
        for j in range(len(s1)):
            c3 = s3[i + j + 1]
            if (dp[j + 1] and c3 == s2[i]) or (newDp[j] and c3 == s1[j]):
                newDp.append(True)
            else:
                newDp.append(False)
        dp = newDp

    return dp[-1]


s11 = "aabcc"
s12 = "dbbca"
s13 = "aadbbcbcac"  # true
s12 = ""
s22 = ""
s23 = "a"  # false
print("RESULT: ", isInterleave(s11, s12, s13))
