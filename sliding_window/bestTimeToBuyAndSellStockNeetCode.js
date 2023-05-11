/*
   LeetCode problem: Best Time to Buy and Sell Stock (easy)

   You are given an array prices where prices[i] is the price of a given stock on the ith day.

   You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

   Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

   

   Example 1:
      Input: prices = [7,1,5,3,6,4]
      Output: 5
      Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
      Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
   
   Example 2:
      Input: prices = [7,6,4,3,1]
      Output: 0
      Explanation: In this case, no transactions are done and the max profit = 0.
   
   Constraints:
   1 <= prices.length <= 105
   0 <= prices[i] <= 104

   Solution by NeetCode because my solution using two pointers and I check NeetCode to make sure is he using two pointers also or use something else like sliding window instead.

   I know sliding window uses two pointers but in this problem I don't the difference between the two.

   LeetCode: 
      Runtime: 87 ms, beats 42.57%
      Memory: 51.3 MB, beats 85.82%
*/

function bestTimeToBuyAndSellStock(prices) {
   if (prices.length === 1) return 0;
   let max = 0;
   let l = 0;
   for (let r = 1; r < prices.length; r++) {
      if (prices[r] < prices[l]) {
         l = r;
      } 
      let prob = prices[r] - prices[l];
      max = prob > max ? prob : max;
      
   }
   console.log(max);
   return max;
}
const prices1 = [7,1,5,3,6,4]; // 5
const prices2 = [7,1,5,3,6,0,9]; // 9
const prices3 = [7,6,4,3,1]; // 0
const prices4 = [1,2]; // 1
const prices5 = [7,1,5,3,6,0,3]; // 5
let sux;
console.log(bestTimeToBuyAndSellStock(prices5));