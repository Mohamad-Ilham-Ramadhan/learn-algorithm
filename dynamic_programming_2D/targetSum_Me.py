"""
	(2D Dynamic Programming) 494. Target Sum (medium)

	Link: https://leetcode.com/problems/target-sum/
    
	Tags: Array, Dynamic Programming, Backtracking

	Constraints:
		- 1 <= nums.length <= 20
		- 0 <= nums[i] <= 1000
		- 0 <= sum(nums[i]) <= 1000
		- -1000 <= target <= 1000
	======================================================================

	Submissions: 
		HashMap DP
			runtime: 169 ms, beats 84.80%
			memory: 16.37 MB, beats 94.19%
"""
'''
	[1 1 1 1 1] t=3
	1 2 3
1  1, -1
1  2 0, 0 -2
1  3 1 1 -1, 1 -1 -1 -3
1  4 2 2 0 2 0 0 -2, 2 0 0 -2 0 -2 -2 -4
1  5 3 3 1 3 1 1 -1 3 1 1 -1 1 -1 -1 -3, 3 1 1 -1 1 -1 -1 -3 1 -1 -1 -3 -1 -3 -3 -5

Above, there is a lot redundant number, so we remove it using hashmap
0 {0: 1}
1 { 1: 1, -1, 1}
1 { 2: 1, 0: 2, -2: 1}
1 { 3: 1, 1: 3, -1: 3, -3: 1}
1 { 4: 1, 2: 4, 0: 6, -2: 4, -4: 1}
1 {5: 1, 3: 5, 1: 10, -1: 10, -3: 5, -5: 1}

	[1 2 2 5] t=8 # 1
1 	1 -1
2  3 1 -1 -3
2  5 3 1 -1, 1 -1 -3 -5
5  10 8 6 4 6 4 2 0, 0 -2 -4 -6 -4 -6 -8 -10
'''
# hash Map dp by myself
def findTargetSumWays(nums, target):
	dp = {0: 1}
	for i in range(len(nums)):
		newDp = {}
		for key in dp:
			if key + nums[i] in newDp:
				newDp[key + nums[i]] += dp[key]
			else: 
				newDp[key + nums[i]] = dp[key]

			if key - nums[i] in newDp:
				newDp[key - nums[i]] += dp[key]
			else: 
				newDp[key - nums[i]] = dp[key]
		print('newDP', newDp)
		dp = newDp
	if target not in dp:
		return 0
	print('dp', dp)
	return dp[target]

n1 = [1,1,1,1,1]; t1 = 3 # 5
n2 = [1]; t2 = 1; # 1
n3 = [1,2,2,5]; t3 = 8 # 1
n4 = [0,0,0,0,0,0,0,0,1]; t4 = 1 # 256
print('RESULT: ', findTargetSumWays(n1, t1))
