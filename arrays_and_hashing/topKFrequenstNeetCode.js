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

   Solution by NeetCode: https://www.youtube.com/watch?v=YPTqKIgVk-k

      Using bucket sort algorithm. Time complexity O(n):

      - store count of nums inside a hash
      - loop the hash and place each nums into the bucket
      - then loop the buckets from the greatest to the least
      - if result.length === k then return result 
      - add to the result 

      [1,1,1,2,2,100]

      bucket -->  (count)  |0|  1  | 2 | 3 | 4 | 5 | 6 | <--- from nums.length because the maximum count when nums only one
                  values   | |[100]|[2]|[1]|   |   |   |

   LeetCode submission:
      Runtime: 83 ms, beats 37%
      Memorry: 47.8 MB, beats 19.31%
*/

function topKFrequent(nums, k) {
   const result = [];
   const hash = {};
   const bucket = Array.from({length: nums.length});
   console.log('bucket intial', bucket.slice());
   for (let n of nums) {
      if (hash[n] === undefined) {
         hash[n] = 1;
      } else {
         hash[n] += 1;
      }
   }
   for (let [n, c] of Object.entries(hash)) {
      if (bucket[c] === undefined) {
         bucket[c] = [n];
      } else {
         bucket[c].push(n);
      }
   }
   console.log('hash', hash, 'bucket', bucket);
   for (let i = bucket.length - 1; i >= 0; i--) {
      if (bucket[i] === undefined) continue;
      for (let j = 0; j < bucket[i].length; j++) {
         result.push(bucket[i][j]);
         if (result.length === k) return result;
      }
   }
}
const nums1 = [1,1,1,2,2,3]; const k1 = 2; // expected: [1,2]
const nums2 = [1,4,1,1,7,3,5,3,3,1,1]; const k2 = 3; // expected: [1,2]
const nums3 = [1,2]; const k3 = 2;
const nums4 = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]; const k4 = 10;
const nums5 = [1]; const k5 = 1;
console.log('topKFrequent', topKFrequent(nums5, k5));