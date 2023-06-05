/*
  leetcode: 213. House Robber II (medium)

  You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

  Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

  

  Example 1:
    Input: nums = [2,3,2]
    Output: 3
    Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

  Example 2:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

  Example 3:
    Input: nums = [1,2,3]
    Output: 3
  

  Constraints:
    - 1 <= nums.length <= 100
    - 0 <= nums[i] <= 1000

  Leetcode submission:
    (using maps)
      #1
        - Runtime: 57 ms, beats 68.35%
        - Memory: 43.8 MB, beats 8.92%
      #2
        - Runtime: 74 ms, beats 5.5%
        - Memory: 43.8 MB, beats 8.92%
    (using variable)
      #1
        - Runtime: 71 ms, beats 7.74%
        - memory: 41.8 MB, beats 76.79%
      #2
        - Runtime: 66 ms, beats 19.70%
        - Memory: 42 MB, beats 57.58%
*/
/*
  [3,4,100,5,6,100,4,100,7,1,100,9,100,4]
  3 + 100 + 100 + 100 + 100 + 100 - 3;
  4 + 5 + 100 + 100 + 100 + 100
*/

// THIS SOLUTION IS NOT PASSED
function rob(nums) {
  if (nums.length === 1) return nums[0];
  if (nums.length === 2) return Math.max(nums[0], nums[1]);

  // rootIndex is 0 or 1, the first index number in the total sum
  // if we include index 0 and last in the total sum then totalSum - Math.min(nums[0], nums[lastIndex])
  // root index in the map is for track their rootIndex
  let sumMap = (new Map()).set(-3, [0, 0]).set(-2, [0, 0]).set(-1, [0, 0]); // [rootIndex, sum]
  for (let i = 0; i < nums.length; i++) {
    const n = nums[i];
    let rootIndex = 0;
    if (i === 0) {
      rootIndex = 0;
    } else if (i === 1) {
      rootIndex = 1;
    } else if (i < nums.length - 1) {
      rootIndex = sumMap.get(i - 2)[1] + n >= sumMap.get(i - 3)[1] + n ? sumMap.get(i - 2)[0] : sumMap.get(i - 3)[0];
      console.log('else', rootIndex);
    }
    // for rootIndex nums.length - 1, there is in the next, right before


    // jika i = nums.length - 1
    // pilih antara prev yang rootIndex nya 1 sama 0 yang 
    // jika 0 maka setelah kalkulasi total - Math.min(nums[0], nums[length-1]) (let say: afterMin)
    // Math.max(afterMin, prev yang rootIndex 1)
    if (i === nums.length - 1) {
      console.log('i === nums.length - 1');
      // cari rootIndex === 1
      let tempI2; // i - 2, i-2 + n
      if (sumMap.get(i - 2)[0] === 0) {
        tempI2 = (sumMap.get(i - 2)[1] + n) - Math.min(n, nums[0])
      } else {
        tempI2 = sumMap.get(i - 2)[1] + n;
      }
      console.log('i-2', sumMap.get(i - 2)[0], sumMap.get(i - 2)[1]);
      // cari rootIndex === 1
      let tempI3; // i - 3, i-3 + n
      if (sumMap.get(i - 3)[0] === 0) {
        tempI3 = (sumMap.get(i - 3)[1] + n) - Math.min(n, nums[0])
      } else {
        tempI3 = sumMap.get(i - 3)[1] + n;
      }
      // console.log('i-3',sumMap.get(i-3)[0], sumMap.get(i-3)[1]);
      console.log('tempi2', tempI2);
      console.log('tempi3', tempI3);
      // maybe there will be a bug when tempI2 === tempI3 (yes there is a bug)
      if (tempI2 > tempI3) {
        rootIndex = sumMap.get(i - 2)[0]
      } else {
        rootIndex = sumMap.get(i - 3)[0]
      }
      sumMap.set(i, [rootIndex, Math.max(tempI2, tempI3)]);
    } else {
      sumMap.set(i, [rootIndex, Math.max(sumMap.get(i - 2)[1] + n, sumMap.get(i - 3)[1] + n)]);
    }
  }
  console.log('sumMap before', new Map(sumMap));
  // if (sumMap.get(nums.length - 1)[0] === 0) {
  //   sumMap.set(nums.length - 1, [0, sumMap.get(nums.length - 1)[1] - Math.min(nums[0], nums[nums.length - 1])]);
  // }
  return Math.max(sumMap.get(nums.length - 1)[1], sumMap.get(nums.length - 2)[1], sumMap.get(nums.length - 3)[1]);

}
// const nums0 = [1, 7, 3, 7, 100]; // expect 107
// const nums1 = [2, 3, 2];// expect: 3
// const nums2 = [1, 2, 3, 1];// expect: 4
// const nums3 = [1, 2, 3];// expect: 3
// const nums4 = [3, 4, 100, 5, 6, 100, 4, 100, 7, 1, 100, 9, 100, 4]; // expect: 503
// const nums5 = [3, 4, 100, 5, 6, 100, 4, 100, 7, 1, 100, 9, 4, 100]; // expect: 500
// const nums6 = [1, 1, 1, 2]; // expect: 3
// const nums7 = [2, 2, 4, 3, 2, 5]; // expect: 10
// const nums8 = [2, 2, 5, 3, 2, 5]; // expect: 10 // check potential bug when tempI2 === tempI3
// const nums9 = [2,1,2,6,1,8,10,10]; // expect: 25
// console.log('RESULT: ', rob(nums9));


