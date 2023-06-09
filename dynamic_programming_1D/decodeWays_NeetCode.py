'''
    LeetCode: 91. Decode Ways (medium)

    A message containing letters from `A-Z` can be encoded into numbers using the following mapping:

        'A' -> "1"
        'B' -> "2"
        ...
        'Z' -> "26"

    To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, `"11106"` can be mapped into:

        - "AAJF" with the grouping (1 1 10 6)
        - "KJF" with the grouping (11 10 6)

    Note that the grouping `(1 11 06)` is invalid because `"06"` cannot be mapped into `'F'` since `"6"` is different from `"06"`.

    Given a string `s` containing only digits, return the number of ways to decode it.

    The test cases are generated so that the answer fits in a 32-bit integer.

    

    Example 1:
        Input: s = "12"
        Output: 2
        Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

    Example 2:
        Input: s = "226"
        Output: 3
        Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

    Example 3:
        Input: s = "06"
        Output: 0
        Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
    

    Constraints:
        - 1 <= s.length <= 100
        - s contains only digits and may contain leading zero(s).

    Solution by neetcode
    
    LeetCode submission:
        # recursive
            Runtime: 49 ms, beats 50.84%
            Memory: 16.6 MB, beats 9.51%

        # iterative 
            Runtime: 48 ms, beats 56.36%
            Memory: 16.2 MB, beats 74.35%
  
'''

def numDecodings(s):
    # recursive dp 
    # dp = { len(s) : 1}
    # # print('dp', dp, type(dp))
    # def dfs(i):
    #     if i in dp: 
    #         return dp[i]
    #     if s[i] == '0':
    #         return 0

    #     res = dfs(i + 1)

    #     if (i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] in '0123456')):
    #         res += dfs(i + 2)
        
    #     dp[i] = res 
    #     return res
    
    # return dfs(0)

    # iterative 
    dp = { len(s): 1}

    for i in range(len(s) - 1, -1, -1):
        if s[i] == '0': 
            dp[i] = 0
        else: 
            dp[i] = dp[i + 1]
        
        if (i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456')): 
            dp[i] += dp[i + 2]

    return dp[0]

s1 = '12' # expect: 2 -> 'AB' (1 2) or 'L' (12)
s2 = '226' # expect: 3 -> 'BZ' (2 26) or 'VF' (22 6) or 'BBF' (2 2 6)
s3 = '06' # expect: 0
s4 = '1847624' # expect: 4
s5 = '8473627' # expect: 1
s6 = '122341' # expect: 5
s7 = '121021' # expect: 4
s = '120' 
print('RESULT :', numDecodings(s1))

'''
          '121'
        1     12
      2  21  1
    1       
                '1212'
            1           12
        2      21    1     12
      1  12   2     2
    2
'''