"""
	(Dynamic Programming) 1043. Partition Array for Maximum Sum (medium)

	Link: https://leetcode.com/problems/partition-array-for-maximum-sum/
    
	Tags: Dynamic Programming,

	Constraints:
		- 1 <= arr.length <= 500
		- 0 <= arr[i] <= 10^9
		- 1 <= k <= arr.length
	======================================================================

	Submissions: 
		runtime: _ ms, beats 5.12%
		memory: _ MB, beats 80.16%
"""
'''
a1 = [1,15,7,9,2,5,10]; k1 = 3 # 84 [15,15,15,9,10,10,10]
[1,15,7,9,2,5,10]
[14,14,22,0,7,11,11

a2 = [1,4,1,5,7,3,6,1,9,9,3]; k = 4 # 83
	  [4,7,7,7,7,9,9,9,9,9,9]
		1 4 1  5  7  3 6 1  9 9 3
	1  0 
   4  3 0 3 
   1  3
   5  4 5 9 9 
   7  0 3 9 11 11 12 7 11
   3  
   6
   1
   9
   9
   3
   
   [1,1,1,5,4,3,7]
   [5,5,5,5,7,7,7]
   
	[5,5,8, 6, 7, 0, 1, 2, 0, 9]; k5 = 4 # 82
   [8,8,8, 8, 2, 2
				   7, 7
				  		  24,24,24,24
   
	a6 = [5,7,9,5,10,1,0,10,6,0]; k6 = 4 # 97
   
			5  7  9  5  10  1  0  10  6  0
      2  0  2  2  4  5   9  1  9   4  
      3
      4

'''
def maxSumAfterPartitioning(arr, k):
    pass

a1 = [1,15,7,9,2,5,10]; k1 = 3 # 84 [15,15,15,9,10,10,10]
a2 = [1,4,1,5,7,3,6,1,9,9,3]; k2 = 4 # 83
a3 = [1]; k3 = 1 # 1
a4 = [1,1,1,5,4,3,7]; k4 = 4 # 41
a5 = [5,5,8,6,7,0,1,2,0,9]; k5 = 4 # 82
a6 = [5,7,9,5,10,1,0,10,6,0]; k6 = 4 # 97

print('sum sum', sum([1,7,7,7,7,9,9,9,9,9,9]))