/*
  300. Longest Increasing Subsequence (medium)

  Given an integer array `nums`, return the length of the longest strictly increasing subsequence.


  Example 1:
    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

  Example 2:
    Input: nums = [0,1,0,3,2,3]
    Output: 4

  Example 3:
    Input: nums = [7,7,7,7,7,7,7]
    Output: 1
  

  Constraints:
    - 1 <= nums.length <= 2500
    - -104 <= nums[i] <= 104
  

  Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

  NeetCode solution

  LeetCode submission: 
    #1 O(n^2)
      Runtime: 137 ms, beats 77.70%
      Memory: 43.8 MB, beats 73.80%
*/

function lengthOfLIS(nums) {
   const LIS = [];
   for (let i = 0; i < nums.length; i++) {
     LIS[i] = 1;
   }
 
   /*
     for i in range(len(nums) - 1, -1, -1):
     for j in range(i + 1, len(nums)):
       if (nums[i] < nums[j]):
         LIS[i] = max(LIS[i], 1 + LIS[j])
 
   return max(LIS)
   */ 
  for (let i = nums.length - 1; i >= 0; i--) {
     for (let j = i + 1; j < nums.length; j++) {
       if (nums[i] < nums[j]) LIS[i] = Math.max(LIS[i], 1 + LIS[j])
     }
  }
  return Math.max(...LIS);
 }
 const nums1 = [10,9,2,5,3,7,101,18];
 const nums2 = [0,1,0,3,2,3];
 console.log('RESULT : ', lengthOfLIS(nums2));