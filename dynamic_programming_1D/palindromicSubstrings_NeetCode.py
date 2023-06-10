"""
  Leetcode: 647. Palindromic Substrings (medium)

  Given a string `s`, return the number of palindromic substrings in it.

  A string is a palindrome when it reads the same backward as forward.

  A substring is a contiguous sequence of characters within the string.
  

  Example 1:
    Input: s = "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".

  Example 2:
    Input: s = "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
  

  Constraints:
    - 1 <= s.length <= 1000
    - s consists of lowercase English letters.

  solution by NeetCode

  Leetcode submission:
    Runtime: 139 ms, beats 59.18%
    Memory: 16.1 MB, beats 76.94%
"""

def countSubstrings(s):
  res = 0

  for i in range(len(s)):
    res += countPali(s, i, i)
    res += countPali(s, i, i + 1)
  return res

def countPali(s, l, r):
  res = 0
  while l >= 0 and r < len(s) and s[l] == s[r]:
    res += 1
    l -= 1
    r += 1
  return res


print('RESULT: ', countSubstrings('caaac'))