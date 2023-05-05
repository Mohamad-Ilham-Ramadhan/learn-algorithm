// Backtracking algorithm/technique 

/* 
   LeetCode problem: Permutations II

   Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.


   Example 1:
      Input: nums = [1,1,2]
      Output:
      [[1,1,2],
      [1,2,1],
      [2,1,1]]

   Example 2:
      Input: nums = [1,2,3]
      Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
   
   Example 3:
      Input: nums = [1]
      Output: [[1]]

   Solution by NeetCode:
      Using hashmap to store the remaining of numbers 
      Time complexity = O(n!)

   LeetCode submition result:
      Runtime: 77ms, beats 68.79%
      Memory: 44.5MB, beats 87.58%
*/

function permutations2(nums) {
   let result = [];
   let permutation = [];
   let count = {};
   for (let n of nums) {
      if (count[n] === undefined) {
         count[n] = 0;
      }
      count[n] += 1;
   }

   function dfs() {
      console.log('dfs called');
      if (permutation.length === nums.length) { 
         result.push(permutation.slice());
         return;
      }
      for (let num in count) {
         if (count[num] > 0) {
            permutation.push(num);
            count[num] -= 1;

            dfs();

            count[num] += 1;
            permutation.pop();
         }
      }
   }
   dfs();
   console.log('count: ', count);
   return result;
}
/*
   {1: 2, 2: 1}
   perm = [1]
   count = { 1: 1, 2: 1}
   res = [[1,1,2], [1,2,1],]
*/

console.log('permutations', permutations2([1,1,2]));