// THIS ANSWER IS PASSED
function rob2(nums) {
  if (nums.length === 1) return nums[0];
  if (nums.length === 2) return Math.max(nums[0], nums[1]);

  let sumMap1 = (new Map()).set(-3, [0, 0]).set(-2, [0, 0]).set(-1, [0, 0]);
  for (let i = 0; i < nums.length; i++) {
    const n = nums[i];
    let rootIndex = 0;
    if (i === 0) {
      rootIndex = 0;
    } else if (i === 1) {
      rootIndex = 1;
    } else {
      rootIndex = sumMap1.get(i - 2)[1] + n >= sumMap1.get(i - 3)[1] + n ? sumMap1.get(i - 2)[0] : sumMap1.get(i - 3)[0];
      console.log('else', rootIndex);
    }
    sumMap1.set(i, [rootIndex, Math.max(sumMap1.get(i - 2)[1] + n, sumMap1.get(i - 3)[1] + n)]);
  }

  if (sumMap1.get(nums.length - 1)[0] === 0) {
    sumMap1.set(nums.length - 1, [0, sumMap1.get(nums.length - 1)[1] - Math.min(nums[0], nums[nums.length - 1])]);
  }

  let result1 = Math.max(sumMap1.get(nums.length - 1)[1], sumMap1.get(nums.length - 2)[1], sumMap1.get(nums.length - 3)[1]);


  // ==================================
  let sumMap2 = (new Map()).set(-3, 0).set(-2, 0).set(-1, 0);
  let nums2 = nums.slice(1);
  for (let i = 0; i < nums2.length; i++) {
    const n = nums2[i];
    sumMap2.set(i, Math.max(sumMap2.get(i - 2) + n, sumMap2.get(i - 3) + n));
  }
  let result2 = Math.max(sumMap2.get(nums2.length - 1), sumMap2.get(nums2.length - 2), sumMap2.get(nums2.length - 3));
  console.log('sumMap 1 ', sumMap1)
  console.log('sumMap 2 ', sumMap2)
  console.log('result 1 ', result1, 'result 2 ', result2);
  return Math.max(result1, result2);
}

