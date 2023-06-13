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
// Naive solution: O(n^n), time limit exceeded
function coinChange(coins, amount) {
  result = Infinity;
  let x = 0;
  function dfs(total, count) {
    x++;
    // console.log('total', total, 'count', count);
    if (total > amount) return;
    if (total === amount && count < result) result = count;
    for (let c of coins) {
      dfs(total + c, count + 1)
    }
  }
  for (let c of coins) {
    dfs(c, 1)
  }
  console.log('executed', x);
  return result === Infinity ? -1 : result;
}
function coinChangeModulo(coins, amount) {
  let result = 0;
  if (amount === 0) return 0;
  coins.sort((a,b) => b-a);
  // console.log('coins sorted', coins);
  for (let i = 0; i < coins.length; i++) {
    const c = coins[i];
    if (c === amount) return 1;
    if (c > amount) continue;

    let d = Math.floor(amount / c);
    let remain = amount % c;
    // console.log('HERE', remain, c);
    if (remain === 0) return d;
    let cc = []; // current coin changes
    for (let x = 0; x < d; x++) {
      cc.push([i, coins[i]]) // [index, coin]
    }
    console.log('cc', cc.slice());

    while (cc.length > 0) {
      console.log('cc', cc.slice(), 'remain', remain, 'c', c, 'i', i);
      for (let j = i + 1; j < coins.length; j++) {
        const c = coins[j];
        console.log('c', c);
        let r = remain % c;
        let d = Math.floor(remain / c);
        if (r === remain) {
          continue;
        } else if (r === 0) {
          console.log('FOUND','cc', cc.slice(), 'remain', remain, 'c', c, 'd', d);
          return cc.length + d
        } else {
          // console.log('remain push', r, 'd', d, 'c', c);
          while (d > 0) {
            cc.push([j, c]);
            remain -= c;
            d--;
          }
        }
      }
      let popC = cc.pop();
      remain += popC[1];
      i = popC[0];
    }
  }

  return -1;
}
function coinChangeHashMap(coins, amount) {
  if (amount === 0) return 0;
  // let result = -1;
  let possible = [];
  let combs = [];
  coins.sort((a,b) => b - a);
  console.log('coins', coins);
  // const map = new Map(); // {combination: sum}
  /*
  9+9+1+1+1+1+1 = 7
  9+7+7 = 3
  9+1+1+1+1... = 15

  7+7
  7+1

  1+1
  */
  function recur(i, c, s, comb) {
    // console.log('i', i, 'c', c, 's', s, 'result', result);
    // console.log('i', i, 'c', c, 's', s);
    // if (result !== -1) return result;
    if (s > amount) return 0;
    if (s === amount) {
      // console.log('FOUND, ', 'i', i, 'c', c, 's', s);
      // result = c;
      possible.push(c);
      combs.push(comb);
      // return c;
      return;
    }
    for (let x = i; x < coins.length; x++) {
      // const r = recur(x, c+1, s + coins[x])
      // if (r) return r;
      recur(x, c+1, s + coins[x], [...comb, coins[x]])
    }
  }
  for (let i = 0; i < coins.length; i++) {
    // const r = recur(i, 1, coins[i]);
    // if (r) return r;
    recur(i, 1, coins[i], [coins[i]]);
  }
  console.log('possible', possible);
  console.log('combinations', combs);
  if (possible.length === 0) return -1
  let min = Infinity;
  for (let i = 0; i < possible.length; i++) {
    const c = possible[i];
    min = Math.min(c,min);
  }
  return min;
}

// time limit exceeded and doesn't get all possible answer. 
function mod(coins, amount) {
  if (amount === 0) return 0;
  coins.sort( (a,b) => b - a);
  let possible = [];

  function recur(prevI, prevC, prevM, prevD, prevS) {
    // console.log('i', prevI, 'c', prevC, 'm', prevM, 'd', prevD);
    for (let i = prevI+1; i < coins.length; i++) {
      const c = coins[i];
      if (c > prevM) {
        const s = prevS - prevC + c;
        const d = prevD - 1;
        const m = amount - s;
        recur(prevI, prevC, m, d, s)
        continue;
      };
      const m = prevM % c;
      const d = prevD + Math.floor( prevM / c);
      const s = prevS + c;
      if (m === 0) {
        possible.push(d);
      } else {
        recur(i, c, m, d, s)
      }
    }
  }
  for (let i = 0; i < coins.length; i++) {
    const c = coins[i];
    if (c > amount) continue;
    if (c === amount) return 1;
    const m = amount % c;
    const d = Math.floor( amount / c);
    const s = d * c;
    if (m === 0) {
      possible.push(d);
    };
    recur(i, c, m, d, s)
  }
  console.log('possible', possible);
}

