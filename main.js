/*
  70. Climbing Stairs (easy)

  You are climbing a staircase. It takes `n` steps to reach the top.

  Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?


  Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

  Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
  

  Constraints:
    - 1 <= n <= 45

  Solution by NeetCode:
    top down approach
    using only 2 vairable to store sub problem so, the space complexity is O(2) or O(1)

  LeetCode submission:
    #1
    - Runtime: 54 ms, beats 74.61%
    - Memory: 41.3 MB, beats 91.43%


*/

function climbStairs(n) {
  let one = 1; let two = 1;
  for (let i = 0; i < n-1; i++) {
    console.log('one', one);
    const temp = one;
    one = one + two;
    two = temp;
  }
  return one;
}
const n1 = 2;
const n2 = 3;
const n3 = 44; // time limit exeeded

const start = Date.now();
console.log('RESULT: ', climbStairs(n3));
console.log('RUNTIME: ', Date.now() - start);
