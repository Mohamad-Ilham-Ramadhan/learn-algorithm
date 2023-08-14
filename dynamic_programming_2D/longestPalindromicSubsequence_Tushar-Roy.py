'''
    (2D dynamic programming) Leetcode: 516. Longest Palindromic Subsequence (medium)

    Link: https://leetcode.com/problems/longest-palindromic-subsequence/

    Tags: 

    Constraints:
        - 1 <= s.length <= 1000
        - s consists only of lowercase English letters.

    ======================================================================

    Submissions: 
        runtime: 1156 ms, beats 77.18%
        memory: 32.79 MB, beats 86.34%
        


'''

'''
    Input: s = "bbbab"
    Output: 4
    Explanation: One possible longest palindromic subsequence is "bbbb".

    Input: s = "cbbd"
    Output: 2
    Explanation: One possible longest palindromic subsequence is "bb".
'''

# concept/idea by Tushar Roy, coded by me
def longestPalindromeSubseq(s): 
	dp = [[0] * len(s) for i in range(len(s))] 
	i = 0
	j = 0
	while i < len(s):
		dp[i][j] = 1
		i += 1
		j += 1

	for i in range(1, len(s)):
		l = i + 1 # length of palindrome
		x = i
		for j in range(len(s) - i): 
			li = (x-l) + 1 # left/start index of palindrome
			# print('i', i, 'x', x, 'j', j, 'length', l, 'li', li)
			# print('palindrome', s[li:x+1])
			if s[li] != s[x]:
				dp[j][x] = max(dp[j][x-1], dp[j+1][x])
			else: # if the left and right equal
				dp[j][x] = 2 + dp[j+1][x-1]
			x += 1
    
	print('dp', dp)
	return dp[0][len(s)-1]
	'''
    dp [
    [1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4],
    [0, 0, 1, 2, 3],
    [0, 0, 0, 1, 2],
    [0, 0, 0, 0, 1]]
	'''
s1 = 'bbbab' # 4
s3 = 'abcda' # 3 (aca)
s4 = 'dsdcagac' # 5 (cagac)
s5 = 'axdmmux' # 4
s6 = 'axdmzymux' # 5
s7 = 'dscdcagacc' # 7 (ccagacc)
s8 = 'dscdcagcac' # 5 (cc[ag]cc)
s9 = 'axdmzymuxuyxz' # 7
s10 = 'abababaaba' # 9 (fail: 10)
longestPalindromeSubseq(s10)
'''
  a b a b a b a a b a
  0 1 2 3 4 5 6 7 8 9
0 1 1 3 3
1   1 1 3 3
2     1 1 3 3
3       1 1 3 3
4         1 1 3 
5           1 1 2
6             1 2 2
7               1 1 3
8                 1 1 
9                   1 

dp [
       a  b  a  b  a  b  a  a  b  a
       0  1  2  3  4  5  6  7  8  9
	0 [1, 1, 3, 3, 5, 5, 7, 7, 8, 10],
	1 [0, 1, 1, 3, 3, 5, 5, 5, 8, 8],
	2 [0, 0, 1, 1, 3, 3, 5, 5, 6, 8],
	3 [0, 0, 0, 1, 1, 3, 3, 3, 6, 6],
	4 [0, 0, 0, 0, 1, 1, 3, 3, 4, 6],
	5 [0, 0, 0, 0, 0, 1, 1, 2, 4, 4],
	6 [0, 0, 0, 0, 0, 0, 1, 2, 2, 3],
	7 [0, 0, 0, 0, 0, 0, 0, 1, 1, 3],
	8 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
	9 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
	]


		b a x a b
		0 1 2 3 4
	0 1 1 1 3 5
	1   1 1 3 3
	2     1 1 1
	3       1 1
	4         1


		b b b b b
		0 1 2 3 4
	0 1 2 3 4 5
	1   1 2 3 4
	2     1 2 3
	3       1 2
	4         1

		b b x a b
		0 1 2 3 4
	0 1 2 2 2 3
	1   1 1 1 3
	2     1 1 1
	3       1 1
	4         1
	
    b b b a b
    0 1 2 3 4
  
  0 1 2 3 3 4
  1   1 2 2 3
  2     1 1 3  
  3       1 1 
  4         1

     b b b b b
     0 1 2 3 4
   0 1 2 3 4 5 
   1   1 2 3 4 
   2     1 2 3
   3       1 2
   4         1

     d s d c a g a c
     0 1 2 3 4 5 6 7
   0 1 1 3 3 3 3 3 5
   1   1 1 1 1 1 3 5
   2     1 1 1 1 3 5
   3       1 1 1 3 5
   4         1 1 3 3 
   5           1 1 1
   6             1 1
   7               1 

    dscdcagacc
    ans = 7
    lidIndex = [9, 8, 7]
    d {c: [9, 8, 4], a: [7,5], g: [6], d: [3]}
    g = 6

    dscdcagcac
          0,1,2,3,4,5,6,7,8,9
          d s c d c a g c a c
    dp = [3,3,3,3,4,4,5,3,4,4]

    axdmzymux
          a x d m z y m u x
    dp = [1,2,3,4,5,5,4,1,2]
    r = [8]
    cp = 4

          a x d m z y m u x u y x z
    dp = [1,1,3,3,5,7,5,5,7,6,1,2,2]
    r = [x,z,u]




'''