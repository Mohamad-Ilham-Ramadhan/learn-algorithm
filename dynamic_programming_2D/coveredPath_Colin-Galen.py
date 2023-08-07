'''
    Codeforces: (dynamic programming) B. Covered Path (1400)
    link: https://codeforces.com/problemset/problem/534/B
    Tags: dynamic programming, greedy, math, *1400

===========================================================

    submission:
        runtime: 62 ms, memory: 0 KB
'''

'''
5 6
4 2
5 + 7 + 8 + 6 = 26
'''
[start, end] = input().split(' ')
start, end = int(start), int(end)
[n, d] = input().split(' ') 
n, d = int(n), int(d)

inf = 1e17
dp = [[-inf] * 10 for i in range(n)]

dp[0][start] = 0

for i in range(n-1): # time
    print("\n")
    for j in range(10): # sum
        for k in range(-d, (d+1)): # addition or substraction
            if j + k >= 0 and j + k < 10:
                m =  max( dp[i + 1][j + k], dp[i][j] + j)
                dp[i + 1][j + k] = m
                print('i', i, 'j', j, 'k', k, 'm', m)

'''
5 6
4 2
5 + 7 + 8 + 6 = 26
i = 0
j = 5
k = -2
dp [
    [-inf, -inf, -inf, -inf, -inf, 0, -inf, -inf, -inf, -inf],
    [-inf, -inf, -inf, 5, 5, 5, 5, 5, -inf, -inf],
    [-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf]
]
dp [
    [-1e+17, -1e+17, -1e+17, -1e+17, -1e+17, 0, -1e+17, -1e+17, -1e+17, -1e+17], 
    [-1e+17, -1e+17, -1e+17, 5, 5, 5, 5, 5, -9.999999999999998e+16, -9.999999999999998e+16], 
    [-1e+17, 8, 9, 10, 11, 12, 12, 12, 12, 12], 
    [11, 13, 15, 17, 18, 19, 20, 21, 21, 21]
]
'''
print('dp', dp)
print(dp[n - 1][end] + end)