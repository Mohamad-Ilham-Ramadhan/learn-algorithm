// Arrays & Hasing

/*
   LeetCode Two Sum (easy)

   Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

   You may assume that each input would have exactly one solution, and you may not use the same element twice.

   You can return the answer in any order.

   Example 1:
      Input: nums = [2,7,11,15], target = 9
      Output: [0,1]
      Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

   Example 2:
      Input: nums = [3,2,4], target = 6
      Output: [1,2]

   Example 3:
      Input: nums = [3,3], target = 6
      Output: [0,1]
   
   Constraints:
      2 <= nums.length <= 104
      -109 <= nums[i] <= 109
      -109 <= target <= 109

   Solution by NeetCode:
      Using a hashmap of previous the numbers as keys and its index as values in iteration.
      check current hashmap[ target - nums[i] ], if exist then it is the result
      if not then save the current nums[i] in the hashmap, hashmap[nums[i]] = i;

      Time Complexity: O(n)

   LeetCode submission:
      Runtime: 60 ms, beats 89.19%.
      Memory: 42.5 MB, beats 63.14%.
      
*/
function twoSum(nums, target) {
   const hashmap = {}; // pake object daripada map karena keysnya integer, object lebih cepat jike kondisi begini
   for (let i = 0; i < nums.length; i++) {
      if (hashmap[target - nums[i]] !== undefined) {
         return [hashmap[target - nums[i]], i];
      }
      hashmap[nums[i]] = i;
   }
}
const nums = [2,7,11,15]; const target = 9;
const nums2 = [2,7,14,2]; const target2 = 4;
console.log('two sum', twoSum(nums2, target2))