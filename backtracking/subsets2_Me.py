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

   Soluton by myself:
      backtracking

   Leetcode submission
      #1 
         runtime: 60 ms, beats 21.81%
         memory: 16.6 MB, beats 61.55%
      #2 
         runtime: 52 ms, beats 66.86%
         memory: 16.16 MB, beats 62.27%

'''
def subsetsWithDup(nums): 
   nums.sort()
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

# build subset with return value
def solution2(nums): 
   nums.sort() 
   def dfs(start):
      subset = []
      s = set() # no duplicate num 
      for i in range(start, len(nums)): 
         n = nums[i]
         if n in s: continue 
         s.add(n)
         res = dfs(i+1)
         for j in res:
            j.append(n)
            subset.append(j)
         subset.append([n])

      return subset
   result = dfs(0)
   result.append([])
   return result

nums = [1,2,2,1] # [[],[1],[1,1],[1,1,2],[1,1,2,2],[1,2],[1,2,2],[2],[2,2]]
n2 = [1,2,2,3] # [[],[1],[1,2],[1,2,2],[1,2,2,3],[1,2,3],[1,3],[2],[2,2],[2,2,3],[2,3],[3]]
n3 = [1,2,2] # [[],[1],[1,2],[1,2,2],[2],[2,2]]

'''
'''
# print('RESULT :', subsetsWithDup(nums))
print('sol2', solution2(n3))