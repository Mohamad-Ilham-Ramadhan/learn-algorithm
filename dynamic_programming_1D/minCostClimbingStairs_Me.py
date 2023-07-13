'''
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
      #1
         dynamic programming, store it in array/list
      #2 
         dynamic programming, store it in variables for better space complexity

   Leetcode submission:
      #1
         runtime: 71 ms, beats 71.96%
         memory: 16.4 MB, beats 66.5%
         
'''
# Time complexity: O(n), Space complexity: O(n)
def minCostClimbingStairs(cost): 
   dp = [0 for i in range(len(cost))]
   dp[len(cost)-1] = cost[len(cost)-1]
   dp[len(cost)-2] = cost[len(cost)-2]

   for i in range(len(cost)-3, -1, -1): 
      n = cost[i]
      print('i', i, 'n', n)
      dp[i] = n + min(dp[i+1],dp[i+2])
   
   return min(dp[0], dp[1])

c1 = [10,15,20]
c2 = [1,100,1,1,1,100,1,1,100,1]
c3 = [2,3,1,4,6,3,10,1,1,4,3,12] # 15
c4 = [10,15,20,4,19,7,8,3,3,4,16,4,9] # 37
c5 = [3,9]
'''
   10+15+4+7+3+3+4+4
   15+4+7+3+4+4
'''
print('RESULT :', minCostClimbingStairs(c5))