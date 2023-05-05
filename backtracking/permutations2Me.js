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

   Solution (By NeetCode) then modified by me:
      Using Tree
         - if array.length === 1 then return the array
         - place unique integers (unique array from duplicates array) for node 
         - then when get down, delete from the duplicates array of node's number 
         - recurse(deletedDuplicatesArray)
                        root [1, 1, 2]
                      /  |  
                      1  2    unique [1,2], non [1,1,2]
                     /\  |    
                    1 2  1  
                    | |  | 
                    2 1  1 
*/

/* 
   Solution by me modified from Permutations 1

   Time Complexity: O(n!) the slowest time complexity.

   LeetCode test:
      runtime: 71 ms beats 63.50%
      memory: 46.6 MB beats 8.33%

*/

/*
   Runtime: 113 ms, beats 31.83%
   Memory: 50.3 MB, beats 13.7%
*/
var permute = function (nums) {
   if (nums.length === 1) { return [nums]; }
   let result = [];
   let uniqueNums = nums.slice();
   for (let i = 0; i < uniqueNums.length; i++) {
      const filtered = uniqueNums.filter(n => n !== uniqueNums[i]).concat(uniqueNums[i]);
      if (filtered.length === uniqueNums.length) { continue;}
      uniqueNums = filtered;
      i = 0;
   }

   // loop yg unique
   for (let i = 0; i < uniqueNums.length; i++) {
      // masukin yang duplicate dikurang nums[i]
      let newNums = Object.assign([], nums);
      for (let j = 0; j < uniqueNums.length; j++) {
         if (uniqueNums[j] === uniqueNums[i]) {
            newNums.splice(newNums.indexOf(uniqueNums[j]), 1);
            break;
         }
      }
      const permuRes = permute(newNums);
      permuRes.forEach(permutation => {
         result.push([uniqueNums[i], ...permutation]);
      });
   }
   return result;
};
// [1, [3,2], [2,3] ]
const nums = [1, 2, 3];
const error = [-1,2,-1,2,1,-1,2,1];
console.log('permutations', permute([1,1,2]));
