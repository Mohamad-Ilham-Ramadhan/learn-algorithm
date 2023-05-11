/*
   LeetCode problem: Search in Rotated Sorted Array (medium)

   There is an integer array nums sorted in ascending order (with distinct values).

   Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` `(1 <= k < nums.length)` such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0,1,2,4,5,6,7`] might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

   Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

   You must write an algorithm with `O(log n)` runtime complexity.


   Example 1:
      Input: nums = [4,5,6,7,0,1,2], target = 0
      Output: 4
   Example 2:
      Input: nums = [4,5,6,7,0,1,2], target = 3
      Output: -1
   Example 3:
      Input: nums = [1], target = 0
      Output: -1

   Constraints:
      1 <= nums.length <= 5000
      -104 <= nums[i] <= 104
      All values of nums are unique.
      nums is an ascending array that is possibly rotated.
      -104 <= target <= 104

   LeetCode: 
      Runtime: 69 ms, beats 14.21%;
      Memory: 42 MB, beats 58.85%;
 */

      function searchInSortedArray(nums, target) {
         let result = -1;
         let l = 0;
         let m = Math.floor(nums.length / 2);
         let r = nums.length - 1;
         let left;
         let mid;
         let right;
         for (let i = 0; i < nums.length; i++) {
            left = nums[l];
            mid = nums[m];
            right = nums[r];
            console.log(left, mid, right);
            if (left === target) return l;
            if (mid === target) return m;
            if (right === target) return r;
            if (l === m || r === m) return result;
            if (target < mid) {
               // probably target is in the left;
               if (target < left) {
                  if (right > mid) {
                     // target is in the left
                     r = m - 1;
                     m = Math.floor((l + r) / 2);
                  } else if (right < mid) {
                     // target is in the right
                     l = m + 1;
                     m = Math.floor((l + r + 1) / 2);
                  }
               } else if (target > left) {
                  // (array is not rotated) target is in the left
                  r = m - 1;
                  m = Math.floor((l + r) / 2);
               }
               continue;
            }
            if (target > mid) {
               // probably target is in the right;
               if (target > right) {
                  if (left > mid) {
                     // target is in the left
                     r = m - 1;
                     m = Math.floor((l + r) / 2);
                  } else if (left < mid) {
                     // target is in the right
                     l = m + 1;
                     m = Math.floor((l + r + 1) / 2);
                  }
               } else if (target < right) {
                  // (array is not rotated) target is in the right
                  l = m + 1;
                  m = Math.floor((l + r + 1) / 2);
               }
               continue;
            }
         }
         return result;
      }
      const nums1 = [4, 5, 6, 7, 0, 1, 2]; const target1 = 1;// 5
      const nums2 = [1, 2, 3, 4, 5, 6, 7]; const target2 = 2;// 1
      const nums3 = [2, 3, 4, 5, 6, 7, 1]; const target3 = 7;// 5
      const nums4 = [4, 5, 6, 0, 1, 2, 3]; const target4 = 2;// 5
      const nums5 = [5, 6, 0, 1, 2, 3, 4]; const target5 = 0;// 2
      const nums6 = [0, 1, 2, 3, 4, 5, 6]; const target6 = 33// 3
      const nums7 = [3,4,0,2]; const target7 = 3;
      console.log(searchInSortedArray(nums7, target7));