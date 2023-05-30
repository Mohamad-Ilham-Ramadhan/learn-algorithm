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

  Solution:
    sort the candidates first 
    use backtracking to get all unique combinations

    without sorting: 
      check all posibbles combinations
      it turns out to be faster

  Leetcod submission:
    #1 (with sorting)
      - Runtime: 80 ms, beats 49.13%
      - Memory: 44.5 MB, beats 97.89%
      # attempt #2
      - Runtime: 83 ms, beats 36.19%
      - Memory: 44.7 MB, beats 92.58%
    #2 (without sorting)
      - Runtime: 76 ms, beats 65.98%
      - Memory: 45 MB, beats 80.66%
      # attempt #2
      - Runtime: 74 ms, beats 74.97%
      - Memory: 44.8 MB, beats 92.58%
*/

// #1 with sorting
function combinationSum(candidates, target) {
   candidates.sort( (a,b) => a - b);
   let result = [];
 
   function backtrack(sumArr, sum, index) {
     for (let i = index; i < candidates.length; i++) {
       const n = candidates[i];
       if (sum + n === target) {
         result.push(sumArr.concat(n));
         return;
       }
       if (sum + n > target) return;
       backtrack(sumArr.concat(n), sum + n, i);
     }
   }
 
   for (let i = 0; i < candidates.length; i++) {
     const n = candidates[i];
     console.log('n', n);
     if (n === target) {
       result.push([n]);
       return result;
     }
     if (n > target) return result;
     backtrack([].concat(n), n, i);
 
   }
   return result;
 }
 
 // #2 without sorting
 function combinationSumWithout(candidates, target) {
   let result = [];
 
   function backtrack(sumArr, sum, index) {
     for (let i = index; i < candidates.length; i++) {
       const n = candidates[i];
       if (sum + n === target) {
         result.push(sumArr.concat(n));
         return;
       }
       if (sum + n < target) {
         backtrack(sumArr.concat(n), sum + n, i);
       }
     }
   }
 
   for (let i = 0; i < candidates.length; i++) {
     const n = candidates[i];
     console.log('n', n);
     if (n === target) {
       result.push([n]);
     }
     if (n < target) {
       backtrack([].concat(n), n, i);
     }
   }
   return result;
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
 console.log('RESULT: ', combinationSumWithout(candidates4, target4));