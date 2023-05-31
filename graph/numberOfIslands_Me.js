/*
  Leetcode: 200. Number of Islands (medium) 

  Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

  An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

  

  Example 1:
    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1

  Example 2:
    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3
  

  Constraints:
    - m == grid.length
    - n == grid[i].length
    - 1 <= m, n <= 300
    - grid[i][j] is '0' or '1'.
  
  Solution by myself:
    using dfs

  Leetcode submission: 
    #1 use string matching in the Set (`${x},${y}`)
      #1
      Runtime: 141 ms, beats 15.71%
      Memory: 58.9 MB, beats 9.21%
      #2
      Runtime: 151 ms, beats 12.80%
      Memory: 59 MB, beats 9%
    #2 use number matching in the Set ((y * colsLength) + x)
      #1
      Runtime: 93 ms, beats 41.46%
      Memory: 47.5 MB, beats 46.35%
      #2
      Runtime: 81 ms, beats 66.89%
      Memory: 47.2 MB, beats 46.77%
*/

function numIslands(grid) {
   const visited = new Set();
   const rowsLength = grid.length;
   const colsLength = grid[0].length;
 
   function dfs(x, y) {
     if (
       (x < 0 || x >= colsLength) ||
       (y < 0 || y >= rowsLength) ||
       // ( visited.has(`${x},${y}`) ) ||
       ( visited.has((y * colsLength) + x) ) ||
       (grid[y][x] === '0')
     ) return false;
     // visited.add(`${x},${y}`)
     visited.add((y * colsLength) + x);
     
     dfs(x-1, y);
     dfs(x, y-1);
     dfs(x+1, y);
     dfs(x, y+1);
 
     return true;
   }
 
   let result = 0;
 
   for (let y = 0; y < rowsLength; y++) {
     for (let x = 0; x < colsLength; x++) {
       if (grid[y][x] === '1') {
         if (dfs(x, y)) {
           result++;
         }
       }
     }
   }
   return result;
 }
 const grid1 = [
   ["1","1","1","1","0"],
   ["1","1","0","1","0"],
   ["1","1","0","0","0"],
   ["0","0","0","0","0"]
 ]; // expect 1
 const grid2 = [
   ["1","1","0","0","0"],
   ["1","1","0","0","0"],
   ["0","0","1","0","0"],
   ["0","0","0","1","1"]
 ]; // expect 3
 const grid3 = [['1']]; // 1
 const grid4 = [['0']]; // 0
 const grid5 = [
   ['1', '0'],
   ['0', '1'],
 ]; // 2
 const grid6 = [
   ["1","0","0","1","1","1","0","1","1","0","0","0","0","0","0","0","0","0","0","0"], // 3
   ["1","0","0","1","1","0","0","1","0","0","0","1","0","1","0","1","0","0","1","0"], // 4 // 7
   ["0","0","0","1","1","1","1","0","1","0","1","1","0","0","0","0","1","0","1","0"], // 2 // 9
   ["0","0","0","1","1","0","0","1","0","0","0","1","1","1","0","0","1","0","0","1"], // 2 // 11
   ["0","0","0","0","0","0","0","1","1","1","0","0","0","0","0","0","0","0","0","0"], // 0 // 11
   ["1","0","0","0","0","1","0","1","0","1","1","0","0","0","0","0","0","1","0","1"], // 4 // 15
   ["0","0","0","1","0","0","0","1","0","1","0","1","0","1","0","1","0","1","0","1"], // 4 // 19
   ["0","0","0","1","0","1","0","0","1","1","0","1","0","1","1","0","1","1","1","0"], // 1 // 20
   ["0","0","0","0","1","0","0","1","1","0","0","0","0","1","0","0","0","1","0","1"], // 2 // 22
   ["0","0","1","0","0","1","0","0","0","0","0","1","0","0","1","0","0","0","1","0"], // 5 // 27
   ["1","0","0","1","0","0","0","0","0","0","0","1","0","0","1","0","1","0","1","0"], // 3 // 30
   ["0","1","0","0","0","1","0","1","0","1","1","0","1","1","1","0","1","1","0","0"], // 4 // 34 <--- 33
   ["1","1","0","1","0","0","0","0","1","0","0","0","0","0","0","1","0","0","0","1"], // 4 // 38
   ["0","1","0","0","1","1","1","0","0","0","1","1","1","1","1","0","1","0","0","0"], // 3 // 41
   ["0","0","1","1","1","0","0","0","1","1","0","0","0","1","0","1","0","0","0","0"], // 2 // 43
   ["1","0","0","1","0","1","0","0","0","0","1","0","0","0","1","0","1","0","1","1"], // 6 // 49
   ["1","0","1","0","0","0","0","0","0","1","0","0","0","1","0","1","0","0","0","0"], // 4 // 53
   ["0","1","1","0","0","0","1","1","1","0","1","0","1","0","1","1","1","1","0","0"], // 3 // 56
   ["0","1","0","0","0","0","1","1","0","0","1","0","1","0","0","1","0","0","1","1"], // 1 // 57
   ["0","0","0","0","0","0","1","1","1","1","0","1","0","0","0","1","1","0","0","0"]  // 1 // 58
 ];// 58
 console.log('sum :', 3+4+2+2+0+4+4+1+2+5+3+4+4+3+2+6+4+3+1+1);
 const grid7 = [
   ['0','1','0'],
   ['1','1','1'],
   ['0','1','0'],
   ['1','1','1'],
   ['1','0','1'],
   ['1','1','1'],
   ['0','0','1'],
   ['1','0','1'],
 ]; // 2
 console.log('RESULT: ', numIslands(grid7));