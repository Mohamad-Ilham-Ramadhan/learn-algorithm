"""
	(2D Dynamic Programming) 312. Burst Ballons (hard)

	Link: https://leetcode.com/problems/burst-balloons/
    
	Tags:  Dynamic Programming

	Constraints:
		- n == nums.length
		- 1 <= n <= 300
		- 0 <= nums[i] <= 100
	======================================================================

	Submissions: 
		runtime: 4552 ms, beats 66.64%
		memory: 19.04 MB, beats 80.71%
"""
"""
n1 = [3,1,5,8] # 167
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

[5 1]
1*5*1 = 5, 1 * 1 * 1

	5 1
1  5 1
5  5 5

n1 = [3,1,5,8] # 167

3 = [3 1]=3 [3 5]=15 [3 8]=24
1 = [3 1 5]=15 [3 1 8]=24
5 = [1 5 8]=40 [3 5 8]=120
8 = [5 8]=40 [1 8]=8 [3 8]=24

n4 = [5,8,1,9] # 486

	8*1*9=72 + 5*8*9=360 + 1*5*9=45 + 9 

5 = [5 8]=40 [5 1]=5 [5 9]=45 
8 = [5 8 1]=40 [5 8 9]=360 
1 = [8 1 9]=72 [5 1 9]=45
9 = [1 9]=9 [8 9]=72 [5 9]=45

n4 = [5,8,1,9] # 486
	5  8  1 9
5  0  40 5 45
8  40 0  8 72
   

Roy Tushar's

	3 1 5 8
   0 1 2 3
   
	0  1   2   3
0   3  30  159 167
1	   15  135 159
2		   40  48
3              40

k=0 = 0 + 159 + 3 = 162
k=1 = 3 + 48 + 1 = 52
k=2 = 30 + 40 + 5 = 75
k=3 = 159 + 0 + 8 = 167
"""


def maxCoins(nums):
    n = len(nums)
    dp = []
    for i in range(n):
        dp.append([])
        for j in range(n):
            dp[i].append(0)

    print("dp", dp)
    for l in range(1, n + 1):
        for i in range(0, (n + 1) - l):
            j = i + l - 1
            m = 0 # max
            for k in range(i, j + 1):
                leftBurst = 0 if k == i else dp[i][k-1]
                rightBurst = 0 if k == j else dp[k+1][j]
                kBurst = nums[k] 
                if i > 0: kBurst = kBurst * nums[i-1]
                if j < (n-1): kBurst =  kBurst * nums[j+1]
                m = max(m, leftBurst + rightBurst + kBurst)
                print('i', i, 'j', j, 'k', k, 'm', m)
            dp[i][j] = m

    print('final dp', dp)
    return dp[0][n-1]
'''
	0  1   2   3
0   3  30  159 167
1	   15  135 159
2		   40  48
3              40

n1 = [3, 1, 5, 8]  # 167

final dp [
    [3, 4, 9, 17],
    [0, 1, 6, 14],
    [0, 0, 5, 13],
    [0, 0, 0, 8]]
'''
n1 = [3, 1, 5, 8]  # 167
maxCoins(n1)
n2 = [1, 5]  # 10
n3 = [5, 1]  # 10
n4 = [5, 8, 1, 9]  # 486
n5 = [0, 8, 1, 2, 3]  # 96
# print('RESULT: ', maxCoins(n1))
