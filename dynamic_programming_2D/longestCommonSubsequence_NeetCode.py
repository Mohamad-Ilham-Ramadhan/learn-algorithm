'''
   (2D dynamic programming) LeetCode: 1443. Longest Common Subsequence (medium)

   Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return `0`.

   A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

   For example, `"ace"` is a subsequence of `"abcde"`.
   A common subsequence of two strings is a subsequence that is common to both strings.

      

   Example 1:
      Input: text1 = "abcde", text2 = "ace" 
      Output: 3  
      Explanation: The longest common subsequence is "ace" and its length is 3.

   Example 2:
      Input: text1 = "abc", text2 = "abc"
      Output: 3
      Explanation: The longest common subsequence is "abc" and its length is 3.

   Example 3:
      Input: text1 = "abc", text2 = "def"
      Output: 0
      Explanation: There is no such common subsequence, so the result is 0.
   

   Constraints:
      - 1 <= text1.length, text2.length <= 1000
      - text1 and text2 consist of only lowercase English characters.

   Solution by NeetCode

   LeetCode submission:
      runtime: 848 ms, beats 80.42%
      memory: 42.6 MB, beats 25.55%
'''

def longestCommonSubsequence(text1, text2):
   dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

   for i in range(len(text1)-1, -1, -1):
      for j in range(len(text2) -1, -1, -1):
         if text1[i] == text2[j]: 
            dp[i][j] = 1 + dp[i + 1][j + 1]
         else: 
            dp[i][j] = max(dp[i][j+1], dp[i+1][j])
   
   return dp[0][0]

t10 = 'abcde'; t20 = 'ace' # 3
t11 = "abc"; t21 = "abc"; # 3
t12 = "abc"; t22 = "def"; # 0
t13 = 'axxdec'; t23 = 'abcdeaxxdec' # 6
'''
   ''-> 0 0 0 0 0 0 0 0 0 0 0 0 
   a -> 0 1 1 1 1 1 1 1 1 1 1 1
   x -> 0 1 1 1 1 1 
   x -> 0 1 1 1 1 1 1 2 3 3 3 3
   d -> 0 1 1 1 2 2 2 2 3 4 4 4
   e -> 0 1 1 1 2 3 3 3 3 4 5 5
   c -> 0 1 1 2 2 3 3 3 3 4 5 6
'''
t14 = 'abcdef'; t24 = 'bcdefabc' # 5
'''
   0 0 0 0 0 0 1 1 1
   0 1 1 1 1 1 1 2 2
   0 1 2 2 2 2 2 2 3
   0 1 2 3 3 3 3 3 3
   0 1 2 3 4 4 4 4 4
   0 1 2 3 4 5 5 5 5
'''
t15 = "mhunuzqrkzsnidwbun"; t25 = "szulspmhwpazoxijwbq" # 6, output: 5
t16 = "abcba"; t26 = "abcbcba"; # 5, output: 6 
# print('RESULT :', lcs3(t13, t23))

# dp = [[0] * 3] * 2
# dp = [[0,0,0],[0,0,0]]
# dp[1][1] = 1
# print('dp', dp)

import unittest
import time
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
    
    def tearDown(self) -> None:
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_xxx(self):
        self.assertEqual(longestCommonSubsequence(t10, t20), 3) 
        self.assertEqual(longestCommonSubsequence(t11, t21), 3) 
        self.assertEqual(longestCommonSubsequence(t12, t22), 0) 
        self.assertEqual(longestCommonSubsequence(t13, t23), 6) 
        self.assertEqual(longestCommonSubsequence(t14, t24), 5) 
        self.assertEqual(longestCommonSubsequence(t15, t25), 6) 
        self.assertEqual(longestCommonSubsequence(t16, t26), 5) 


if __name__ == "__main__":
    unittest.main()