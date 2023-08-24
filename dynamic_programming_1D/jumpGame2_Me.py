"""
	(1D Dynamic Programming) 45. Jump Game II (medium)

	Link: https://leetcode.com/problems/jump-game-ii
    
	Tags:  Array, Dynamic Programming, Greedy

	Constraints:
		- 1 <= nums.length <= 10^4
      - 0 <= nums[i] <= 1000
      - It's guaranteed that you can reach nums[n - 1].
	======================================================================

	Submissions: 
		runtime: 4464 ms, beats 22.39%
		memory: 17.55 MB, beats 19.45%
"""
# slow dp
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
