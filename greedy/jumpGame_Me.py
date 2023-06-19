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

   Solution by me:

   Leetcode submission:
      #1
         runtime: 3999 ms, 11.27%
         memory: 18.3 MB, 5.88%
'''
# solution #1 (maybe this solution is using brute force)
def canJump(nums):
   visited = set()
   i = 0
   while (i < len(nums) - 1 and i >= 0):
      if i in visited: return False
      visited.add(i) 
      n = nums[i]
      temp = i
      print('i', i, 'n', n, 'i + n', i + n, 'len(nums) - 1', len(nums) - 1, i + n >= len(nums) - 1)
      if i + n >= len(nums) - 1 : return True
      for j in range(i + n, i, -1):
         n2 = nums[j]
         print('j', j, 'n2', n2)
         if n2 == 0 or j in visited: continue
         else: 
            i = j
            break
      if i == temp: 
         i -= 1
         print('mundur')
   if i == -1: return False
   return True 

n1 = [2,3,1,1,4] # true
n2 = [3,2,1,0,4] # false
n3 = [5,8,2,3,1,0,0,2,3,1] # true
n4 = [0] # true 
n5 = [1,0] # true
n6 = [2,0,0] # true, output false
n7 = [3,0,8,2,0,0,1] # true, output false
n8 = [3,11,0,8,2,0,0,1,2,1,4,0,1] # true, output false
n9 = [0,1] # 

print('RESULT : ', canJump(n9))