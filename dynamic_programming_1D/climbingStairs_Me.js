/*
  70. Climbing Stairs (medium)

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

  Solution by myself:
    - using backtracking (combination) fail: time limit exceeded
    - using dynamic programming (caching): store total combination from n1, n2 = n1 + n1, n3 = n2 + n1, n4 = n3 + n2, n5 = n4 + n3, ...

  LeetCode submission:
    #1 cache using Object
      #1
      - Runtime: 63 ms, beats 24.57%
      - Memory: 41.7 MB, beats 70.8%
      #2
      - Runtime: 63 ms, beats 24.57%
      - Memory: 41.8 MB, beats 49.79%
    #2 cache using Map
      #1
      - Runtime: 50 ms, beats 89.32%
      - Memory: 42.1 MB, beats 29.25%
      #2
      - Runtime: 55 ms, beats 70.1%
      - Memory: 41.8 MB, beats 60.35%

*/

function climbStairs(n) {

   // BACKTRACKING TEST: FAIL, TIME LIMIT EXCEEDED
 
   // let result = 0;
   // function dfs(sum) {
   //     if (sum === n) result++;
   //     if (sum > n) return;
   //     dfs(sum + 1);
   //     dfs(sum + 2)
   // }
   // dfs(1);
   // dfs(2);
   // return result;
 
   /*
     {
       2: 2
       3: 3
     }
     dp(4) = 2 + 3
   */
   let cache = {1: 1, 0: 1, '-1': 0};
   // const cache = (new Map()).set(1,1).set(0,1).set(-1,0);
   function dp(n) {
     if (cache[n] !== undefined) return cache[n];
     // if (cache.has(n)) return cache.get(n);
     cache[n] = dp(n-2) + dp(n-1);
     // cache.set(n, dp(n-2) + dp(n-1) );
     return cache[n];
     // return cache.get(n);
   }
   return dp(n);
 }
 const n1 = 2;
 const n2 = 3;
 const n3 = 44; // time limit exeeded
 
 const start = Date.now();
 console.log('RESULT: ', climbStairs(4));
 console.log('RUNTIME: ', Date.now() - start);
 
 /*
   Observing the patterns:
 
   1
 
   1,1
   2
 
   1,1,1
   2,1
   1,2
 
 
   1,1,1,1
   2,1,1
   1,2,1
   1,1,2
   2,2
   
   1,1,1,1,1
   2,1,1,1
   1,2,1,1
   1,1,2,1
   2,2,1
   1,1,1,2
   2,1,2
   1,2,2
   
   1,1,1,1,1,1
   2,1,1,1,1
   1,2,1,1,1
   1,1,2,1,1
   2,2,1,1
   1,1,1,2,1
   2,1,2,1
   1,2,2,1
   1,1,1,1,2
   2,1,1,2
   1,2,1,2
   1,1,2,2
   2,2,2
 */