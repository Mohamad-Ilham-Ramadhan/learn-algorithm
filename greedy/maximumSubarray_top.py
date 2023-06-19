'''
   (Greedy) leetcode: 53. Maximum Subarray (medium)

   Given an integer array `nums`, find the subarray with the largest sum, and return its sum.
   

   Example 1:
      Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
      Output: 6
      Explanation: The subarray [4,-1,2,1] has the largest sum 6.

   Example 2:
      Input: nums = [1]
      Output: 1
      Explanation: The subarray [1] has the largest sum 1.

   Example 3:
      Input: nums = [5,4,-1,7,8]
      Output: 23
      Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
   

   Constraints:
      - 1 <= nums.length <= 105
      - -104 <= nums[i] <= 104
   

   Follow up: 
      If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

   ===============================================================
   
   Solution by top submitted solution by others: 

   Leetcode submission:
      runtime: 640 ms, beats 98.65%
      memory: 30.9 MB, beats 38.29%


'''
# From the top solution that beats 98.50%
def maxSubarray(nums):
   currSum = 0
   maxSum = nums[0]

   for n in nums:
      if n > currSum and currSum < 0:
            currSum = n
      else:
            currSum += n
      print('currSum', currSum, 'maxSum', maxSum)
      if currSum > maxSum:
            maxSum = currSum
   return maxSum
'''
[-2,1,-3,4,-1,2,1,-5,4]
-2 1 1 2 2 3 4 4
c = -1
m = 4

'''

n1 = [-2,1,-3,4,-1,2,1,-5,4] # expect: 6
n2 = [1] # expect: 1
n3 = [5,4,-1,7,8] # expect: 23
n4 = [-2,-4,-1,-3] # expect: -1
n5 = [-1,-2] # expect: -1, output -2

print('RESULT :', maxSubarray(n1))
'''

'''