/*
   LeetCode Problem: Find Minimum in Rotated Sorted Array (medium)

   Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums` = [0,1,2,4,5,6,7] might become:

   [4,5,6,7,0,1,2] if it was rotated 4 times.
   [0,1,2,4,5,6,7] if it was rotated 7 times.
   Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

   Given the sorted rotated array nums of unique elements, return the minimum element of this array.

   You must write an algorithm that runs in O(log n) time.

   
   Example 1:
      Input: nums = [3,4,5,1,2]
      Output: 1
      Explanation: The original array was [1,2,3,4,5] rotated 3 times.

   Example 2:
      Input: nums = [4,5,6,7,0,1,2]
      Output: 0
      Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

   Example 3:
      Input: nums = [11,13,15,17]
      Output: 11
      Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

   Constraints:
      n == nums.length
      1 <= n <= 5000
      -5000 <= nums[i] <= 5000
      All the integers of nums are unique.
      nums is sorted and rotated between 1 and n times.

   LeetCode by Myself: 
      # naive O(n)
      Runtime: 65 ms, beats 23.32%
      Memory: 42.1 MB, beats 45.68%

      # binary search O(log n) + O(3) || O(3)
         Runtime: 55 ms, beatsh 77.69%
         Memory: 42.3 MB, beats 24.97%
*/

function findMinimumInRotatedSortedArray_naive(nums) {
   // wkwkwk gak pake binary search
   return Math.min(...nums);
}

// using binary search  O(log n)
function findMinimumInRotatedSortedArray(nums) {
   if (nums.length === 1) {
      return nums[0];
   } 
   // else if(nums.length <= 3) {
   //    return Math.min(...nums);
   // }
   let l = 0; // left index
   let r = nums.length - 1; // right index
   let m = Math.floor((nums.length - 1) / 2); // mid index
   let x = 0; // for debugging, escape from infinite loop
   console.log(nums, nums[4]);
   let left; let mid; let right;
   while (l !== m || m !== r || r !== l) {
      if (x === 17) break;
      left = nums[l]; mid = nums[m]; right = nums[r];
      console.log('before', l, left, '|', m, mid,'|',r, right);
      if ( (left < mid && left < right) || (left > mid && left > right) ) {
         // go left
         console.log('go left');
         r = m;
         m = Math.floor((l + r) / 2)
      } else {
         // go right
         console.log('go right');
         l = m;
         if (right < left) {
            m = Math.ceil((l + r) / 2)
         } else {
            m = Math.floor((l + r) / 2);
         }
         // console.log('go right', l, m);
      }
      x++;
   }
   console.log(l,m,r, nums);
   return nums[m];
} // [9,0,8]
const nums2 = [4,5,6,7,0,1,2];
const nums3 = [6,7,0,1,2,4,5];
const nums4 = [1,2,3,4,5,6,0];
const nums5 = [33,32,0,2,3,4,6,7,22];
const nums6 = [666];
const nums7 = [3,0];
const nums8 = [1,2,3];
const nums9 = [2,1,3]
console.log(findMinimumInRotatedSortedArray(nums2));