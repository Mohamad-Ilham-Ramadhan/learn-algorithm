'''
    Codeforces: (dynamic programming) 830A Office Keys (1800)
    link: https://codeforces.com/problemset/problem/830/A
    Tags: dynamic programming

===========================================================

    submission:
        runtime: 202 ms, memory: 37100 KB
'''

'''
input #1:
2 4 50
20 100
60 10 40 80
output: 50

input #2:
1 2 10
11
15 7
output: 7
    
'''

# By Colin Galen
[n,k,p] = input().split(' ')
n, k, p = int(n), int(k), int(p)
a = [int(i) for i in input().split(' ')]
b = [int(i) for i in input().split(' ')]
a.sort()
b.sort()
inf = 1e17
dp = []
for i in range(k+1):
    dp.append([])
    for j in range(n+1):
        dp[i].append(inf)

dp[0][0] = 0

for i in range(k):
    for j in range(n+1):
        # don't take person
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

        # do take person
        if j < n:
            dp[i+1][j+1] = min(dp[i+1][j+1], max(dp[i][j], abs(a[j] - b[i]) + abs(b[i] - p)) )

print(dp[k][n])


# def officeKeys(location, people, keys):

#     # for p in people:
#     #     for k in keys: 
#     #         d = abs(p - k)
#     #         d += abs(k - location)
#     #         print('p', p, 'd', d)
#     people.sort()
#     keys.sort()
    
# l1 = 50
# p1 = [20, 100]
# k1 = [60, 10, 40, 80]
# officeKeys(l1, p1, k1)
'''
20 100
10 40 60 80
'''