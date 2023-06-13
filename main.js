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

  LeetCode submission: 
    #1 O(n^2)
      Runtime: 354 ms, beats 9.56%
      Memory: 43.6 MB, beats 83.14%
*/

function lengthOfLIS(nums) {
  /* 
    [10,9,2,5,3,7,101,18]
    18 -> 1
    101 -> 1
    7 -> 2
    3 -> 3
    5 -> 3
    2 -> 4
    9 -> 2
    10 -> 2

    [0,1,0,3,2,3]
    3 -> 1
    2 -> 2
    3 -> 1
    0 -> 3
    1 -> 3
    0 -> 4
  */
  // attempt #1 [start]
  let result = -Infinity;
  let dp = [];
  for (let i = nums.length - 1; i >= 0; i--) {
    const n1 = nums[i];
    let max = 1;
    for (let j = i+1; j < nums.length; j++) {
      const n2 = nums[j];
      if (n2 > n1) {
        max = Math.max(max, dp[j]+1);
      }
    }
    dp[i] = max;
    result = Math.max(result, max);
  }
  console.log('dp', dp);
  return result;  
  // attempt #1 [start]
}
const nums1 = [10,9,2,5,3,7,101,18]; // expect: 4
const nums2 = [0,1,0,3,2,3]; // expect: 4
const nums3 = [7,7,7,7,7,7,7]; // expect: 1

const start = Date.now();
console.log('RESULT :', lengthOfLIS(nums1));
console.log('RUNTIME :', Date.now() - start);