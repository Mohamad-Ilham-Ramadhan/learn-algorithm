'''
   (graph) leetcode: 994. Rotting Oranges (medium)

   You are given an `m x n` `grid` where each cell can have one of three values:

      - `0` representing an empty cell,
      - `1` representing a fresh orange, or
      - `2` representing a rotten orange.

   Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

   Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.

   

   Example 1:


      Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
      Output: 4

   Example 2:
      Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
      Output: -1
      Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

   Example 3:
      Input: grid = [[0,2]]
      Output: 0
      Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
   

   Constraints:
      - m == grid.length
      - n == grid[i].length
      - 1 <= m, n <= 10
      - grid[i][j] is 0, 1, or 2.

   Related topics:
      (Array) (Breadth-first search) (Matrix)
      
   ======================================================= 

   solution by myself 
      using Breadth-first search

   Leetcode submission
      runtime: 67 ms, beats 62.61%
      memory: 16.4 MB, beats 27.2%
'''
from collections import deque
def orangesRotting(grid): 
   # get all rotten coordinate 
   rottens = deque() # (x,y,minute)
   for y in range(len(grid)):
      for x in range(len(grid[0])): 
         if grid[y][x] == 2: 
            rottens.append((x,y,0))
   
   print('rottens', rottens)
   minutes = 0 
   # Rotting progress using breadth-first search
   while len(rottens):
      [x,y,minute] = rottens.popleft()
      if x-1 >= 0 and grid[y][x-1] == 1: # go left
         rottens.append((x-1,y,minute+1))
         grid[y][x-1] = 2
      if x+1 < len(grid[0]) and grid[y][x+1] == 1: # go right 
         rottens.append((x+1,y,minute+1))
         grid[y][x+1] = 2
      if y-1 >= 0  and grid[y-1][x] == 1: # go bottom 
         rottens.append((x,y-1,minute+1))
         grid[y-1][x] = 2
      if y+1 < len(grid) and grid[y+1][x] == 1: # go bottom 
         rottens.append((x,y+1,minute+1))
         grid[y+1][x] = 2
      
      print(y,x, minutes, minute)
      for g in grid.copy():
         print(g, '\n')
      print(y,x)
      print('-----------------------------------------------')
      minutes = minute
   
   # check if there is fresh orange left 
   for y in range(len(grid)):
      for x in range(len(grid[0])): 
         if grid[y][x] == 1: return -1

   return minutes

g1 = [[2,1,1,0,],
      [1,1,0,0,],
      [0,1,1,0,]]
g2 = [[2,1,1,1],
      [1,1,1,1],
      [1,1,1,2]]
g3 = [[2,1,1],
      [0,1,1],
      [1,0,1]]
g4 = [[2,1,1],[1,1,1],[0,1,2]] # 2

print('RESULT :', orangesRotting(g4))