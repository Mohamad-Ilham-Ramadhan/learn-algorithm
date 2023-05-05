// Backtracking algorithm/technique 



/*
   LeetCode problem: Permutations 

   Given an array (nums) of distinct integers, returns all the posibble permutations. You can return an answer in any order.

   Example 1:
      Input: nums = [1,2,3]
      Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

   Example 2:
      Input: nums = [0,1]
      Output: [[0,1], [1,0]]
   
   Example 3:
      Input: nums = [1]
      Output: [[1]]

   Solution (By NeetCode): https://www.youtube.com/watch?v=s7AvT7cGdSo
      Using Tree 
                        root
                      /  |  \
                      1  2     3
                     /\  /\    /\
                    2 3  1 3  1  2
                    | |  | |  |  |
                    3 2  3 1  2  1
*/

/* 
   Solution by me, I don't copy paste from chatGPT but accidentally it is same with solutin from chatGPT

   Time Complexity: O(n!) the slowest time complexity.

   LeetCode test:
      runtime: 71 ms beats 63.50%
      memory: 46.6 MB beats 8.33%

   EDIT: Ternyata my solution mirip dengan punya NeetCode
*/
var permute = function (nums) {
   if (nums.length === 1) { return [nums]; }
   let result = [];
   for (let i = 0; i < nums.length; i++) {
      const permuRes = permute(nums.filter(n => n !== nums[i]));
      permuRes.forEach(arr => {
         result.push([nums[i], ...arr]);
      });
   }
   return result;
};
// [1, [3,2], [2,3] ]
const nums = [1,2,3,4];
console.log('permutations', permute(nums));
// 2 = 5
// 3 = 19
// 4 = 83