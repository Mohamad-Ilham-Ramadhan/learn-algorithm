'''
    Codeforces: (dynamic programming) 548B Mike and Fun (1400)
    link: https://codeforces.com/problemset/problem/548/B
    Tags: brute force, dp, greedy, implementation, *1400

===========================================================

    submission:
        runtime: _ ms, memory: _ KB
'''

'''
input #1:
5 4 5
0 1 1 0
1 0 0 1
0 1 1 0
1 0 0 1
0 0 0 0
1 1
1 4
1 1
4 2
4 3
output: 
3
4
3
3
4

input #2:
2 2 10
1 1
0 1
1 1
2 1
1 1
2 2
1 1
2 1
2 2
2 2
1 1
1 1
output: 
1
2
2
2
1
1
1
1
2
1

input #4
5 5 30
0 1 1 1 0
1 1 0 1 1
0 1 1 1 1
0 0 1 1 0
0 0 0 0 0
3 2
2 2
2 2
4 3
1 4
3 2
4 1
2 4
1 4
2 1
5 2
4 1
4 1
5 1
2 4
2 4
4 4
1 2
3 1
4 5
1 2
2 3
1 1
5 1
3 4
1 1
5 4
1 5
5 4
2 2
output: 
3
3
3
3
3
4
4
4
4
4
4
4
4
4
4
4
4
4
5
5
5
5
5
5
4
3
3
4
4
4
'''

# time complexity O(q (m+n))
[n, m, q] = input().split(' ')
n,m,q = int(n), int(m), int(q)
grid = []
dp = []
for i in range(n):
    grid.append([])
    dp.append([])
    total = 0
    mx = 0
    for j in input().split(' '):
        grid[i].append(int(j))
        if int(j) == 1: total += 1
        else: 
            mx = max(mx, total)
            total = 0
    mx = max(mx, total)
    dp[i] = mx

# query O(q (m + n))
for k in range(q):
    [i,j] = input().split(' ')
    i,j = int(i)-1, int(j)-1
    grid[i][j] ^= 1 # flip 1 to 0, and 0 to 1

    # O(m)
    cm = 0 # current row max
    total = 0
    for col in grid[i]:
        if col == 1: total += 1
        else: 
            cm = max(cm, total)
            total = 0
    cm = max(cm, total)
    dp[i] = cm

    # O(n)
    # select current query max from all row in dp
    for m in dp:
        cm = max(cm, m)
    print(cm)

'''
2 2 10
1 1
0 1
1 1
2 1
1 1
2 2
1 1
2 1
2 2
2 2
1 1
1 1

1
2
2
2
1
1
1
1
2
1
'''