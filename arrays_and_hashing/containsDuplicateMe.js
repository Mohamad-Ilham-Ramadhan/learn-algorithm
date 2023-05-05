// Arrays & Hasing 

/*
   LeetCode Problems: Contains Duplicate : 

   Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

   Example 1:
   Input: nums = [1,2,3,1]
   Output: true

   Example 2:
   Input: nums = [1,2,3,4]
   Output: false

   Example 3:
   Input: nums = [1,1,1,3,3,4,3,2,4,2]
   Output: true

   Constraints:
   - 1 <= nums.length <= 105
   - -109 <= nums[i] <= 109

   Solution by myself: 
      using hasing, 
      loop over n:  
         if hashObj[n[i]] !== undefined then true;
      return false; 

   Time Complexity of my solution is O(n)

   LeetCode submission:
      Runtime: 91 ms, beats 69.5%
      Memorry: 54.3 MB, beats 50.25%
*/

function containsDuplicate(nums) {
   let hashing = {};
   for (let i = 0; i < nums.length; i++) {
      if (hashing[nums[i]] !== undefined) return true;
      hashing[nums[i]] = true;
   }
   return false;
}
const nums1 = [1,2,3,1]; const nums2 = [1,2,3,4]; const nums3 = [1,1,1,3,3,4,3,2,4,2];
console.log('containsDuplicate', containsDuplicate(nums2));

// Using two pointers, the time complexity is O(n / 2)
/*
   LeetCode submission:
      Runtime: 98 ms, beats 49.40%. Memory: 54 MB, beats 56.78%
*/
function containsDuplicateTwoPointers(nums) {
   if (nums.length === 1) return false;
   let hashing = {};
   let j = nums.length - 1;
   for (let i = 0; i < Math.ceil(nums.length/2); i++) {
      if (hashing[nums[i]] !== undefined) return true;
      hashing[nums[i]] = true;
      if (j == i) break;
      if (hashing[nums[j]] !== undefined) return true;
      hashing[nums[j]] = true;
      if (j-1 === i ) break;
      j--;
   }
   return false;
}
console.log('containsDuplicateTwoPointers', containsDuplicateTwoPointers([1,5,3,4,7]));
/* 
   Brute force, time complexity is O(n^2)
   LeetCode submission: 
   Runtime: 5536 ms, beats 13.22%
   Memory: 48.7 MB, beats 99.66%
*/
function containsDuplicateBruteForce(nums) {
   for (var i = 0; i < nums.length - 1; i++) {
      for (var j = i + 1; j < nums.length; j++) {
         if (nums[i] === nums[j]) return true;
      }
   }
   return false;
}
console.log('containsDuplicateBruteForce', containsDuplicateBruteForce([1,2,3,1]));

