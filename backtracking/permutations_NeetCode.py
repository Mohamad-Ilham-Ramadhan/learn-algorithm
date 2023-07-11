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

   Solution by NeetCode:

   Leetcode submission: 
      runtime: 52 ms, beats 78.48%
      memory: 16.4 MB, beats 73.14% 

'''

# solution 1
def permute(nums): 
   print(nums)
   result = [] 

   # base case
   if (len(nums) == 1): 
      return [nums[:]]

   for i in range(len(nums)): 
      n = nums.pop(0)
      perms = permute(nums)
      print('perms', perms)
      for perm in perms: 
         perm.append(n)

      result.extend(perms)
      nums.append(n)
   return result
   '''
      [3,1] n = 2, perms = [[3,2,1], [2,3,1]], result = [[3,2,1], [2,3,1]]
      [3] n = 1, perms = [[1,3], [3,1]], result = [1,3]


   '''
n1 = [1,2,3]
print('RESULT :', permute([1,2,3]))
'''
   1    2   3
  2 3
 3   2
'''