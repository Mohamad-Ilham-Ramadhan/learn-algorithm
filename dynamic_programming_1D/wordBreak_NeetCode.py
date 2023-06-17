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

  Solution by NeetCode:
  
  Leetcode submission:
    runtime: 62 ms, beats 20.38% 
    memory: 16.3 MB, beats 74.78%
'''
from datetime import datetime 

def wordBreak(s, wordDict):
  dp = [False] * (len(s) + 1)
  dp[len(s)] = True 
  
  for i in range(len(s) -1, -1, -1):
    for w in wordDict:
      if (i + len(w)) <= len(s) and s[i: i + len(w)] == w: 
        dp[i] = dp[i + len(w)]
      if dp[i]:
        break 
  
  return dp[0]

s1 = 'leetcode'; wd1 = ['leet', 'code']; # expect: true
s2 = 'applepenapple'; wd2 = ['apple', 'pen']; # expect: true
x2 = 'applepenapple'; xd2 = ['apple', 'ap', 'pp', 'pen'] # expect: true
s3 = 'catsandog'; wd3 = ['cats', 'dog', 'sand', 'and', 'cat']; # expect: false
s4 = 'catandcats'; wd4 = ['cat', 'and', 'cats']; # expect: true
s5 = 'catsandcat'; wd5 = ['cat', 'and', 'cats']; # expect: true
s6 = 'ab'; wd6 = ['a', 'b'] # expect: true
s7 = 'bb'; wd7 = ['a', 'b', 'bb', 'bbb', 'bbbb'] # expect: true, output: false
s8 = 'cars'; wd8 = ['car', 'ca', 'rs']
s9 = 'a'; wd9 = ['b']; # expect: false,
s10 = 'aaaaaaa'; wd10 = ["aaaa","aa"]; # expect: false, output: true
'''
  dp[7] = false 
  dp[6] = false 
  dp[5] = true | dp[4] = true | dp[3] = true | dp[2] = true | dp[1] = true | dp[0] = true
'''
s11 = 'aaaaaaa'; wd11 = ['aaaa', 'aaa'] # expect: true, output: false
s12 = 'catscat'; wd12 = ['cat', 'cats'] # expect: true
s13 = 'ccbb'; wd13 = ['bc', 'cb']
s14 = "catsandogcat"; wd14 = ["cats","dog","sand","and","cat","an"] # expect: True, output: false
s15 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wd15 = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

start = datetime.timestamp(datetime.now())
print('result: ', wordBreak(s15, wd15))
print('runtime: ', start - datetime.timestamp(datetime.now()))
