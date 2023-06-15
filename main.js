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

  Solution by Stable Sort and simplified by me

  LeetCode submission: 
    #1 O(n log n)
      Runtime: 68 ms, beats 87.61%
      Memory: 44.4 MB, beats 27.75%
*/

function lengthOfLIS(nums) {
  let piles = [[nums[0]]];
  let x = 0;
  for (let i = 1; i < nums.length; i++) {
    x++;
    const n = nums[i];
    let isInserted = false;
    for (let j = 0; j < piles.length; j++) {
      x++;
      const p = piles[j];
      if (n <= p[p.length - 1]) {
        p.push(n);
        isInserted = true;
        break;
      }
    }
    if (!isInserted) {
      piles.push([n]);
    };
  }
  console.log('piles', piles, 'x', x);
  return piles.length;
}


// Example usage:
const arr = [9, 3, 7, 5, 2, 8, 1, 6, 4];
// const sortedArr = patienceSort(arr);
// console.log(sortedArr); // Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

const nums1 = [10,9,2,5,3,7,101,18];
const nums2 = [0,1,0,3,2,3];
const nums3 = [7,7,7,7,7,7,7];
const nums4 = [5,7,5,9,1,2,5,8,3,11,6,4];
const nums5 = [4,10,5,8,3,3,9,4,12,11];
console.log('RESULT : ', patienceSort(nums5));
// console.log('RESULT GPT: ', patienceSortGPT(cards));
// console.log('RESULT : ', lengthOfLIS(nums2));
