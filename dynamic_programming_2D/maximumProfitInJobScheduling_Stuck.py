"""
	(1D dynamic programming) Leetcode: 1235. Maximum Profit in Job Scheduling (hard)

	Link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/
	Tags: Dynamic programming

	Constraints:
		- 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
		- 1 <= startTime[i] < endTime[i] <= 10^9
		- 1 <= profit[i] <= 10^4
	======================================================================

	Submissions: 
		#1 1D dynamic programming
			runtime: 40 ms, beats 78.49%
			memory: 16.28 MB, beats 72.48%

"""

'''
	startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
   [1,  2,  3,  3]
   [3,  4,  5,  6]
   [50, 10, 40, 70]
    
	
   
dp [50, 70]

	startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
	[1,  2,  3,   4,  6]
	[3,  5,  10,  6,  9]
	[20, 20, 100, 70, 60]

   [5,10]
   dp [
		[3, 20]
      [5, 20]
      [6, 90]
      [9, 150]
      [10, 120]
	]

	
	startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
	[1   2  4  6  3]
	[3   5  6  9  10]
	[20 20  70 60 100]
	dp [
		[3, 20]
		[4, 90]
		[5, 20]
		[9, 150]
		[10, 100]
	]
'''

'''
startTime = [6,24,45,27,13,43,47,36,14,11,11,12] endTime = [31,27,48,46,44,46,50,49,24,42,13,27] profit = [14,4,16,12,20,3,18,6,9,1,2,8] Output 45 Expected 45	
	[11  14]
	[13  24]

	[2    9]


'''
def sortJob(startTime, endTime, profit):	
	newStartTime = [startTime[0]]
	newEndTime = [endTime[0]]
	newProfit = [profit[0]] 
	for i in range(1, len(endTime)):
		# binary search sort 
		l = 0
		r = len(newEndTime) - 1
		while l < r: 
			pass
		

def jobScheduling(startTime, endTime, profit):
	pass 