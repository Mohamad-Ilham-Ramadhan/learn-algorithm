'''
   (backtracking) leetcode: 78. Subsets (medium)

   Given an integer array nums of unique elements, return all possible subsets [A subset of an array is a selection of elements (possibly none) of the array.] (the power set).

   The solution set must not contain duplicate subsets. Return the solution in any order.

   

   Example 1:
      Input: nums = [1,2,3]
      Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

   Example 2:
      Input: nums = [0]
      Output: [[],[0]]
   

   Constraints:
      - 1 <= nums.length <= 10
      - -10 <= nums[i] <= 10
      - All the numbers of nums are unique.

   Related Topics:
      (Array) (Backtracking) (Bit Manipulation)

   ============================================================= 

   Solution by myself:
      backtracking 

   Leetcode submission: 
      runtime: 48 ms, beats 68.37% 
      memory: 16.4 MB, beats 80.90%

'''
def subsets(nums): 
   result = []
   def dfs(start, subset): 
      result.append(subset)
      for i in range(start, len(nums)):
         newSet = subset.copy()
         newSet.append(nums[i]) 
         dfs(i+1, newSet)
   dfs(0, [])
   return result
'''
            []
          1     2   3
         2 3    3
'''
n1 = [1,2,3]
print('RESULT :', subsets([0]))