/*
  Leetcode: 198. House Robber (medium)

  You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

  Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

  

  Example 1:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

  Example 2:
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12.
  

  Constraints:
    - 1 <= nums.length <= 100
    - 0 <= nums[i] <= 400

  Solution by myself:
    Dynamic programing bottom-up approach (probably LOL. I still don't grasp the concept fully yet)

  LeetCode submission:
    #1 (using variable)
      #1 (with comments)
      - Runtime: 63 ms, beats 27.9%
      - Memory: 41.4 MB, beats 91.80%
      #2 (without comments)
      - Runtime: 57 ms, beats 62.35%
      - Memory: 42.4 MB, beats 16.45%
      #3 (using ternary to compare 2 num instead Math.max)
      - Runtime: 65 ms, beats 18.72%
      - Memory: 42.1 MB, beats 42.28%

    #2 (using map)
      #1 (with comments)
      - Runtime: 58 ms, beats 57.11%
      - Memory: 41.8 MB, beats 62.35%
      #2 (without comments)
      - Runtime:  62 ms, beats 33.59%
      - Memory: 42 MB, beats 42.28%
      #3 (using ternary to compare 2 num instead Math.max)
      - Runtime:  66 ms, beats 15.27%
      - Memory: 42.4 MB, beats 16.45%

*/

function rob(nums) {
  // let lastOne = nums[0];
  // let lastTwo = nums[1] ? nums[1] : 0;
  // let lastThree = nums[2] ? nums[2] + lastOne  : 0;
  // let lastOne = 0;
  // let lastTwo = 0;
  // let lastThree = 0;

  let sumMap = (new Map()).set(-3, 0).set(-2, 0).set(-1, 0);
  /*
    === Progressive === 
    [3,4,100,5,6,100,4,100,7,1,100,9,100]
    3
    4
    
    100 + 3 = 103
    5 + 4 = 9

    6 + 103 = 109
    100 + 103 = 203

    4 + 109 = 113
    100 + 203 = 303

    7 + 203 = 210
    1 + 303 = 304

    100 + 303 = 403
    9 + 304 = 313

    100 + 403 = 503 <- the greatest
  */
 // lastThree = nums[i - 3] ? nums[i - 3] : 0;
 // lastTwo = nums[i - 2] ? nums[i - 2] : 0;
 // lastOne = nums[i - 1] ? nums[i - 1] : 0;
  for (let i = 0; i < nums.length; i++) {
    // console.log('i', i);
    const n = nums[i];
    sumMap.set(i, Math.max(sumMap.get(i-2) + n, sumMap.get(i-3) + n) );
    // sumMap.set(i, sumMap.get(i-2) + n > sumMap.get(i-3) + n ? sumMap.get(i-2) + n : sumMap.get(i-3) + n)

    // let tempOne = lastOne;
    // lastOne = Math.max(lastTwo + n, lastThree + n);
    // //  lastOne = lastTwo + n > lastThree + n ? lastTwo + n : lastThree + n;
    // let tempTwo = lastTwo;
    // lastTwo = tempOne;
    // lastThree = tempTwo;
  }
  // console.log('sumMap: ', sumMap);
  // console.log('lastOne', lastOne, 'lastTwo', lastTwo, 'lastThree', lastThree);
  // return Math.max(lastOne, lastTwo, lastThree);
  return Math.max(sumMap.get(nums.length - 1), sumMap.get(nums.length - 2), sumMap.get(nums.length - 3));
};
const nums1 = [1,2,3,1]; // expect 4
const nums2 = [2,7,9,3,1]; // expect 12
const nums3 = [2,1,1,2] // expect 4 = 2 + 2
const nums4 = [3,4,100,5,6,100,4,100,7,1,100,9,100]; // expect 503
const nums5 = [9,6];
const nums6 = [8];
const nums7 = [1,2,3]; // 4
console.log('RESULT: ', rob(nums4));
/*
  [2,7,9,3,1]
  1
  3

  9 + 1 = 10
  7 + 3 = 10

  2 + 10 = 12 <- the answer

  [2,1,1,2]
  2
  1

  1 + 1 = 2
  2 + 2 = 4

  [3,4,100,5,6,100,4,100,7,1,100,9,100]
  100 = 100
  9 = 9
  100 + 100 = 200
  1 + 9 = 10

  7 + 200 = 207
  100 + 200  = 300

  4 + 207 = 211
  100 + 300 = 400

  6 + 300 = 306
  5 + 400 = 405

  100 + 400 = 500
  4 + 405 = 409

  3 + 500 = 503 <- the greatest, the answer

  [2,9,5,6,100,4,5,100,7,8,100] 

  100
  8

  7 + 100 = 107
  100 + 100 = 200

  5 + 107 = 112
  4 + 200 = 204

  100 + 200 = 300
  6 + 204 = 210

  5 + 300 = 305
  9 + 300 = 309 => the answer

  2 + 305 = 307



  [2,3,5,6,100,4,5,100,7,8,100] -> 100,100,100 = 300

  mulai dari 2

  5 + 100 + 5 + 7 + 100 = 217
  6 + 4 + 100 + 8 = 118

  kita pilih 5 karena posibility totalnya lebih besar 

  100 + 5 + 7 + 100 = 212 
  4 + 100 + 8 = 112

  kita pilih 100 
  [2,5,100]

  5 + 7 + 100 = 112
  100 + 8 = 108

  kita pilih 5
  [2,5,100,5]

  7
  8

  kita pilih 8 
  [2,5,100,5,100] = 212

  [2,9,5,6,100,4,5,100,7,8,100] 

  mulai dari 9 
  6 + 4 + 100 + 8 = 118
  100 + 5 + 7 + 100 = 212

  [9,100]


  === Progressive === 
  [3,4,100,5,6,100,4,100,7,1,100,9,100]

  3
  4
  
  100 + 3 = 103
  5 + 4 = 9

  6 + 103 = 109
  100 + 103 = 203

  4 + 109 = 113
  100 + 203 = 303

  7 + 203 = 210
  1 + 303 = 304

  100 + 303 = 403
  9 + 304 = 313

  100 + 403 = 503 <- the greatest
*/