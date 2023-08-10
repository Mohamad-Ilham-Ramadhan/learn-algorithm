'''
    learn dynamic programming from Tushar Roy - Coding Made Simple Youtube playlist 

    Subset Sum Problem Dynamic Programming
'''
def subsetsum(subset, total): 
    subset.sort() 
    dp = []
    dp.append([True]) # 1 = True, 0 = False
    for i in range(1, total+1): dp[0].append(False)
    for i in range(1, len(subset) + 1): 
        i -= 1 
        dp.append([True])
        for j in range(1, total + 1):
            if dp[i][j] or j - subset[i] >= 0 and dp[i][j - subset[i]]:
                dp[i+1].append(True)
                if j == total: 
                    print('subset[i]', subset[i], 'j', j)
                    return True
            else:
                dp[i+1].append(False)
    print(dp)
    return dp[len(subset)][total]

s1 = [2,3,7,8,10]; t1 = 11 # true
print('RESULT: ', subsetsum(s1, t1))
'''
    subset: [2,3,7,8,10], total = 11 # true
[
    [True, False, False, False, False, False, False, False, False, False, False, False],
    [True, False, True, False, False, False, False, False, False, False, False, False],
    [True, False, True, True, False, True, False, False, False, False, False, False],
    [True, False, True, True, False, True, False, True, False, True, True, False],
    [True, False, True, True, False, True, False, True, True, True, True, True],
    [True, False, True, True, False, True, False, True, True, True, True, True]
]
'''