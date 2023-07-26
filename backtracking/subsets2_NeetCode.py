'''
   (backtracking) leetcode 90. Subsets II (medium)

   Given an integer array `nums` that may contain duplicates, return all possible subsets [A subset of an array is a selection of elements (possibly none) of the array.] (the power set).

   The solution set must not contain duplicate subsets. Return the solution in any order.

   

   Example 1:
      Input: nums = [1,2,2]
      Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

   Example 2:
      Input: nums = [0]
      Output: [[],[0]]
   

   Constraints:
      - 1 <= nums.length <= 10
      - -10 <= nums[i] <= 10

   Related Topics: 
      (Array) (Backtracking) (Bit Manipulation)
   ====================================================================================================

   Soluton by NeetCode:
      backtracking

   Leetcode submission
      runtime: 49 ms, beats 79.92%
      memory: 16.62 MB, beats 25.16%

'''
def subsetsWithDup(nums): 
   res = []
   nums.sort()

   def backtrack(i, subset): 
      if i == len(nums): 
         res.append(subset[::])
         return 
      
      # All subsets that don't include nums[i]
      subset.append(nums[i])
      backtrack(i+1, subset)
      subset.pop()

      # All subsets that don't include nums[i]
      while i + 1 < len(nums) and nums[i] == nums[i+1]:
         i += 1

      backtrack(i+1, subset)
   
   backtrack(0, [])
   return res

nums = [1,2,2,1] # [[],[1],[1,1],[1,1,2],[1,1,2,2],[1,2],[1,2,2],[2],[2,2]]
n2 = [1,2,2,3] # [[],[1],[1,2],[1,2,2],[1,2,2,3],[1,2,3],[1,3],[2],[2,2],[2,2,3],[2,3],[3]]
n3 = [1,2,2] # [[],[1],[1,2],[1,2,2],[2],[2,2]]

'''
'''
# print('RESULT :', subsetsWithDup(nums))
print('sol2', solution2(n3))