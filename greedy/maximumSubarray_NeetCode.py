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
   
   Solution by NeetCode: 


   Leetcode submission:
      runtime: 689 ms, beats 81.49%
      memory: 31.1 MB, beats 15%

'''
# NeetCode solution: O(n)
def maxSubarray(nums):
   maxSub = nums[0]
   curSum = 0 

   for n in nums: 
      if curSum < 0:
         curSum = 0
      curSum += n
      maxSub = max(maxSub, curSum)
   
   return maxSub


n1 = [-2,1,-3,4,-1,2,1,-5,4] # expect: 6
n2 = [1] # expect: 1
n3 = [5,4,-1,7,8] # expect: 23
n4 = [-2,-4,-1,-3] # expect: -1
n5 = [-1,-2] # expect: -1, output -2

print('RESULT :', maxSubarray(n1))
'''

'''