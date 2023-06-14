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
  let x = 0;
  for (let i = nums.length - 1; i >= 0; i--) {
    x++;
    const n1 = nums[i];
    let max = 1;
    for (let j = i + 1; j < nums.length; j++) {
      x++;
      const n2 = nums[j];
      if (n2 > n1) {
        max = Math.max(max, dp[j] + 1);
      }
    }
    dp[i] = max;
    result = Math.max(result, max);
  }
  console.log('dp', dp, 'x', x);
  return result;
  // attempt #1 [end]

  // attempt #2 [start]

  /*
    [0, 10, 9, 11, 12, 100, 1, 2, 3, 4]
        [ [4] ] -> 1
    3   [ [4,3] ] -> 2
    2   [ [4,3,2] ] -> 3
    1   [ [4,3,2,1] ] -> 4
    100 [ [4,3,2,1], [100] ] -> 4
    12  [ [4,3,2,1], [100, 12]] -> 4
    11  [ [4,3,2,1], [100, 12, 11] ] -> 4
    9   [ [4,3,2,1], [100, 12, 11, 9] ] -> 4
    10  [ [4,3,2,1], [100, 12, 11, 9], [100, 12, 11, 10] ] -> 4
    0   [ [4,3,2,1,0], [100, 12, 11, 9, 0], [100, 12, 11, 10, 0] ] -> 5

    [0, 1, 0, 3, 2, 3]
      [ [3] ] -> 1
    2 [ [3,2] ] -> 2
    3 [ [3,2], [3] ] -> 2
    0 [ [3,2,0], [3,0] ] -> 3
    1 [ [3,2,0], [3,0], [3,1], [3,2,1] ] -> 3
    0 [ [3,2,0], [3,0], [3,1,0], [3,2,1,0] ] -> 4
    
  */
  // result = 1;
  // subs = [  ];
  // let z = 0;
  // for (let i = nums.length - 1; i >= 0; i--) {
  //   z++;
  //   const n1 = nums[i];
  //   let isInserted = false;
  //   let newSubs = [];
  //   for (let j = 0; j < subs.length; j++) {
  //     z++;
  //     const s = subs[j];
  //     let x = s.length - 1;
  //     while (n1 < s[0] || x >= 0) {
  //       z++;
  //       const n2 = s[x];
  //       // console.log('n1', n1, 'n2', n2);
  //       if (n1 === n2) break;
  //       if (n1 < n2) {
  //         if (x === s.length - 1) {
  //           s.push(n1);
  //           result = Math.max(s.length, result);
  //         } else {
  //           newSubs.push([...s.slice(0, x+1), n1])
  //         }
  //         isInserted = true;
  //         break;
  //       }
  //       x--;
  //     }
  //   }
  //   if (!isInserted && newSubs.length === 0) {
  //     subs.push([n1]);
  //   } 
  //   if (isInserted && newSubs.length > 0) {
  //     subs.push(...newSubs);
  //   }
  //   // console.log(n1, 'subs.slice', ...subs.slice());
  // }
  // console.log('z', z);
  // return result;
  // attempt #2 [end]
}
const nums1 = [10, 9, 2, 5, 3, 7, 101, 18]; // expect: 4
/*
  9 -> 2
  3 -> 4
  18 -> 4
*/
const nums2 = [0, 1, 0, 3, 2, 3]; // expect: 4
/*
  0 -> 3
  0 -> 2
  2-> 4
*/
const nums3 = [7, 7, 7, 7, 7, 7, 7]; // expect: 1
const nums4 = [0, 10, 9, 11, 12, 100, 1, 2, 3, 4, 5, 6, 7, 8]// [4, 1, 4], [100, 9, 4], 
/*
  0 -> 4
  1 -> 8
*/

const start = Date.now();
console.log('RESULT :', lengthOfLIS(nums1));
console.log('RUNTIME :', Date.now() - start);
var arr = [7, -2, 4, 1, 6, 5, 0, -4, 2];
function qs(arr) {
  function q(arr) {
    if (arr.length === 0) return arr;
    if (typeof arr[0] === 'number') {
      const pivot = arr[arr.length - 1];
      const a1 = [];
      const a2 = [];
      for (let i = 0; i < arr.length - 1; i++) {
        const e = arr[i];
        if (e < pivot) {
          a1.push([i, e])
        } else {
          a2.push([i, e])
        }
      }
      // console.log('a1', a1, 'a2', a2);
      return [...q(a1), [arr.length - 1, pivot], ...q(a2)]
    } else {
      const pivot = arr[arr.length - 1];
      const a1 = [];
      const a2 = [];
      for (let i = 0; i < arr.length - 1; i++) {
        const e = arr[i];
        if (e[1] < pivot[1]) {
          a1.push(e)
        } else {
          a2.push(e)
        }
      }
      // console.log('a1', a1, 'a2', a2);
      return [...q(a1), pivot, ...q(a2)]
    }
  }
  sortedNums = q(arr);
  console.log('sortedNums', sortedNums);
  let result = [];

  for (let i = 0; i < sortedNums.length; i++) {
    const n = sortedNums[i];
    
  }
}
qs(nums4);