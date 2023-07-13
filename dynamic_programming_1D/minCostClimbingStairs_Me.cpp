/*
   (1D dynamic programming) leetcode: 746. Min Cost Climbing Stairs (easy)

   You are given an integer array `cost` where `cost[i]` is the cost of `ith` step on a staircase. Once you pay the cost, you can either climb one or two steps.

   You can either start from the step with index `0`, or the step with index `1`.

   Return the minimum cost to reach the top of the floor.

   

   Example 1:
      Input: cost = [10,15,20]
      Output: 15
      Explanation: You will start at index 1.
      - Pay 15 and climb two steps to reach the top.
      The total cost is 15.

   Example 2:
      Input: cost = [1,100,1,1,1,100,1,1,100,1]
      Output: 6
      Explanation: You will start at index 0.
         - Pay 1 and climb two steps to reach index 2.
         - Pay 1 and climb two steps to reach index 4.
         - Pay 1 and climb two steps to reach index 6.
         - Pay 1 and climb one step to reach index 7.
         - Pay 1 and climb two steps to reach index 9.
         - Pay 1 and climb one step to reach the top.
         The total cost is 6.
   

   Constraints:
      = 2 <= cost.length <= 1000
      = 0 <= cost[i] <= 999

   Related Topics: 

   ========================================================== 

   Solution by myself:
      dynamic programming, store it in variables for better space complexity

   Leetcode submission:
      runtime: 3 ms, beats 94.62%
      memory: 13.6 MB, beats 91.89%

*/

#include <iostream>
#include <vector>
using namespace std;

// time O(n), space O(1)
int minCostClimbingStairs(vector<int>& cost) {
   int dp1 = cost[size(cost) - 2];
   int dp2 = cost[size(cost) - 1]; 
   for (int i = size(cost) - 3; i >= 0; i--) {
      int temp = dp1;
      dp1 = cost[i] + min(dp1, dp2);
      dp2 = temp;
   }
   return min(dp1, dp2);
}
int main() {
   vector<int> c1 = {10,15,20}; // 15
   vector<int> c2 = {1,100,1,1,1,100,1,1,100,1}; // 6 
   vector<int> c3 = {10,15,20,4,19,7,8,3,3,4,16,4,9};

   cout << minCostClimbingStairs(c3);
   
   return 0;
}