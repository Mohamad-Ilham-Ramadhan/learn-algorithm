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

   Solution by myself:

   LeetCode submission:
      #1 (time complexity and space complexity O(n * m))
         Runtime: 919 ms, 55.28%
         Memory: 42.5 MB, 33,75%
      #2 (time complexity O(n * m) and space complexity O(m))
         Runtime: 636 ms, 96.51%
         Memory: 16 MB, 90.84%
'''

# attempt #1 (fail)
from collections import deque
def longestCommonSubsequence(text1, text2):
   map = {} 
   for i in range(len(text2)): 
      c = text2[i]
      if c in map: 
         map[c].append(i)
      else: 
         map[c] = [i]
   
   si = 0 # last subsequence start index
   ls = 0 # length of sub
   pi = 0 # last char index in sub (text2),
   queue = deque([])

   # initialize first char 
   for i in range(len(text1)): 
      if text1[i] in map: 
         queue.append([i, map[text1[i]][0] ])
         break

   # print('queue', queue)
   # [start, pi] = queue.pop()
   # print('start', start, 'pi', pi)
   # return
   while len(queue) > 0:
      curLs = 1
      [start, pi] = queue.pop()
      print('START', start, text1[start], '\n')
      for i in range(start + 1, len(text1)):
         c = text1[i]
         print('char', c)
         if c in map:
            for mi in map[c]: 
               print('map char', text2[mi], mi, pi, map[text1[start]][0])
               if mi > pi: 
                  print()
                  curLs += 1
                  pi = mi
                  break
               if mi < map[text1[start]][0]:
                  print('add to queue, possible longest sub', mi, text2[mi])
                  queue.appendleft([i, mi])
      if curLs == len(text1) or curLs == len(text2):
         return curLs
      print('====',ls, curLs, '====')
      ls = max(ls, curLs)
   
   return ls

# after understanding Hint from leetcode. Time complexity and space complexity is O(n * m)
def longestCommonSubsequence2(text1, text2):
   text1 = ' ' + text1
   text2 = ' ' + text2
   t1l = len(text1)
   t2l = len(text2)
   # dp = [[0] * t2l] * t1l
   dp = []
   for i in range(t1l):
      dp.append([])
      for j in range(t2l):
         dp[i].append(0)
   # print('dp before', dp, text1, text2)
   for i in range(1, t1l): 
      ci = text1[i]
      for j in range(1, t2l):
         cj = text2[j]
         # print('dp[0]', dp[0])
         if ci == cj:
            dp[i][j] = 1 + dp[i-1][j-1]
            # print('match', i, ci, j, cj)
         else: 
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

   return dp[t1l-1][t2l-1]

# Time complexity O(n * m) and space complexity is O(m)
def lcs3(text1, text2):
   text1 = ' ' + text1
   text2 = ' ' + text2
   t1l = len(text1)
   t2l = len(text2)
   # dp = [[0] * t2l] * t1l
   dp = [] # prev dp (in 2D this is prev row)
   for i in range(t2l):
      dp.append(0)
   # print('dp before', dp, text1, text2)
   for i in range(1, t1l): 
      ci = text1[i]
      currentSub = [0]
      for j in range(1, t2l):
         cj = text2[j]
         # print('dp[0]', dp[0])
         if ci == cj:
            # dp[i][j] = 1 + dp[i-1][j-1]
            currentSub.append(1 + dp[j-1])
            # print('match', i, ci, j, cj)
         else: 
            # dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            currentSub.append(max(currentSub[j-1], dp[j]))
      dp = currentSub

   return currentSub[t2l-1]
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
        self.assertEqual(lcs3(t10, t20), 3) 
        self.assertEqual(lcs3(t11, t21), 3) 
        self.assertEqual(lcs3(t12, t22), 0) 
        self.assertEqual(lcs3(t13, t23), 6) 
        self.assertEqual(lcs3(t14, t24), 5) 
        self.assertEqual(lcs3(t15, t25), 6) 
        self.assertEqual(lcs3(t16, t26), 5) 


if __name__ == "__main__":
    unittest.main()