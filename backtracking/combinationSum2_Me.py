'''
   (backtracking) leetcode 40. Combination Sum II (medium)

   Given a collection of candidate numbers (`candidates`) and a target number (target), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

   Each number in `candidates` may only be used once in the combination.

   Note: The solution set must not contain duplicate combinations.

   

   Example 1:
      Input: candidates = [10,1,2,7,6,1,5], target = 8
      Output: 
      [
      [1,1,6],
      [1,2,5],
      [1,7],
      [2,6]
      ]

   Example 2:
      Input: candidates = [2,5,2,1,2], target = 5
      Output: 
      [
      [1,2,2],
      [5]
      ]
   

   Constraints:
      - 1 <= candidates.length <= 100
      - 1 <= candidates[i] <= 50
      - 1 <= target <= 30

   Related Topics: 
      (Array) (Backtracking)

   ==================================================================================

   Solution by myself
      backtracking
   
   leetcode submission:
      runtime: 68 ms, 81.69%
      memory: 16.6 MB beats 20.3%
   
'''
def combinationSum2(candidates, target):
   candidates.sort() 

   combinations = []

   def dfs(i, combination, sum):
      # print('i', i)
      if sum == target: 
         combinations.append(combination)
         return
      if sum > target or i == len(candidates) or (sum + candidates[i]) > target: 
         return

      last = 0
      for j in range(i, len(candidates)): 
         # print('j', j)
         if candidates[j] == last : continue 
         last = candidates[j]
         dfs(j+1,[*combination, candidates[j]], sum+candidates[j] )

   dfs(0,[],0)
   return combinations

c1 = [10,1,2,7,6,1,5]; t1 = 8
c2 = [2,5,2,1,2]; t2 = 5
print('RESULT :', combinationSum2(c2, t2))
'''Input: candidates = [10,1,2,7,6,1,5], target = 8
      Output: 
      [
      [1,1,6],
      [1,2,5],
      [1,7],
      [2,6]
      ]

      1+2+5 ok       6+1+5 no
      1+7 ok         6+5 no
      1+6+1 ok       1+5 no
      1+1+5 no       5 no
      2+7 no
      2+6 ok
      2+1+5 ok
      2+5 no 
      7+6 no
      7+1 ok
      7+5 no

   [1,1,2,5,6,7,10]
   1+1+6    2+6
   1+2+5    
   1+7
'''