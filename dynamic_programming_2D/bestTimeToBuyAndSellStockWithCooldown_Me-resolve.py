"""
	(2D Dynamic Programming) 309. Best Time to Buy and Sell Stock with Cooldown (medium)

	Link: https://leetcode.com/problems/partition-equal-subset-sum
    
	Tags:  Array, Dynamic Programming

	Constraints:
		- 1 <= nums.length <= 200
		- 1 <= nums[i] <= 100
	======================================================================

	Submissions: 
		resolve
			runtime: 50 ms, beats 75.42%
			memory: 16.69 MB, beats 79.81%
"""
'''
n1 = [1,2,3,0,2] # 3
   b    c   s
2= -2 | 0 | 2
0= 2 | 0 | 0
3= -3 | 2 | 3
2= 1 | 2 | 4
1= 3 | 2 | 0

n3 = [0,2,7,8,3,9,5,9] # 13
p= 0 | 0 | 0
p= 0 | 0 | 0
9= -9| 0 | 9
5= 4 | 0 | 9
9= 0 | 4 | 9
3= 6 | 4 | 9
8= 1 | 6 | 12
7= 5 | 6 | 13
2= 11| 6 | 13
0= 13| 11| 13
untung = 13

'''
def maxProfit(prices):
	dp1 = [0,0,0] # i-1, [buy profit, cooldown profit, sell profit]
	dp2 = [0,0,0] # i-2, [buy profit, cooldown profit, sell profit]
	for i in range(len(prices)-1, -1, -1):
		p = prices[i]
		newDp1 = [dp1[2] - p, max(dp1[0], dp1[1]), max(p + max(dp2[0], dp2[1]), dp1[2])]
		dp2 = dp1 
		dp1 = newDp1
	return max(dp1[0], dp1[1])
n1 = [1,2,3,0,2] # 3 [1->2, 0->2]
n2 = [1] # 0
n3 = [0,2,7,8,3,9,5,9] # 13
print('RESULT: ', maxProfit(n2))