'''
    (2D dynamic programming) Leetcode: 322. Coin Change (medium)

    Link: https://leetcode.com/problems/coin-change/

    Tags: Array, Dynamic Programming, Breadth-search first

    ======================================================================

    Submissions: 
      #1
         runtime: 4723 ms, beats 5.01%
         memory: 20.51 MB, beats 26.04%
      #2
         runtime: 3769 ms, beats 5.01%
         memory: 20.40 MB, beats 26.32%
      #3 
         runtime: 2283 ms, beats 5.01%
         memory: 20.56 MB, beats 26.04%

'''

def coinChange(coins, amount):
    coins.sort()
   #  dp = [[-1] * (amount + 1)] # solution #1, #2
    dp = [[float('inf')] * (amount + 1)] # solution #3
    for i in range(1, (len(coins) + 1)):
        dp.append([0])
        for j in range(1, amount + 1):
            c = coins[i-1]
            m = float('inf')
            if j - c >= 0: 
               m = min(m, dp[i][j-c] + 1)

            # solution #3
            m = min(m, dp[i-1][j])

            # solution #1, #2
            # for k in range(i-1, 0, -1):
            #    if k == i-3: break # soluition #2
            #    m = min(m, dp[k][j])
            dp[i].append(m)
    print('dp after', dp)
    return -1 if dp[len(coins)][amount] == float('inf') else dp[len(coins)][amount]
    

c1 = [1,2,5]; a1 = 12
c2 = [186,419,83,408]; a2 = 6249
c3 = [1,2,5,7,8,4]; a3 = 30 # 4 (7,7,8,8)
print('RESULT: ', coinChange([1,3,4], 14))
'''
        0  1  2  3  4  5  6  7  8  9  10  11

    0   0 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1  -1
    1   0  1  2  3  4  5  6  7  8  9  10  11
    2   0  1  1  2  2  3  3  4  5
    5   0  

    dp after [
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],

        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15],
        [0, 1, 1, 2, 1, 2, 2, 3, 2, 3, 3, 4, 3, 4, 4, 5, 4, 5, 5, 6, 5, 6, 6, 7, 6, 7, 7, 8, 7, 8, 8],
        [0, 1, 1, 2, 1, 1, 2, 2, 3, 2, 2, 3, 3, 4, 3, 3, 4, 4, 5, 4, 4, 5, 5, 6, 5, 5, 6, 6, 7, 6, 6],
        [0, 1, 1, 2, 1, 1, 2, 1, 2, 2, 3, 2, 2, 3, 2, 3, 3, 4, 3, 3, 4, 3, 4, 4, 5, 4, 4, 5, 4, 5, 5],
        [0, 1, 1, 2, 1, 1, 2, 1, 1, 2, 2, 3, 2, 2, 3, [2,] 2, 3, 3, 4, 3, 3, 4, 3, 3, 4, 4, 5, 4, 4, 5]
    ]

    [1,3,4] a = 14 3,4,3,4
    44411 wrong

        0   1  2  3  4  5  6  7  8  9  10 11 12  13  14

    0   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1  -1 -1  -1  -1 
    1   0   1  2  3  3  5  6  7  8  9  10 11 12  13  14
    3   0   1  2  1  2  3  2  3  4  3  4  5  4    5  6
    4   0   1  2  1  1  2  2  2  2  3  3  3  3   4   4
    []

'''