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

    Solution by myself:
        base case: 
        dp[-2] = 0
        dp[-1] = 1
        dp[0] = 0 + 1 = 1

        if s[i-1] == '0':
            dp[i] = dp[i-1]

        if int(s[i-1] + s[i]) <= 26 for example s[i-1] = '1' and s[i] = '9', so int(s[i-1] + s[i]) = '19', convert to number 19 <= 26 true, then:
            dp[i] = dp[i-1] + dp[i-2]

        if int(s[i-1] + s[i]) > 26 then:
            dp[i] = dp[i-1]


        if s[i] == '0':
            if int(s[i-1] + s[i]) <= 26:
                dp[i] = dp[i-2]
            if int(s[i-1] + s[i]) > 26
                return 0
        
        return dp[len(dp) - 1]
    
    LeetCode submission:
        Runtime: 48 ms, beats 55.24%
        Memory: 16.3 MB, beats 47.56%
'''

# attempt #1
def numDecodings(s):
    if s[0] == '0': return 0

    # Base case
    s = '00' + s
    dp = [0] * len(s)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, len(s)):
        ns = s[i]
        nn = int(ns)
        pcn = int(s[i-1] + s[i]) # prev + c to number
        if s[i-1] == '0':
            if nn == 0:
                return 0
            dp[i] = dp[i-1]
            continue
        if nn == 0:
            if pcn <= 26: 
                dp[i] = dp[i-2]
                continue
            elif pcn > 26:
                return 0
        if pcn <= 26 :
            dp[i] = dp[i-1] + dp[i-2]
        elif pcn > 26 :
            dp[i] = dp[i-1]
        # print('char', s[i])
        # if 
    # print('dp', dp)
    return dp[len(dp) - 1]

s1 = '12' # expect: 2 -> 'AB' (1 2) or 'L' (12)
s2 = '226' # expect: 3 -> 'BZ' (2 26) or 'VF' (22 6) or 'BBF' (2 2 6)
s3 = '06' # expect: 0
s4 = '1847624' # expect: 4
s5 = '8473627' # expect: 1
s6 = '122341' # expect: 5
s7 = '121021' # expect: 4
s = '120' 
# print('RESULT :', numDecodings(s1))
print('to number', '09', int('09'))

'''
    1 -> A      8   -> H        15  -> O        22  -> V
    2 -> B      9   -> I        16  -> P        23  -> W
    3 -> C      10  -> J        17  -> Q        24  -> X
    4 -> D      11  -> K        18  -> R        25  -> Y
    5 -> E      12  -> L        19  -> S        26  -> Z
    6 -> F      13  -> M        20  -> T
    7 -> G      14  -> N        21  -> U

    base case: 
        dp[ when i < 0 ] = 0

    if int(s[i-1] + s[i]) convert to number <= 26 for example i-1 = '1' and i = '9', so int(s[i-1] + s[i]) = '19', convert to number 19 <= 26 true, then:
        dp[i] = dp[i-1] + dp[i-2]

    if int(s[i-1] + s[i]) > 26 then:
        dp[i] = dp[i-1]

    if i-1 == zero:
        dp[i] = dp[i-1]

    if i == ZERO:
        if int(s[i-1] + s[i]) <= 26:
            dp[i] = dp[i-2]
        if i-1 + 1 > 26
            return 0
    
    2012260 -> 0
    201226 ->  5       
    1 1 1 2 3 5

    203 -> 1
    T TC
            
    1213021 -> 0

    1212021 -> 6
    A   AB  ABA ABAB    ABAT    ABATB   ABATBA
        G   AU  ABG     AUT     AUTB    ABATU
            GA  AUB     GAT     GATB    AUTBA
                GAB                     AUTU
                GG                      GATBA
                                        GATU
                
    121021 -> 4
    A   AB  ABA ABJ ABJB    ABJBA
        L   AU  LJ  LJB     ABJU
            LA              LJBA
                            LJU
            
    12234192 -> 10
    A   AB  ABB ABBC    ABBCD   ABBCDA 10 20
        L   AV  ABW     ABWD    ABWDA
            LB  AVC     AVCD    AVCDA
                LBC     LBCD    LBCDA
                LBW     LBWD    LBWDA

    122341 -> 5
    A   AB  ABB ABBC    ABBCD   ABBCDA
        L   AV  ABW     ABWD    ABWDA
            LB  AVC     AVCD    AVCDA
                LBC     LBCD    LBCDA
                LBW     LBWD    LBWDA

    [1] [12, 2] [22, 22] [25, 5, 25, 5] [4, 4, 4, 4] [1, 1, 1, 1]

    8473627 -> 1
    [8] [4] [7] [3] [6] [2] [7]

    1847624 -> 4
    [1] [18, 8] [4, 4] [7, 7] [6, 6] [26, 6, 26, 6] [4, 4, 4, 4]

    226
    [2] [22, 2] [6, 26, 6]

    

    1212 -> 5
    A   AB  ABA ABAB
        G   AU  ABG
            GA  AUB
                GAB
                GG

    12121 -> 8
    A   AB  ABA ABAB    ABABA
        G   AU  ABG     ABAU
            GA  AUB     ABGA
                GAB     AUBA
                GG      AUU
                        GABA
                        GAU
                        GGA

    [1] [2, 12] [1, 21, 1] [2, 12, 2, 12, 2] [1, 21, 1, 21, 1, 1, 21, 1]

    121212 -> 13
    A   AB  ABA ABAB    ABABA   ABABAB
        G   AU  ABG     ABAU    ABABG
            GA  AUB     ABGA    ABAUB
                GAB     AUBA    ABGAB
                GG      AUU     ABGG
                        GABA    AUBAB
                        GAU     AUBG
                        GGA     AUUB
                                GABAB
                                GABG
                                GAUG
                                GGAB
                                GGG
    ABAB
    GAB
    AUB
    ABG
    GG

    121212 -> 13
    1212121 -> 21
    12121212 -> 34
    121212121 -> 55
    1212121212 -> 89
'''