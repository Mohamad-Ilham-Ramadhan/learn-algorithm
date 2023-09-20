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
		runtime: 117 ms, beats 73.49%
		memory: 17.25 MB, beats 93.55%
"""

def jump(nums):
    l = 0 # left limit of posibility jump sub array
    c = 0 # current pos
    j = 0
    while l < len(nums) - 1: 
        f = 0 # farthest jump
        fi = 0 # farthest jump index
        for i in range(1 + l, 1 + c + nums[c]):
            if i >= len(nums) - 1: return j + 1
            if i + nums[i] > f: 
                fi = i
                f = i + nums[i]
            if fi >= len(nums) - 1: return j + 1
        l = c + nums[c]
        j += 1
        c = fi
    return j


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
