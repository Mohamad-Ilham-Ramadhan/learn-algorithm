/*
   LeetCode problem: Longest Consecutive Sequence (Hard-Medium)

   Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

   == YOU MUST WRITE AN ALGORITHM THAT RUNS IN O(N) TIME. ==

   Example 1:

   Input: nums = [100,4,200,1,3,2]
   Output: 4
   Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
   Example 2:

   Input: nums = [0,3,7,2,5,8,4,6,0,1]
   Output: 9
   

   Constraints:

   0 <= nums.length <= 105
   -109 <= nums[i] <= 109

   Solution by myself:
      I don't know, is it run in the O(n) because It use sorting which is O(n log n) but the sorting algorithm is built-in so I don't know is it count as O(n log n) or not.

   LeetCode submission:
      Runtime: 105 ms, beats 76.17%
      Memory: 50.5 MB, beats 93.99% 
*/

function longestConsecutive(nums) {
   if (nums.length === 0) return 0;
   if (nums.length === 1) return 1;
   nums.sort( (a,b) => a - b);
   let result = 1;
   let prev = nums[0];
   let streak = 1;
   for (let i = 1; i < nums.length; i++) {
      if (nums[i] === prev) continue;
      if (nums[i] - 1 === prev) {
         if (++streak > result) {
            result = streak;
         }
      } else {
         streak = 1;
      }
      prev = nums[i];
   }
   return result;
}
const nums1 = [100,4,200,1,3,2]; // result: 4, -> [1,2,3,4]
const nums2 = [0,3,7,2,5,8,4,6,0,1]; // result: 4, -> [0,1,2,3,4,5,6,7,8]
console.log(longestConsecutive([1,2,0,1]));