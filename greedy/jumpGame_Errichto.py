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

   Solution by Errichto, convert by me from c++ to python


   Leetcode submission:
      #1 
         runtime: 507 ms, beats 32.2%
         memory: 17.6 MB, beats 81.16%
      #2 
         runtime: 479 ms, beats 57.55%
         memory: 17.8 MB, beats 9.16%


'''

def canJump(nums):
   # Errichto's
   n = len(nums)
   can_reach = 0
   i = 0
   while i <= can_reach:
      # if (i == n - 1):
      # attempt #2 (modified by me)
      if (i == n - 1 or can_reach >= n - 1):
            return True 
      can_reach = max(can_reach, i + nums[i])
      i += 1
   return False

'''
   cr = 2
   cr = 4
'''
n1 = [2,3,1,1,4] # true
n2 = [3,2,1,0,4] # false
n3 = [5,8,2,3,1,0,0,2,3,1] # true
n4 = [0] # true 
n5 = [1,0] # true
n6 = [2,0,0] # true, output false
n7 = [3,0,8,2,0,0,1] # true, output false
n8 = [3,11,0,8,2,0,0,1,2,1,4,0,1] # true, output false
x8 = [8,2,0,0,1,2,1,4,0,1]
'''
[false,false,false,true,true,true,true,false, true]
'''
n9 = [0,1] # false
print('RESULT : ', canJump(n1)) 