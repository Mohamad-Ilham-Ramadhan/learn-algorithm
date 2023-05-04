// Backtracking algorithm/technique 

/*
   LeetCode problem: Permutations Unique or Permutations II

   Given a collection of numbers, (nums), that might contain duplicates, return all possible unique permutations in any order.

   Example 1:
      Input: nums = [1,1,2]
      Output:
      [[1,1,2],
      [1,2,1],
      [2,1,1]]

   Example 2:
      Input: nums = [0,1]
      Output: [[0,1], [1,0]]
   
   Example 3:
      Input: nums = [1]
      Output: [[1]]

   Solution (By NeetCode):
      Using Tree 
                        root
                      /  |  \
                      1  2     3
                     /\  /\    /\
                    2 3  1 3  1  2
                    | |  | |  |  |
                    3 2  3 1  2  1
      Then remove duplicates permutation
*/

// Time Complexity: O(n!) the slowest time complexity.
var permute = function (nums) {
   function helper(nums) {
      if (nums.length === 1) { 
         // console.log('result', [nums]); 
         return [nums]; }
      let result = [];
      for (let i = 0; i < nums.length; i++) {
         // const permuRes = permute(nums.filter(n => n !== nums[i]));
         let newNums = Object.assign([], nums);
         for (let j = 0; j < nums.length; j++) {
            if (nums[j] === nums[i]) { 
               newNums.splice(j, 1);
               break;
            }
         }
         const permuRes = helper(newNums);
         permuRes.forEach(arr => {
            result.push([nums[i], ...arr]);
         });
      }
      // console.log('result', result);
      return result;
   }
   let result = helper(Object.assign([], nums));

   // remove duplicates permutation 
   const length = nums.length;
   for (let i = 0; i < result.length; i++) {
      const perm = result[i];
      for (let j = 0; j < result.length; j++) {
         // console.log('j result.length', result.length);
         if (i === j) continue;
         const perm2 = result[j];
         let match = true;
         for (let k = 0; k < length; k++) {
            if (perm[k] !== perm2[k]) { match = false; break;}
         }
         if (match) {
            // remove duplicates
            result.splice(j,1);
            j = 0;
         }
      }
   }
   return result;
};
// [1, [3,2], [2,3] ]
const nums = [1,2,3];
const numsDuplicates = [1,1,2];
const numsDuplicates2 = [1,1,0,0,1,-1,-1,1]; // time exceeded LeetCode test Error
console.log('permutations', permute());
// 2 = 5
// 3 = 19
// 4 = 83