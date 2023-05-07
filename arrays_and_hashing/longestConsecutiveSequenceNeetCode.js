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

   Solution by NeetCode: https://www.youtube.com/watch?v=P6RZZMu_maU
      the solution is we check the previous number of the number if doesn't exist then the number is the start of the sequence.
      we count until the next number is not or it is another start of sequence 

      [100,4,200,1,2,3]

      <-- 1 2 3 4 .....  100 .... 200 --->

      first we convert the nums into the sets so wen't we check the previous/next number we get O(1) time complexity.

   LeetCode submission:
      Runtime: 91 ms, beats 96.19%
      Memory: 50.5 MB, beats 73.54% 
*/

function longestConsecutive(nums) {
   nums = new Set(nums);
   let longest = 0;
   for (let n of nums) {
      // if num is the start of a sequence then we count the sequence
      if (!nums.has(n-1)) {
         let newLongest = 1;
         while (nums.has(n+1)) {
            newLongest++;
            n = n + 1;
         }
         longest = Math.max(newLongest, longest);
      }
   }
   return longest;
}
const nums1 = [100,4,200,1,3,2]; // result: 4, -> [1,2,3,4]
const nums2 = [0,3,7,2,5,8,4,6,0,1]; // result: 4, -> [0,1,2,3,4,5,6,7,8]
console.log(longestConsecutive(nums2));