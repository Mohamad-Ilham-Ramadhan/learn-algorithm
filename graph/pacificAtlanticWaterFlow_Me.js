/*
  Leetcode: 417. Pacific Atlantic Water Flow (medium)

  There is an `m x n` rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

  The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.

  The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

  Return a 2D list of grid coordinates `result` where `result[i] = [ri, ci]` denotes that rain water can flow from cell `(ri, ci)` to both the Pacific and Atlantic oceans.

  

  Example 1:
      Pacific Ocean

   P [1, 2, 2, 3, 5] 
   C [3, 2, 3, 4, 4]
   O [2, 4, 5, 3, 1]  Atlantic ocean
     [6, 7, 1, 4, 5]
     [5, 1, 1, 2, 4]
      
      Atlantic ocean

  Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
  Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
  Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
    [0,4]: [0,4] -> Pacific Ocean 
          [0,4] -> Atlantic Ocean
    [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
          [1,3] -> [1,4] -> Atlantic Ocean
    [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
          [1,4] -> Atlantic Ocean
    [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
          [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
    [3,0]: [3,0] -> Pacific Ocean 
          [3,0] -> [4,0] -> Atlantic Ocean
    [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
          [3,1] -> [4,1] -> Atlantic Ocean
    [4,0]: [4,0] -> Pacific Ocean 
          [4,0] -> Atlantic Ocean
    Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

  Example 2:

    Input: heights = [[1]]
    Output: [[0,0]]
    Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
  

  Constraints:
    - m == heights.length
    - n == heights[r].length
    - 1 <= m, n <= 200
    - 0 <= heights[r][c] <= 105

  Solution by myself: 
    use dfs
    and object/hashmap for visited 

  Leetcode submission: 
    # visited use object 
      #1
        Runtime: 685 ms, beats 10.66%
        Memory: 51.1 MB, beats 59.25%
      #2 (clean comment)
        Runtime: 676 ms, beats 10.66%
        Memory: 50.5 MB, beats 80.94%
    # visited use Set string (`${r},${c}`)
      #1
        Runtime: 1089 ms, beats 5.98%
        Memory: 59.7%, beats 5.98%
      #2 (clean comment)
        Runtime: 1060 ms, beats 6.17%
        Memory: 60.17%, beats 5.61%

*/
function pacificAtlantic(heights) {
   let result = [];
   const rowsLength = heights.length;
   const cellsLength = heights[0].length;
   const visited = new Set();
   // const visited = {};
   let isAtlantic = false;
   let isPacific = false;
 
   function dfs(r, c, prevHeight, origin) {
     // console.log('origin', origin, '[r,c]',`[${r},${c}]`, 'prevHeight', prevHeight, 'height', heights[r] ? heights[r][c] ? heights[r][c] : 'ocean' : 'ocean');
     // console.log('visit', (r * cellsLength) + c );
 
     // if (visited.has((r * cellsLength) + c)) return;
     // if (visited[r] && visited[r][c]) return;
     if (visited.has(`${r},${c}`)) return;
     // r <= -1 -> atlantic 
     // c <= -1 -> atlantic
     if (r <= -1 || c <= -1) {
       // console.log('pacific');
       isPacific = true;
       return;
     }
     // r >= rowsLength -> pacific 
     // c >= cellsLength -> pacific
     if (r >= rowsLength || c >= cellsLength) {
       // console.log('atlantic');
       isAtlantic = true;
       return;
     } 
     const height = heights[r][c];
     if (height > prevHeight || (isAtlantic && isPacific)) {
       // console.log('height', height, 'prevHeight', prevHeight);
       return
     };
 
     // visited.add((r * cellsLength) + c);
     // if (visited[r] === undefined ) visited[r] = {};
     // visited[r][c] = true;
     visited.add(`${r},${c}`);
     // if (!isPacific) {
       dfs(r,c+1,height, origin); // right -> pacific
       dfs(r+1,c,height, origin); // bottom -> pacific
     // }
     // if (!isAtlantic) {
       dfs(r-1,c,height, origin); // up -> atlantic
       dfs(r,c-1,height, origin); // left -> atlantic
     // }
     // dfs(r-1,c,height); // up -> atlantic
     // dfs(r,c+1,height); // right -> pacific
     // dfs(r+1,c,height); // bottom -> pacific
     // dfs(r,c-1,height); // left -> atlantic
     // visited.delete((r * cellsLength) + c);
     // delete visited[r][c];
     visited.delete(`${r},${c}`);
 
   }
   for (let r = 0; r < rowsLength; r++) {
     for (let c = 0; c < cellsLength; c++) {
       // console.log('================================================================', heights[r][c]);
       dfs(r,c,heights[r][c], heights[r][c])
       if (r === 6 && c === 1) {
         // console.log('===> ', heights[r][c], 'isAtlantic', isAtlantic, 'isPacific', isPacific);
 
       }
       if (isAtlantic && isPacific) {
         result.push([r,c]);
       }
       isAtlantic = false;
       isPacific = false;
     }
   }
   return result;
 }
 const heights1 = [
   [1,2,2,3,5],
   [3,2,3,4,4],
   [2,4,5,3,1],
   [6,7,1,4,5],
   [5,1,1,2,4]
 ]; // [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
 const heights2 = [[1]]; // [[0,0]];
 const heights3 = [
   [1,2,3,4,5,6,7,8,9,10,11,12,13],
   [48,49,50,51,52,53,54,55,56,57,58,59,14],
   [47,88,89,90,91,92,93,94,95,96,97,60,15],
   [46,87,120,121,122,123,124,125,126,127,98,61,16],
   [45,86,119,144,145,146,147,148,149,128,99,62,17],
   [44,85,118,143,160,161,162,163,150,129,100,63,18],
   [43,84,117,142,159,168,169,164,151,130,101,64,19],
   [42,83,116,141,158,167,166,165,152,131,102,65,20],
   [41,82,115,140,157,156,155,154,153,132,103,66,21],
   [40,81,114,139,138,137,136,135,134,133,104,67,22],
   [39,80,113,112,111,110,109,108,107,106,105,68,23],
   [38,79,78,77,76,75,74,73,72,71,70,69,24],
   [37,36,35,34,33,32,31,30,29,28,27,26,25]
 ]; // TIME LIMIT EXCEEDED. Expected: [[0,12],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[1,11],[1,12],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[2,9],[2,10],[2,11],[2,12],[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],[3,9],[3,10],[3,11],[3,12],[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[4,6],[4,7],[4,8],[4,9],[4,10],[4,11],[4,12],[5,0],[5,1],[5,2],[5,3],[5,4],[5,5],[5,6],[5,7],[5,8],[5,9],[5,10],[5,11],[5,12],[6,0],[6,1],[6,2],[6,3],[6,4],[6,5],[6,6],[6,7],[6,8],[6,9],[6,10],[6,11],[6,12],[7,0],[7,1],[7,2],[7,3],[7,4],[7,5],[7,6],[7,7],[7,8],[7,9],[7,10],[7,11],[7,12],[8,0],[8,1],[8,2],[8,3],[8,4],[8,5],[8,6],[8,7],[8,8],[8,9],[8,10],[8,11],[8,12],[9,0],[9,1],[9,2],[9,3],[9,4],[9,5],[9,6],[9,7],[9,8],[9,9],[9,10],[9,11],[9,12],[10,0],[10,1],[10,2],[10,3],[10,4],[10,5],[10,6],[10,7],[10,8],[10,9],[10,10],[10,11],[10,12],[11,0],[11,1],[11,2],[11,3],[11,4],[11,5],[11,6],[11,7],[11,8],[11,9],[11,10],[11,11],[11,12],[12,0],[12,1],[12,2],[12,3],[12,4],[12,5],[12,6],[12,7],[12,8],[12,9],[12,10],[12,11],[12,12]] -> 157
 const heights4 = [
   [8,7],
   [11,2],
   [1,13],
   [14,15],
   [0,10],
   [19,9],
   [17,14],
   [10,10],
   [5,5],
   [15,3],
   [6,10],
   [11,10],
   [4,3],
   [12,13],
   [11,7],
   [0,9],
   [13,5],
   [11,18],
   [9,19],
   [10,11]
 ]; // [[0,0],[0,1],[1,0],[2,1],[3,1],[4,1],[5,0],[6,0],[6,1],[7,0],[7,1],[8,0],[8,1],[9,0],[10,1],[11,0],[11,1],[12,0],[13,0],[13,1],[14,0],[15,1],[16,0],[17,1],[18,1],[19,0],[19,1]] -> 27
 const start = Date.now();
 console.log('RESULT: ', pacificAtlantic(heights1));
 console.log('RUNTIME: ', Date.now() - start);