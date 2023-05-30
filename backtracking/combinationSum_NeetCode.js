/*
  leetcode: 39. Combination Sum (medium)

  Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.

  The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the 
  frequency
  of at least one of the chosen numbers is different.

  The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

  

  Example 1:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.

  Example 2:
    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]

  Example 3:
    Input: candidates = [2], target = 1
    Output: []
  

  Constraints:
    - 1 <= candidates.length <= 30
    - 2 <= candidates[i] <= 40
    - All elements of candidates are distinct.
    - 1 <= target <= 40

  Solution by NeetCode

  Leetcod submission:
    #1
    - Runtime: 74 ms, beats 74.97%
    - Memory: 45 MB, beats 80.66%
*/

function combinationSum(candidates, target) {
   let res = [];
 
   function dfs(i, cur, total) {
     if (total === target) {
       res.push(cur.slice());
       return;
     }
     if (i >= candidates.length || total > target) return;
 
     cur.push(candidates[i]);
     dfs(i, cur, total + candidates[i]);
     cur.pop();
     dfs(i + 1, cur, total);
   }
 
   dfs(0, [], 0);
   return res;
 }
 
 const candidates1 = [2, 3, 6, 7];
 const target1 = 7; // [[2,2,3],[7]]
 const candidates2 = [2,3,5];
 const target2 = 8; // [[2,2,2,2],[2,3,3],[3,5]]
 const candidates3 = [2]; 
 const target3 = 1; // []
 const candidates4 = [2,3]; 
 const target4 = 2; // [[2]]
 const candidates5 = [8,7,4,3];
 const target5 = 11; // [[3,4,4], [3,8], [4,7]]
 console.log('RESULT: ', combinationSum(candidates5, target5));