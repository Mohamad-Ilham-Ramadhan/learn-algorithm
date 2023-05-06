// Arrays & Hasing 

/*
   LeetCode Problems: Contains Duplicate (easy) : 

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

   Solution by NeetCode: 
      using hashset

   Time Complexity of my solution is O(n)

   LeetCode submission:
      Runtime: 82 ms, Beats 91.29% (FAST)
      Memory 54.7 MB, Beats 46.16%
*/

function containsDuplicate(nums) {
   if ((new Set(nums)).size !== nums.length) return true;
   return false;
}
console.log("ContainsDuplicate", containsDuplicate([1,2,3,5]));