'''
    Codeforces: Hello 2019: B. Petr and a Combination Lock (1200)

    link: https://codeforces.com/problemset/problem/1097/B
    
    Problem tags:
        [bitmask, brute force, dp, *1200]
    =============================================

    Submission:
        # backtracking
            rutnime: 108 ms, memory: 6200 KB
'''

# codeforces's solution 
# backtracking
n = int(input()) 
degrees = []
i = 0
while i < n: 
    i += 1
    degrees.append(int(input()))

# print('n', n, 'degrees', degrees)
combinations = []
def backtrack(i, total): # rotation 0 = right/clockwise, 1 = left/counter-clockwise
    # print('i', i)
    if i == len(degrees):
        if total == 0 or total % 360 == 0: 
            combinations.append(True)
        else: 
            combinations.append(False)
        return
    
    # if rotation: # counter clockwise
    backtrack(i+1, total - degrees[i])
    # else:
    backtrack(i+1, total + degrees[i])

backtrack(0, 0)
# print('combinations', combinations)
isNo = True
for c in combinations: 
    if c: 
        print('YES')
        isNo = False 
        break
if isNo:
    print('NO')

# leetcode's solution style
# backtracking
# def lock(degrees):
#     combinations = []
#     def backtrack(i, total): # rotation 0 = right/clockwise, 1 = left/counter-clockwise
#         print('i', i)
#         if i == len(degrees):
#             if total == 0 or total % 360 == 0: 
#                 combinations.append(True)
#             else: 
#                 combinations.append(False)
#             return
        
#         # if rotation: # counter clockwise
#         backtrack(i+1, total - degrees[i])
#         # else:
#         backtrack(i+1, total + degrees[i])


#     backtrack(0, 0)
#     print('combinations', combinations)
#     for c in combinations: 
#         if c: return True 
    
#     return False

# n1 = [10,20,30]
# n2 = [10,10,10]
# n3 = [120,120,120]
# print('RESULT : ', lock(n3))