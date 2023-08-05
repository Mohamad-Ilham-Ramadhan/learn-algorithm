'''
    Codeforces: D Lecture Sleep (1200)
    link: https://codeforces.com/problemset/problem/961/B
    Tags: [data structures, dp, implementation, two pointers]
    
===========================================================

    submission:
        runtime: 124 ms, memory: 15900 KB
'''

'''
input:
6 3
1 3 5 2 5 4
1 1 0 1 0 0
output:
16 (1+3+5+2+5)

input:
3
1 3 5 2 5 4 1 1 17
1 1 0 1 0 0 1 1 0
output:
25

'''
[n, k] = input().split(' ')
n = int(n)
k = int(k)
theorems = input().split(' ')
for i in range(len(theorems)):
    theorems[i] = int(theorems[i])
behaviors = input().split(' ')
for i in range(len(behaviors)):
    behaviors[i] = int(behaviors[i])

bonus = 0 # bonus if using the secret technique (k)
maxBonus = 0
result = 0
l = 0 # left pointer for k window
for i in range(len(theorems)):
    # print('i-l', i-l)
    if (i - l) == k:
        if behaviors[l] == 0: 
            bonus -= theorems[l]
        l += 1
    
    if behaviors[i] == 0:
        bonus += theorems[i]
    
    # print('l', l, 'i', i, 'bonus', bonus)
    if behaviors[i]: 
        result += theorems[i]
    
    maxBonus = max(maxBonus, bonus)
# print('result', result, maxBonus)
print(result + maxBonus)



# leetcode style
# def writeDown(k, theorems, behaviors):
#     bonus = 0 # bonus if using the secret technique (k)
#     maxBonus = 0
#     result = 0
#     l = 0 # left pointer for k window
#     for i in range(len(theorems)):
#         if (i - l) == k:
#             if behaviors[l] == 0: 
#                 bonus -= theorems[l]
#             l += 1
        
#         if behaviors[i] == 0:
#             bonus += theorems[i]
        
#         print('l', l, 'i', i, 'bonus', bonus)
#         if behaviors[i]: 
#             result += theorems[i]
        
#         maxBonus = max(maxBonus, bonus)
#     print('result', result, maxBonus)
#     return result + maxBonus

# k1 = 3; theorems1 = [1,3,5,2,5,4]; behaviors1 = [1,1,0,1,0,0] # 16
# k2 = 3; theorems2 = [1,3,5,2,5,4,1,1,17]; behaviors2 = [1,1,0,1,0,0,1,1,0] # 25
# k3 = 2; theorems3 = [5,2,7]; behaviors3 = [0,1,0] # 9
# k4 = 2; theorems4 = [5,5,2,7]; behaviors4 = [0,0,1,0] # 12
# k5 = 1; theorems5 = [7]; behaviors5 = [0] # 7
# k6 = 0; theorems6 = [7]; behaviors6 = [0] # 0
# print('RESULT : ', writeDown(k5, theorems5, behaviors5))

