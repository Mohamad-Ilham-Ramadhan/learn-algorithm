'''
    Codeforces: D Lecture Sleep (1200)
    link: https://codeforces.com/problemset/problem/961/B
    Tags: [data structures, dp, implementation, two pointers]

===========================================================

    submission:
        # Colin Galen prefix sum
            runtime: 124 ms, memory: 18200 KB
'''

'''
input:
6 3
1 3 5 2 5 4
1 1 0 1 0 0
output:
16 (1+3+5+2+5)

input:
9 3
1 3 5 2 5 4 1 1 17
1 1 0 1 0 0 1 1 0
output:
25

'''
# Colin Galen answer (Dynamic programming: prefix sum)
[n, k] = input().split(' ')
n, k = int(n), int(k)
a = input().split(' ')
for i in range(len(a)):
    a[i] = int(a[i])
b = input().split(' ')
for i in range(len(b)):
    b[i] = int(b[i])

p = [0] * n # prefix sum when b[i] is 1
p[0] = a[0] * b[0]
for i in range(1, n):
    p[i] = a[i] * b[i] + p[i - 1]

s = [0] * n # suffix sum when b[i] is 1
r = 0
for i  in range(n-1, -1, -1):
    r += a[i] * b[i]
    s[i] = r 

# prefix sum without consider b[i]
pref = [0] * n 
r = 0
for i in range(n):
    r += a[i]
    pref[i] = r

ans = 0
i = 0
while i + k - 1 < n:
    cur = 0
    if i > 0: cur += p[i - 1]
    if i + k < n: cur += s[i + k]

    range_sum = pref[i + k - 1]
    if i > 0: range_sum -= pref[i - 1]
    cur += range_sum
    print('cur', cur)
    ans = max(ans, cur)
    i += 1

print(ans)
'''
1 3 5 2 5 4
1 1 0 1 0 0
p [1, 4, 4, 6, 6, 6]
s [6, 5, 2, 2, 0, 0]
pref [1, 4, 9, 11, 16, 20]

i = 2
cur = 4
range_sum =  12
'''
# print('p', p)
# print('s', s)
# print('pref', pref)
# print('r', r)
# print('ans', ans)