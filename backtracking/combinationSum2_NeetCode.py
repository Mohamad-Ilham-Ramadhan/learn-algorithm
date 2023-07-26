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

   Solution by NeetCode
      backtracking
   
   leetcode submission:
      runtime: 88 ms, beats 67.23%
      memory: 16.50 MB beats 20.94%
   
'''
def combinationSum2(candidates, target):
   candidates.sort() 

   res = []
   def backtrack(cur, pos, target): 
      if target == 0:
         res.append(cur.copy())
      if target <= 0:
         return

      prev = -1 
      for i in range(pos, len(candidates)): 
         if candidates[i] == prev: 
            continue 
         cur.append(candidates[i]) 
         backtrack(cur, i+1, target - candidates[i])
         cur.pop()
         prev = candidates[i]
   
   backtrack([], 0, target)
   return res


c1 = [10,1,2,7,6,1,5]; t1 = 8
c2 = [2,5,2,1,2]; t2 = 5
print('RESULT :', combinationSum2(c1, t1))
'''
   [[6]] -> [[6,1]] -> [[6,1,1]]
   Input: candidates = [10,1,2,7,6,1,5], target = 8
      [1,1,2,5,6,7,10]
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