"""
	(1D Dynamic Programming) 312. Burst Ballons (hard)

	Link: https://leetcode.com/problems/burst-balloons/
    
	Tags:  Dynamic Programming

	Constraints:
		- n == nums.length
		- 1 <= n <= 300
		- 0 <= nums[i] <= 100
	======================================================================

	Submissions: 
		runtime: _ ms, beats 90.92%
		memory: _ MB, beats 89.95%
"""
'''
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
   
'''
def maxCoins(nums):
	pass
n1 = [3,1,5,8] # 167
n2 = [1,5] # 10
n3 = [5,1] # 10
n4 = [5,8,1,9] # 486
n5 = [0,8,1,2,3] # 96
# print('RESULT: ', maxCoins(n1))

def jump(nums):
	inf = 1e7
	dp = [inf] * len(nums)
	dp[len(nums)-1] = 0
	for i in range(len(nums)-2, -1, -1):
		j = i + nums[i]
		if j >= len(nums): j = len(nums)-1
		while j > i:
				dp[i] = min(dp[i], dp[j])
				j -= 1
		dp[i] += 1
	print('dp', dp)
	return dp[0]

n1 = [2,3,1,1,4]
print('RESULT: ', jump(n1))