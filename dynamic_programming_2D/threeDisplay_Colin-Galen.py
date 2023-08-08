'''
    Codeforces: (dynamic programming) C. Three Display (1400)
    link: https://codeforces.com/problemset/problem/987/C
    Tags: brute force dp, implementation, *1400

===========================================================

    submission:
        runtime: 202 ms, memory: 4500 KB
'''

'''
5
2 4 5 4 10
40 30 20 10 40 
2(40) + 4(30) + 5(20) = 90

2 4 5 4 10 6
40 30 20 10 40 10
2(40) + 4(10) + 6(10) = 60

[6, 10] [4->6, 10] [4->6, 10, 5->6] [4->6, 4->10, 4->5->6] [2->4->6, 2->4->10, 4->5->6]
'''

# Colin Galen's solution
n = int(input())
a = [int(s) for s in input().split(' ')]
c = [int(i) for i in input().split(' ')]

dp = []
inf = 1e17
ans = inf 

for i in range(n): 
    dp.append([])
    dp[i].append(c[i])
    for j in range(1, 3): 
        dp[i].append(inf)
        for k in range(i):
            if a[k] < a[i]:
                dp[i][j] = min( dp[i][j], dp[k][j - 1] + c[i])

    ans = min(ans, dp[i][2])

print('dp', dp)
if ans == inf: ans = -1 
print(ans)
'''
6
2 4 5 4 10 6
40 30 20 10 40 10 
i=5
j=2
k=0
dp [
    [40, inf, inf]
    [30, 70, inf]
    [20, 50, 90]
    [10, 50, inf]
    [40, 50, 90]
    [10, 20, 60]
]
dp [
    [40, 1e+17, 1e+17],
    [30, 70, 1e+17],
    [20, 50, 90],
    [10, 50, 1e+17],
    [40, 50, 90]
]
'''