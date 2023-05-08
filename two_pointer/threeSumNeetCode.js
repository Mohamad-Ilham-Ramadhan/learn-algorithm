/*
   LeetCode problem: 3Sum (medium)

   Given an integer array nums, return all the triplets` [nums[i], nums[j], nums[k]]` such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

   Notice that the solution set must not contain duplicate triplets.

   


   Example 1:
   Input: nums = [-1,0,1,2,-1,-4]
   Output: [[-1,-1,2],[-1,0,1]]
      Explanation: 
      nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
      nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
      nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
      The distinct triplets are [-1,0,1] and [-1,-1,2].
      Notice that the order of the output and the order of the triplets does not matter.

   Example 2:
      Input: nums = [0,1,1]
      Output: []
      Explanation: The only possible triplet does not sum up to 0.

      Example 3:
      Input: nums = [0,0,0]
      Output: [[0,0,0]]
      Explanation: The only possible triplet sums up to 0.
   


   Constraints:
      - 3 <= nums.length <= 3000
      - -105 <= nums[i] <= 105

   Solution by NeetCode: https://www.youtube.com/watch?v=jzZsG8n2R9A

   LeetCode submission: 
      Runtime: 174 ms , beats 91.6%
      Memorry: 58.5 MB, beats 30.79%

*/

function threeSum(nums) {
   // sort biar nyari combinasinya gampang tinggal geser j ke kanan dan k ke kiri
   nums.sort((a,b) => a-b);
   console.log(nums);
   let result = [];
   for (let i = 0; i < nums.length -2; i++) {
      if (i > 0 && nums[i] === nums[i - 1]) continue;
      let j = i + 1;
      let k = nums.length - 1;
      while( j < k) {
         const threeSum = nums[i] + nums[j] + nums[k];
         if (threeSum < 0) {
            j++;
         } else if (threeSum > 0) {
            k--;
         } else if (threeSum === 0) {
            // console.log('push', [nums[i], nums[j], nums[k]]);
            result.push([nums[i], nums[j], nums[k]]);
            j++;
            while (nums[j] == nums[j - 1] && j < k) {
               j++;
            }
         }
         // console.log('after', 'nums[i]',i, nums[i], 'nums[j]',j, nums[j], 'nums[k]',k, nums[k]);
      }
   }
   return result;
}
const nums1 = [-1,0,1,2,-1,-4];
const nums2 = [-1,0,1,2,-1,-4,-5,4,-3,1,-2,-9,5,8,9,7]; // [-9, -5, -4, -3, -2, -1, -1, 0, 1, 1, 2, 4, 5, 7, 8, 9]
const nums3 = [-2,0,0,2,2];
const nums4 = [-2,-3,0,0,-2];
console.log(threeSum(nums4));