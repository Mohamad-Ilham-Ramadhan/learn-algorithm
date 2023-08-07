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
[v1, v2] = input().split(' ')
v1, v2 = int(v1), int(v2)
[t, d] = input().split(' ') 
t, d = int(t), int(d)

result = 0 
bonus = 0 # speed bonus
dp = [0] * (t - 1)
for i in range(t-1): 
    result += v1 + bonus 
    dp[i] = v1 + bonus
    bonus += d
result += v2
# print('result', result)
# print('dp', dp)
lastSpeed = v2 
for i in range(len(dp) - 1, -1, -1): 
    diff = abs(lastSpeed - dp[i]) - d 
    # print('diff', diff)
    if diff > 0: 
        result -= diff
        dp[i] -= diff
    lastSpeed = dp[i]
# print('result', result)
# print('dp', dp)
print(result)

# Leetcode style
# def solution(v1, v2, t, d): 
#     result = 0 
#     bonus = 0 # speed bonus
#     dp = [0] * (t - 1)
#     for i in range(t-1): 
#         result += v1 + bonus 
#         dp[i] = v1 + bonus
#         bonus += d
#     result += v2
#     print('result', result)
#     print('dp', dp)
#     lastSpeed = v2 
#     for i in range(len(dp) - 1, -1, -1): 
#         diff = abs(lastSpeed - dp[i]) - d 
#         print('diff', diff)
#         if diff > 0: 
#             result -= diff
#             dp[i] -= diff
#         lastSpeed = dp[i]
#     print('result', result)
#     print('dp', dp)

# solution(7, 3, 5, 4)