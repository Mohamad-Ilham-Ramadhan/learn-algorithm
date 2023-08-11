'''
    (2D dynamic programming) Leetcode: 322. Coin Change (medium)

    Link: https://leetcode.com/problems/coin-change/

    Tags: Array, Dynamic Programming, Breadth-search first

    ======================================================================

    Submissions: 
        runtime: 1143 ms, beats 76.49%
        memory: 16.74 MB, beats 55.55%

'''
    
def coinChangeDP1(coins, amount):
    inf = 1e10
    dp = [inf] * (amount + 1)
    dp[0] = 0
    for i in range(amount + 1):
        cc = dp[i] + 1 # current coin 
        for j in range(len(coins)):
            c = coins[j]
            if i + c <= amount: 
                dp[i + c] = min(cc, dp[i + c])
        print('dp', dp)

    return -1 if dp[amount] == inf else dp[amount]

c1 = [1,2,5]; a1 = 12
c2 = [186,419,83,408]; a2 = 6249
c3 = [1,2,5,7,8,4]; a3 = 30 # 4 (7,7,8,8)
c4 = [1,5,6,8]; a4 = 11
print('RESULT: ', coinChangeDP1(c3, a3))
'''
    [1,5,6,8]
        i = 5
        cc = 6
        0   1  2  3  4  5  6  7  8  9  10  11
        0   1  2  3  4  1  1  2  1  1  3   4

    [1,3,4] a = 14 3,4,3,4
    44411 wrong

        0   1  2  3  4  5  6  7  8  9  10 11 12  13  14

    0   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1  -1 -1  -1  -1 
    1   0   1  2  3  3  5  6  7  8  9  10 11 12  13  14
    3   0   1  2  1  2  3  2  3  4  3  4  5  4    5  6
    4   0   1  2  1  1  2  2  2  2  3  3  3  3   4   4
    []

'''