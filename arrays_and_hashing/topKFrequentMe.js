// Arrays & Hasing

/*
   LeetCode Top K Frequent Elements (medium)

   Given an integer array `nums` and an integer `k`, return the k most frequent elements. You may return the answer in any order.

   Example 1:

   Input: nums = [1,1,1,2,2,3], k = 2
   Output: [1,2]
   Example 2:

   Input: nums = [1], k = 1
   Output: [1]
   

   Constraints:

   1 <= nums.length <= 105
   -104 <= nums[i] <= 104
   k is in the range [1, the number of unique elements in the array].
   It is guaranteed that the answer is unique.
   

   Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

   LeetCode submission:
      probably O(n) 
      Runtime: 87 ms, beats 26.83%
      Memory: 50.1 MB, beats 7.28%

*/

function topKFrequent(nums, k) {
   let most = 0;
   let numCount = {}; // {num: count}
   let countNum = {}; // {count: num}
   let result = [];
   // loop untuk ambil count paling tinggi dan count tiap num
   for (let i = 0; i < nums.length; i++) {
      const n = nums[i];
      if (numCount[n] === undefined) {
         numCount[n] = 1;
         if (most === 0) most = 1;
         continue;
      }
      numCount[n] += 1;
      if (numCount[n] > most) most = numCount[n];
   }
   // isi count num
   for (let [n, c] of Object.entries(numCount)) {
      n = Number(n);
      if (countNum[c] !== undefined) {
         if(typeof countNum[c] === 'number') {
            countNum[c] = [countNum[c], n]
         } else {
            countNum[c] = [...countNum[c], n];
         }
      } else {
         countNum[c] = n;
      }
   }
   // isi result dengan num dengan count tertinggi hingga terendah, jika result sudah penuh maka return;
   while (most !== 0) {
      if (countNum[most] === undefined) {
         most--; continue;
      } else {
         // jika array
         if (typeof countNum[most] === 'object') {
            result.push(...countNum[most]);
         } else {
            result.push(Number(countNum[most]));
         }
      }

      if (result.length === k) return result;

      most--;

   }
   return result;
}
const nums1 = [1,1,1,2,2,3]; const k1 = 2; // expected: [1,2]
const nums2 = [1,4,1,1,7,3,5,3,3,1,1]; const k2 = 3; // expected: [1,2]
const nums3 = [1,2]; const k3 = 2;
const nums4 = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]; const k4 = 10;
console.log('topKFrequent', topKFrequent(nums4, k4));