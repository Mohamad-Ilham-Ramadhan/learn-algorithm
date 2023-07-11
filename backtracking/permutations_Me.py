''' 
   (backtracking) leetcode: 46. Permutations (medium)

   Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


   Example 1:
      Input: nums = [1,2,3]
      Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

   Example 2:
      Input: nums = [0,1]
      Output: [[0,1],[1,0]]

   Example 3:
      Input: nums = [1]
      Output: [[1]]
   

   Constraints:
      - 1 <= nums.length <= 6
      - -10 <= nums[i] <= 10
      - All the integers of nums are unique.

   Related topics:

   ==========================================================================

   Solution by myself:
      backtracking 

   Leetcode submission: 
      #1
         runtime: 64 ms, beats 11,70%
         memory: 16.7 MB, beats 12.50% 

'''

# solution 1
def permute(nums): 
   permutations = []
   def dfs(arrRes, arrRemain):
      if len(arrRes) == len(nums): permutations.append(arrRes)

      for i in range(len(arrRemain)): 
         newArrRes = arrRes.copy() 
         newArrRes.append(arrRemain[i])
         newArrRemain = arrRemain.copy() 
         newArrRemain.pop(i)
         dfs(newArrRes, newArrRemain)
   
   dfs([], nums)
   return permutations

def solution2(nums): 
   permutations = []

   # s = set of index of nums, it means the num has been added
   def dfs(s, arr): 
      if len(arr) == len(nums): permutations.append(arr)

      for i in range(len(nums)): 
         pass
   
n1 = [1,2,3]
print('RESULT :', permute(n1))
'''
   1    2   3
  2 3
 3   2
'''