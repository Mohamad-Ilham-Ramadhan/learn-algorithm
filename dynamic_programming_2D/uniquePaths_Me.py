'''
   LeetCode: (2D dynamic programming) 62. Unique Paths (medium)

   There is a robot on an `m x n` grid. The robot is initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

   Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

   The test cases are generated so that the answer will be less than or equal to `2 * 109`.

   

   Example 1:
      [][][][][][][]
      [][][][][][][]
      [][][][][][][]

      Input: m = 3, n = 7
      Output: 28

   Example 2:
      [][]
      [][]
      [][]

      Input: m = 3, n = 2
      Output: 3
      Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
      1. Right -> Down -> Down
      2. Down -> Down -> Right
      3. Down -> Right -> Down
   

   Constraints:
      1 <= m, n <= 100

   ======================================================================= 

   Solution by myself 
      dynamic programming
      time complexity: O(m*n)
      space complexity: O(m*n)

   Leetcode submission:
      runtime: 46 ms, beats 60.41%
      memory: 16.4 MB, beats 17.46%
'''

def uniquePaths(m, n):
   grid = [[1] * n] 
   for i in range(1,m):
      grid.append([1])
      for j in range(1, n):
         grid[i].append(grid[i-1][j] + grid[i][j-1])
   #    print('i', i)
   # print('grid', grid)
   return grid[m-1][n-1]
m1 = 3; n1 = 7 
m2 = 3; n2 = 2
m3 = 3; n3 = 3
m4 = 2; n4 = 4
import unittest
import time
class TestBro(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
    
    def tearDown(self) -> None:
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_xxx(self):
        self.assertEqual(uniquePaths(m1, n1), 28) 
        self.assertEqual(uniquePaths(m2, n2), 3) 
        self.assertEqual(uniquePaths(m3, n3), 6) 
        self.assertEqual(uniquePaths(m4, n4), 4) 
        
# print('RESULT :', uniquePaths(m3, n3))
if __name__ == "__main__":
   unittest.main()
'''
   m = 3, n = 3 expect => 
   [1][1][1]
   [1][2][3]
   [1][3][6]

   m = 3, n = 7 expect => 28
   [1][1][1][1][1][1][1]
   [1][2][3][4][5][6][7]
   [1][3][6][10][15][21][28]

   m = 2, n = 4 expect => 4
   [1][1][1][1]
   [1][2][3][4]

   m = 4, n = 2 expect => 4
   [1][1]
   [1][2]
   [1][3]
   [1][4]
'''
