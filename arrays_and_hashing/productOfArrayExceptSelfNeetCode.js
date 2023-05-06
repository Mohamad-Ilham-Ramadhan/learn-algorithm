/*
LeetCode problem: Product of Array Except Self (medium) : https://leetcode.com/problems/product-of-array-except-self/

   Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product(dikalikan) of all the elements of `nums` except `nums[i]`.

   The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

   You must write an algorithm that runs in O(n) time and without using the division operation.

   

   Example 1:
      Input: nums = [1,2,3,4]
      Output: [24,12,8,6]

   Example 2:
      Input: nums = [-1,1,0,-3,3]
      Output: [0,0,9,0,0]
   

   Constraints:
   - 2 <= nums.length <= 105
   - -30 <= nums[i] <= 30
   - The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
   

   Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

   Solution by NeetCode: https://www.youtube.com/watch?v=bNvIQI2wAjk
      #1
      create prefix and suffix
      nums     [1,2,3,4]
      prefix   [1,1,2,6]
      suffix   [24,12,4,1]
      result   [24,12,8,6]

      but this still requires extra space complexity to store prefix and suffix
      we can put the prefix and suffix calculation directly into the result array

      --------> prefix
      <-------- suffix
      [1,2,3,4]
      [1,1,2,6] <--- result of prefix loops 
      [24,12,8,6] <--- result of suffix loops

      Time complexity: O(n * 3). Space complexity: O(n * 2) because result array don't count

      LeetCode submission:
         Runtime: 554 ms, beats 11.12%
         Memory: 54.6 MB, beats 49.47%

      #2
      We don't need prefix and suffix arrays for now. Instead we just calculate the prefix and suffix in the result array.

      Time complexity: O(n * 2). Space complexity: O(1) because result array don't count

      LeetCode submission:
         Runtime: 102 ms, beats 68.71%
         Memory: 55.5 MB, beats 30.24%
*/

function productExceptSelf(nums) {
   let result = [];
   let prefix = [];
   let suffix = [];

   // collect prefix
   let lastPrefix = 1;
   for (let i = -1; i < nums.length - 1; i++) {
      const n = nums[i];
      if (n === undefined) { 
         prefix.push(1) 
      } else {
         lastPrefix = lastPrefix * n;
         prefix.push(lastPrefix);
      }
   }
   // collect suffix 
   let lastSuffix = 1;
   for (let i = nums.length; i >= 1; i--) {
      const n = nums[i];
      if (n === undefined) { 
         suffix.push(1) 
      } else {
         lastSuffix = lastSuffix * n;
         suffix.unshift(lastSuffix);
      }
   }
   // calculate the result;
   for (let i = 0; i < nums.length; i++) {
      result[i] = prefix[i] * suffix[i];
   }
   return result
}
const nums = [1,2,3,4];
console.log('productExecptSelf', productExceptSelf(nums));
console.log('productExecptSelf2', productExceptSelf2(nums));
function productExceptSelf2(nums) {
   let result = [];

   // collect prefix
   let lastPrefix = 1;
   for (let i = -1; i < nums.length - 1; i++) {
      const n = nums[i];
      if (n === undefined) { 
         result.push(1) 
      } else {
         lastPrefix = lastPrefix * n;
         result.push(lastPrefix);
      }
   }
   // collect suffix 
   let lastSuffix = 1;
   for (let i = nums.length - 1; i >= 1; i--) {
      const n = nums[i];
      lastSuffix = lastSuffix * n;
      result[i-1] = lastSuffix * result[i-1];
   }
   return result
}