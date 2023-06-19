'''
   (Greedy) LeetCode: 55. Jump Game (medium)

   You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

   Return true if you can reach the last index, or false otherwise.



   Example 1:
      Input: nums = [2,3,1,1,4]
      Output: true
      Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

   Example 2:
      Input: nums = [3,2,1,0,4]
      Output: false
      Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


   Constraints:
      - 1 <= nums.length <= 104
      - 0 <= nums[i] <= 105

   ========================================

   Solution by NeetCode, code implementation by me.


   Leetcode submission:
      #1
         runtime: 533 ms, beats 23.75%
         memory: 28.8 MB, beats 5%
      #2 
         runtime: 522 ms, beats 27.47%
         memory: 28.9 MB, beats 5% 

'''
# implement NeetCode's explanation, using DP 
# attempt #2
def canJump2(nums):
   dp = [True] * len(nums)
   result = False
   def dfs(i):
      
      nonlocal result
      if result: return

      n = nums[i]
      print('i', i, 'n', n)
      if i + n >= len(nums) - 1:
         print('TRUEEE')
         result = True
         return True
      for j in range(i + n, i, -1):
         if not dp[j]: 
            dp[i] = False
            return
         if dfs(j):
            break
      
      dp[i] = False
   
   x = dfs(0)
   print('x', x)
   return result

# attempt #1
def canJump(nums):
   dp = [True] * len(nums)
   result = False
   def dfs(i):

      n = nums[i]
      print('i', i, 'n', n)
      if i + n >= len(nums) - 1:
         print('TRUEEE')
         nonlocal result
         result = True
         return True
      for j in range(i + n, i, -1):
         if not dp[j]: 
            dp[i] = False
            return
         if dfs(j):
            break
      
      dp[i] = False
   
   x = dfs(0)
   print('x', x)
   return result

n1 = [2,3,1,1,4] # true
n2 = [3,2,1,0,4] # false
n3 = [5,8,2,3,1,0,0,2,3,1] # true
n4 = [0] # true 
n5 = [1,0] # true
n6 = [2,0,0] # true, output false
n7 = [3,0,8,2,0,0,1] # true, output false
n8 = [3,11,0,8,2,0,0,1,2,1,4,0,1] # true, output false
n9 = [0,1] # false

print('RESULT : ', canJump(n9))