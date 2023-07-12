'''
   (graphs) leetcode: 695. Max Area of Island (medium) 

   You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

   The area of an island is the number of cells with a value `1` in the island.

   Return the maximum area of an island in `grid`. If there is no island, return `0`.

   

   Example 1:

      Input: grid = [
         [0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]

         Output: 6
         Explanation: The answer is not 11, because the island must be connected 4-directionally.

   Example 2:

      Input: grid = [[0,0,0,0,0,0,0,0]]
      Output: 0

   Constraints:
      - m == grid.length
      - n == grid[i].length
      - 1 <= m, n <= 50
      - grid[i][j] is either 0 or 1.

   Related Topics 
      (Array) (Depth-first search) (Breadth-first search) (Union find) (Matrix)

   ======================================================================================

   Solution by myself 
      hashset, dfs, backtracking
      
   Leetcode submissions
      runtime: 153 ms, beats 59.54%
      memory: 20.1 MB, beats 22.78%
'''

def maxAreaOfIsland(grid): 
   visited = set()

   def dfs(x,y):
      # if coordinate already visited then stop or x or y out of boundaries or the elemnt is 0 (water)
      if (x,y) in visited or x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid) or (grid[y][x] == 0): return 0

      visited.add((x,y))
      # traverse top, right, left, bottom 
      t = dfs(x,y-1) # top
      b = dfs(x,y+1) # bottom
      l = dfs(x-1,y) # left
      r = dfs(x+1,y) # right
      return 1 + t + b + l + r
   
   maxArea = 0
   for y in range(len(grid)): 
      for x in range(len(grid[0])):
         if (x,y) in visited or grid[y][x] == 0: continue 
         area = dfs(x,y)
         maxArea = max(maxArea, area)

   return maxArea

grid = [ [0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]
g2 = [[1,1,0,0,0],
      [1,1,0,0,0],
      [0,0,0,1,1],
      [1,1,1,1,1]] # 8
print('RESULT :', maxAreaOfIsland(g2))