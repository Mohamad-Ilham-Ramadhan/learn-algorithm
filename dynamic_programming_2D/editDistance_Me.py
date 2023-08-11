'''
    (2D dynamic programming) leetcode: 72 Edit Distance (medium)

    link: https://leetcode.com/problems/edit-distance/

    Tags: String, Dynamic Programming

    ======================================

        submission: 
            #1
                runtime: 143 ms, beats 58.13%
                memory: 22.13 MB, beats 11.44%
            #2
                runtime: 127 ms, beats 68.88%
                memory: 20.14 MB, beats 21.24%
'''

'''
        u r s a 0
    
    d   5 5 5 6 7
    o   4 4 4 5 6
    k   3 3 3 4 5
    u   2 2 2 3 4
    s   3 2 1 2 3
    a   4 3 2 1 2
    n   4 3 2 1 1
    0   4 3 2 1 0

    ursa ursa
    w1 = intention w2 = execution # 5

    if different then min(bottom, right, bottom-right) + 1
    if same then bottom-right
'''
# solution 1
def minDistance(word1, word2):
    pass 
    dp = []
    for i in range(len(word2)+1):
        dp.append([])
        for j in range(len(word1)): 
            dp[i].append(len(word1)-j)
        dp[i].append(len(word2)-i)

    for i in range(len(word2)-1, -1, -1): 
        for j in range(len(word1)-1, -1, -1): 
            c1 = word1[j]
            c2 = word2[i]
            # print('c1', c1, 'c2', c2)
            if c1 == c2: 
                dp[i][j] = dp[i+1][j+1]
            else: 
                dp[i][j] = min(dp[i+1][j+1], dp[i][j+1], dp[i+1][j]) + 1
    
    # print('dp', dp)
    return dp[0][0]

w1 = 'ursa'; w2 = 'dokusan'
# print('RESULT: ', minDistance(w1, w2))

'''
    w1 = horse w2 = ros # 3

        0 h o r s e

    0   0 1 2 3 4 5
    r   1 1 2 2 3 4
    o   2 2 1 2 3 4
    s   3 3 2 2 2 3
'''
# solution 2
def minDistance2(word1, word2):
    dp = [[]]
    dp[0] = [i for i in range(len(word1)+1)]
    for i in range(1, len(word2) + 1): 
        dp.append([i])
        for j in range(1, len(word1) + 1):
            # w1Index= i - 1, 
            if word1[j-1] == word2[i-1]:
                dp[i].append(dp[i-1][j-1])
            else: 
                dp[i].append( min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1)
    return dp[len(word2)][len(word1)]
minDistance2('horse', 'ros')

'''
    [   [4, 3, 2, 1, 0],
        [3, 3, 2, 1, 0],
        [2, 2, 2, 1, 0],
        [1, 1, 1, 1, 0],
        [2, 1, 0, 1, 0],
        [3, 2, 1, 0, 0],
        [4, 3, 2, 1, 0],
        [4, 3, 2, 1, 0]]
'''

'''

    w1 = dokusan w2 = ursa # 5
        n a s u k o d

    a   1 1 2 3 4 5 6
    s   1 1 1 2 3 4 5
    r   1 1 1 2 3 4 5
    u   1 1 1 2 3 4 5

    w1 = ursa w2 dokusan # 5
        0 a s r u

    0   0 0 0 0 0
    n   1 1 2 3 4     
    a   2 1 2 3 4    
    s   3 2 1 2 3    
    u   4 3 2 3 2
    k   5 4 3 4 3
    o   6 5 4 5 4
    d   7 6 5 6 5

        u r s a 0
    
    d   5 5 5 6 7
    o   4 4 4 5 6
    k   3 3 3 4 5
    u   2 2 2 3 4
    s   3 2 1 2 3
    a   4 3 2 1 2
    n   4 3 2 1 1
    0   4 3 2 1 0

    ursa ursa
    w1 = intention w2 = execution # 5

        n o i t n e t n i
                u c e x e
    n   0 1 2 3 4 5 6 7 8
    o   0 0 1 2 3 4 5 6 7
    i   0 0 0 1 2 3 4 5 6
    t   0 0 0 0 1 2 3 4 5
    u   0 0 0 0 1 2 3 4 5
    c   0 0 0 0 1 2 3 4 5
    e   0 0 0 0 1 2 3 4 5
    x
    e
'''