// const nums0 = [1, 7, 3, 7, 100]; // expect 107
// const nums1 = [2, 3, 2];// expect: 3
// const nums2 = [1, 2, 3, 1];// expect: 4
// const nums3 = [1, 2, 3];// expect: 3
// const nums4 = [3, 4, 100, 5, 6, 100, 4, 100, 7, 1, 100, 9, 100, 4]; // expect: 503
// const nums5 = [3, 4, 100, 5, 6, 100, 4, 100, 7, 1, 100, 9, 4, 100]; // expect: 500
// const nums6 = [1, 1, 1, 2]; // expect: 3
// const nums7 = [2, 2, 4, 3, 2, 5]; // expect: 10
// const nums8 = [2, 2, 5, 3, 2, 5]; // expect: 10 // check potential bug when tempI2 === tempI3
// const nums9 = [2, 1, 2, 6, 1, 8, 10, 10]; // expect: 25
// console.log('RESULT: ', rob2(nums0));

function rob2Variable(nums) {
  if (nums.length === 1) return nums[0];
  if (nums.length === 2) return Math.max(nums[0], nums[1]);

  let lastThree = [0,0]; // [rootIndex, sum]
  let lastTwo = [0,0]; // [rootIndex, sum]
  let lastOne = [0,0]; // [rootIndex, sum]
  for (let i = 0; i < nums.length; i++) {
    const n = nums[i];
    let tempOne = lastOne;
    // lastOne = Math.max(lastTwo + n, lastThree + n);
    if (lastTwo[1] + n >= lastThree[1] + n) {
      lastOne = [lastTwo[0], lastTwo[1] + n]
    } else {
      lastOne = [lastThree[0], lastThree[1] + n]
    }
    let tempTwo = lastTwo;
    lastTwo = tempOne;
    lastThree = tempTwo;
  }
  console.log('lastOne', lastOne, 'lastTwo', lastTwo, 'lastThree', lastThree);
  
  // if (sumMap1.get(nums.length - 1)[0] === 0) {
  //   sumMap1.set(nums.length - 1, [0, sumMap1.get(nums.length - 1)[1] - Math.min(nums[0], nums[nums.length - 1])]);
  // }
  if (lastOne[0] === 0) {
    lastOne = [0, lastOne[1] - Math.min(nums[0], nums[nums.length - 1])];
  }
  const result1 = Math.max(lastOne[1], lastTwo[1], lastThree[1]);

  // ======================================

  let lastThree2 = 0; // [rootIndex, sum]
  let lastTwo2 = 0; // [rootIndex, sum]
  let lastOne2 = 0; // [rootIndex, sum]
  let nums2 = nums.slice(1);
  for (let i = 0; i < nums2.length; i++) {
    const n = nums2[i];
    let tempOne = lastOne2;
    lastOne2 = Math.max(lastTwo2 + n, lastThree2 + n);
    let tempTwo = lastTwo2;
    lastTwo2 = tempOne;
    lastThree2 = tempTwo;
  }
  let result2 = Math.max(lastOne2, lastTwo2, lastThree2);
  console.log('result1', result1, 'result2', result2);

  return Math.max(result1, result2);
}
const nums0 = [1, 7, 3, 7, 100]; // expect 107
const nums1 = [2, 3, 2];// expect: 3
const nums2 = [1, 2, 3, 1];// expect: 4
const nums3 = [1, 2, 3];// expect: 3
const nums4 = [3, 4, 100, 5, 6, 100, 4, 100, 7, 1, 100, 9, 100, 4]; // expect: 503
const nums5 = [3, 4, 100, 5, 6, 100, 4, 100, 7, 1, 100, 9, 4, 100]; // expect: 500
const nums6 = [1, 1, 1, 2]; // expect: 3
const nums7 = [2, 2, 4, 3, 2, 5]; // expect: 10
const nums8 = [2, 2, 5, 3, 2, 5]; // expect: 10 // check potential bug when tempI2 === tempI3
const nums9 = [2, 1, 2, 6, 1, 8, 10, 10]; // expect: 25
console.log('RESULT: ', rob2Variable(nums0));