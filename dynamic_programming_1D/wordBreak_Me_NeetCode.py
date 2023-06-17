'''
   Leetcode: 139. Word Break (medium)

   Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

   Note that the same word in the dictionary may be reused multiple times in the segmentation.

   

   Example 1:
      Input: s = "leetcode", wordDict = ["leet","code"]
      Output: true
      Explanation: Return true because "leetcode" can be segmented as "leet code".

   Example 2:
      Input: s = "applepenapple", wordDict = ["apple","pen"]
      Output: true
      Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
      Note that you are allowed to reuse a dictionary word.

   Example 3:
      Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
      Output: false
   
      
   Constraints:
      - 1 <= s.length <= 300
      - 1 <= wordDict.length <= 1000
      - 1 <= wordDict[i].length <= 20
      - s and wordDict[i] consist of only lowercase English letters.
      - All the strings of wordDict are unique.

   Solution by neetcode and code implementation by me:
      implementing Neetcode's solution of dynamic programming
      
   Leetcode submission: 
      Runtime: 44 ms, beats 87.29%
      Memory: 16.4 MB, beats 48.60%
'''

# implement NeetCode's explanation
def wordBreak4(s, wordDict):
  dp = [False for i in range(len(s) + 1)]
  dp[len(s)] = True
  # print('dp', len(dp), 's', len(s))

  for i in range(len(s) - 1, -1, -1): 
    char = s[i]
    for w in wordDict:
      if char == w[0] and i + len(w) <= len(s) and s[i: i + len(w)] == w and dp[i + len(w)]:
        dp[i] = True
    # print('char', char)
  
  return dp[0]
