/*
  Leetcode: 322. Coin Change (medium)

  You are given an integer array coins representing `coins` of different denominations and an integer amount representing a total `amount` of money.

  Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

  You may assume that you have an infinite number of each kind of coin.

  
  Example 1:
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

  Example 2:
    Input: coins = [2], amount = 3
    Output: -1

  Example 3:
    Input: coins = [1], amount = 0
    Output: 0

  Solution: 
    - Selama ini gw pake greedy, makanya gak ketemu2, kadang yang paling dikit (correct answer) gak selalu yg pertama ketemu
    - Dan kalo pake backtracking supaya dapetin semua kombinasi, hasilnya time limit exceeded

    - lalu bagaimana pendekatan Dynamic Programming-nya?

  Constraints:
    - 1 <= coins.length <= 12
    - 1 <= coins[i] <= 231 - 1
    - 0 <= amount <= 104

  LeetCode submission:
    - Errichto
      Runtime: 139 ms, 41.37%
      Memory: 47.6 MB, 50.99%
*/
 function erricthoCoinChange(coins, amount) {
   // coins.sort( (a,b) => a-b);
   let dp = [];
   dp[0] = 0;
   for (let i = 1; i <= amount; i++) {
     dp[i] = Infinity
   }
 
   for (let i = 1; i <= amount; i++) {
     for (let c of coins) {
       // dp[i] = Math.min(dp[i], (dp[i - c] === undefined ? 0 : dp[i - c]) + 1)
       if (i-c > -1) {
         dp[i] = Math.min(dp[i], (dp[i - c] === undefined ? 0 : dp[i - c]) + 1)
       }
     }
   }
 
   console.log('dp', dp);
   return dp[dp.length - 1] === Infinity ? -1 : dp[dp.length - 1];
 }
 const coins1 = [1,2,5];
 const amount1 = 11; // expect: 3 -> 1 + 5 + 5
 const coins2 = [1,2,3,4,5];
 const amount2 = 11; // expect: 3 -> 1 + 5 + 5
 const coins3 = [1,2,3,4,5,6,7,8,9,10,11,12];
 const amount3 = 15; // expect: 2 -> 12+3
 const coins4 = [1,2,5];
 const amount4 = 100; // expect: 20, output: time limit exceeded
 const coins5 = [3,4,5];
 const amount5 = 17; // expect: 4, 5+5+4+3
 const coins6 = [4,5];
 const amount6 = 17; // expect: 4, 5+4+4+4 
 const coins7 = [6];
 const amount7 = [17]; // expect: -1
 const coins8 = [4,5,20];
 const amount8 = 17; // expect: 4 -> 5+4+4+4
 const coins9 = [2,5];
 const amount9 = 103; // expect: 20, output: time limit exceeded
 const coins10 = [1,2,3,4,5,6,7,8,9,10,11,12];
 const amount10 = 0;
 const coins11 = [186,419,83,408];
 const amount11 = 6249; // expect: 20, output: 26
 const coins12 = [1,7,9]; // 9+7+7
 const amount12 = 23;
 const coins13 = [411,412,413,414,415,416,417,418,419,420,421,422];
 const amount13 = 9864; // expect: 24 -> 24 * 411
 
 const c1 = [2,5]; const a1 = 12;
 
 
 const start = Date.now();
 console.log('RESULT: ', erricthoCoinChange(coins13, amount13));
 console.log('RUNTIME: ', Date.now() - start);
 // module.exports = coinChange;
 
 
 function combinationSum(nums, n) {
   let dp = [];
   dp[0] = 1;
 
   for (let i = 1; i <= n; i++) {
     dp[i] = 0;
     for (const x of nums) {
       dp[i] += dp[i-x] === undefined ? 0 : dp[i-x]
     }
   }
   console.log('dp', dp);
 }
 const nums1 = [1,2,3];
 const n1 = 4;
 const nums2 = [411,412,413,414,415,416,417,418,419,420,421,422];
 const n2 = 9864; // expect: 24 -> 24 * 411
 const nums3 = [1,7,9]; // 9+7+7
 const n3 = 23;
 
 // const start = Date.now();
 // console.log('COMBINATION SUM: ', combinationSum(nums3, n3));
 // console.log('RUNTIME: ', Date.now() - start);
 /*
   n:  0  1  2  3  4
      [1, 1, 2, 4, 7]
 
      [1,2,3] 4
 
      [1, 1, 0, 0] [1, 1, 2, 0] [1, 1, 2, 4] [1, 1, 2, 4, 7]
 
      0: 0 -> 1
      1: 1 -> 1
      2: 1+1, 2 -> 2
      3: 1+1+1, 2+1, 1+2, 3 -> 4
      4: 1+1+1+1, 2+1+1, 1+2+1, 1+1+2, 2+2, 3+1, 1+3
 
              1           2       3
         1    2   3     1  2     1
       1  2  1         1
      1
 */
 