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
      #1
         runtime: 68 ms, beats 81.69%
         memory: 16.6 MB beats 20.3%
      #2 
         runtime: 67 ms, beats 83.05%
         memory: 16.42 MB, beats 54.30%
   
'''
def combinationSum2(candidates, target):
   candidates.sort() 

   combinations = []

   def backtrack(i, combination, sum):
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
         backtrack(j+1,[*combination, candidates[j]], sum+candidates[j] )

   backtrack(0,[],0)
   return combinations

# build the combinations from return value
def solution2(candidates, target):
   candidates.sort() 

   def backtrack(i, sum):
      # print('i', i)
      if sum == target: 
         print('sum', sum)
         return [[]]
      if sum > target or i == len(candidates) or (sum + candidates[i]) > target: 
         return False

      last = 0
      result = []
      for j in range(i, len(candidates)): 
         # print('j', j)
         if candidates[j] == last : continue 
         last = candidates[j]
         combinations = backtrack(j+1, sum+candidates[j] )
         print('i',i,  candidates[i], 'candidates[j]', candidates[j])
         print('combinations', combinations)
         if combinations == False: continue
         for comb in combinations: 
            comb.append(candidates[j])
            result.append(comb)

      return result 
   
   result = backtrack(0,0)
   return result


c1 = [10,1,2,7,6,1,5]; t1 = 8
c2 = [2,5,2,1,2]; t2 = 5
print('RESULT :', solution2(c1, t1))
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