function hashMap(coins, amount) {
  if (amount === 0) return 0;
  let map = {}; // {sum: count} if sum exist and the count less than then update
  // let map = {}; // {sum: [count, combination]} if sum exist and the count less than then update
  let queue = []; // [i, sum, count]
  let possible = [];
  for (let i = 0; i < coins.length; i++) {
    const c = coins[i];
    map[c] = 1;
    queue.push([i, c, 1])
    // map[c] = [1, [c]];
    // queue.push([i, c, 1, [c]])
  }
  // console.log(map, queue);

  while (queue.length) {
    // const [i, sum, count, combination] = queue.shift();
    const [i, sum, count] = queue.shift();
    // console.log('sum', sum, 'combination', combination);
    for (let j = i; j < coins.length; j++) {
      const c = coins[j];
      const nextSum = sum + c;
      const nextCount = count + 1;
      // const nextComb = [...combination, c];
      // console.log('nextSum', nextSum, 'nextComb', nextComb);
      // if (map[nextSum] && nextCount < map[nextSum][0]) {
      if (map[nextSum] && nextCount < map[nextSum]) {
        // map[nextSum] = [nextCount, nextComb ];
        map[nextSum] = nextCount;
      }
      const r = amount - nextSum;
      if (map[r]) {
        // console.log('FOUND:',amount, r, nextSum, nextCount, nextComb);
        // possible.push([map[r][0] + nextCount, [...nextComb, ...map[r][1]]]);
        possible.push(map[r] + nextCount);
        // continue;
        // break;
        // return map[r][0] + nextCount;
        // return map[r] + nextCount;
      }
      if (r < 0) continue;
      // map[nextSum] = [nextCount, nextComb];
      map[nextSum] = nextCount;
      // queue.push([j, nextSum, nextCount, nextComb]);
      queue.push([j, nextSum, nextCount]);
    }
  }
  console.log('possible', possible);
  return -1;
}
function hashMapRecur(coins, amount) {
  if (amount === 0) return 0;
  // coins.sort((a,b) => b - a);
  coins.sort((a,b) => a-b);
  let map = {};
  let possible = [];

  function rec(i, sum, count) {
    // console.log('RECURSION');
    if (sum > amount) return;
    if (sum === amount) {
      map[sum] = count;
      return;
    }
    for (let j = i; j >= 0; j--) {
      const c = coins[j];
      const nextSum = sum + c;
      const r = amount - nextSum;

      if (map[nextSum] && count + 1 < map[nextSum]) {
        map[nextSum] = count + 1;
      }

      if (r < 0) continue;
      if (r === 0) {
        // console.log('REMAIN 0');
        // since decrement then we don't neet to continue, it's already smallest
        possible.push(count+1);
        break;
        return;
      }
      if (map[r]) {
        // console.log('FOUND REMAIN')
        possible.push(map[r] + count + 1);
        break;
        return;
      }
      rec(j, nextSum, count+1);
    }
  }

  for (let i = 0; i < coins.length; i++) {
    const c = coins[i];
    let count = 1;
    let sum = c;
    map[sum] = count;
    while (sum <= amount) {
      const r = amount - sum;
      if (map[r]) {
        console.log('FUND',sum, map[r] + count);
        map[amount] = map[r] + count;
      }
      map[sum] = count;
      sum += c;
      count++;
    }
  }

  if (map[amount]) {
    possible.push(map[amount]);
  }
  console.log('map', map);
  // for (const sum in map) {
  //   const r = amount - sum;
  //   console.log('r', r);
  //   if (map[r]) {
  //     // console.log('FOUND');
  //     possible.push(map[sum] + map[r])
  //   }
  // }

  // for (let i = coins.length - 1; i >= 0; i--) {
  //   const c = coins[i];
  //   map[c] = 1;
  //   rec(i, c, 1)
  // }
  console.log('possible', possible);
}

function zoro(coins, amount) {
  if (amount === 0) return 0;
  coins.sort( (a,b) => b-a);
  let possible = [];
  // let map = {};
  let x = 0;
  function rec(i, sum, count) {
    x++;
    console.log('RECURSION')
    if (sum > amount) return null;
    if (sum === amount) { 
      // console.log('FOUND', root);
      possible.push(count); 
      return count;
    }
    for (let j = i; j < coins.length; j++) {
      const c = coins[j];
      const nextSum = sum + c;
      const nextCount = count + 1;
      rec(j, nextSum, nextCount)
    }
  }
  for (let i = 0; i < coins.length; i++) {
    const c = coins[i];
    rec(i, c, 1, c);
  }
  console.log('possible', possible, 'x', x);
}

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
