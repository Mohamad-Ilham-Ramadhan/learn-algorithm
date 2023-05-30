/*
  LeetCode: Word Search (medium)

  Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

  The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

  

  Example 1:
    [A] [B] [C]  E
     S   F  [C]  S 
     A  [D] [E]  E

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true

  Example 2:
    A   B   C   E
    S   F   C  [S]
    A   D  [E] [E]

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: true

  Example 3:
    A   B   C   E
    S   F   C   S
    A   D   E   E

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: false
  

  Constraints:
    - m == board.length
    - n = board[i].length
    - 1 <= m, n <= 6
    - 1 <= word.length <= 15
    - `board` and `word` consists of only lowercase and uppercase English letters.

    Follow up: Could you use search pruning to make your solution faster with a larger board?

  Solution by myself (re-solving) 

  LeetCode submission: 
    Runtime: 2079 ms, beats 22.57%
    Memory: 48.9 MB, beats 21.78%
*/

function exist(board, word) {
   function dfs(x, y, visited, str) {
     const rowLength = board.length;
     const columnLength = board[0].length;
     console.log('str', str);
     if (
       (y < 0 || y >= rowLength) || 
       (x < 0 || x >= columnLength) || 
       (board[y][x] !== word[str.length]) || 
       visited.has(`${x}${y}`)
     ) {
       console.log('FALSE');
       return false}
       // console.log(board[y][x], word[str.length]);
 
     str = str + board[y][x];
     // console.log('str after', str);
     if (str === word) {
       console.log('RETURN TRUE');
       return true;
     };
 
     visited.add(`${x}${y}`);    
     
     let isExist =  (
       dfs(x-1,y,visited,str) ||
       dfs(x+1,y,visited,str) ||
       dfs(x,y-1,visited,str) ||
       dfs(x,y+1,visited,str) 
     ); 
     visited.delete(`${x}${y}`);
     return isExist;
   }
   for (let i = 0; i < board.length; i++) {
     for (let j = 0; j < board[0].length; j++) {
       const c = board[i][j];
       if (c == word[0]) {
         if (dfs(j, i, new Set(), '')) return true;
       }
       
     }
   }
   return false;
 }
 const board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]];
 const word1 = "ABCCED"; // expect: true
 const board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]];
 const word2 = 'SEE'; // expect: true
 const board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]];
 const word3 = 'ABCB'; // expect: false
 console.log('RESULT: ', exist(board3, word3))