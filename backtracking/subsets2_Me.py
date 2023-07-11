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

   ====================================================================================================

   Soluton by myself:
      backtracking

   Leetcode submission
      runtime: 60 ms, beats 21.81%
      memory: 16.6 MB, beats 61.55%

'''
def subsetsWithDup(nums): 
   subsets = []
   def dfs(start, s): 
      subsets.append(s)
      v = set() # intuition
      for i in range(start, len(nums)): 
         if nums[i] in v: continue
         dfs(i+1, [*s, nums[i]])
         v.add(nums[i])
   dfs(0,[])
   return subsets

nums = [1,2,2,1] # [[],[1],[1,2],[1,2,2],[2],[2,2]]
'''
   [1,1,2,2]
   [1,1,2,2]
   []

'''
print('RESULT :', subsetsWithDup(nums))