"""
	(Greedy) 45. Jump Game II (medium)

	Link: https://leetcode.com/problems/jump-game-ii
    
	Tags:  Array, Dynamic Programming, Greedy

	Constraints:
    - 1 <= nums.length <= 10^4
      - 0 <= nums[i] <= 1000
      - It's guaranteed that you can reach nums[n - 1].
	======================================================================

	Submissions: 
		runtime: 114 ms, beats 83.12%
		memory: 17.12 MB, beats 98.82%
"""

def jump(nums):
    res = 0
    l = r = 0 
    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(farthest, i + nums[i])
        l = r + 1
        r = farthest
        res += 1
    return res


n1 = [2,3,1,1,4] # 2
n2 = [4,9,7,3,5,10,9,1,2,6] # 2
n3 = [3,3,1,1,2,4,7,1,2,0] # 4
n4 = [4,2,0,1,3,0,3,2,2,1,4,1] # 5
n5 = [7,3,1,7,3,1,3,2,1,1,4,1,7,4,0] # 3
n6 = [1,0] # 1
n7 = [3,2,1]
'''
n  = [7,3,1,7,3,1,3,2, 1,1,4, 1,7,4,0] # 3 , 14
     [0,4,3,10,7,6,9,8, 9,10,14]
'''
print('RESULT: ', jump(n6))
