// Backtracking technique 

// LeetCode Word Search (medium)

/*
   Given an m * n grid of characters (board) and a string (word), return true if word exists in the grid. 

   The word can be constructed from letters of sequential adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
*/

/* 
   Solution by NeetCode (of course it is use backtracking) : https://www.youtube.com/watch?v=pfiQ_PS1g8E
   Time Complexity O(n * m * 4^word) 4^word = dfs()
   Why dfs() execution time complexity is 4^word because each character we call 4 dfs() which each call call 4 dfs() more, so it like a tree that each leaves is 4

   It is been tested on LeetCode.com: runtime beats 23.62% and memory beats 19.69%

*/
function wordSearch(board, word) {
   const ROWS = board.length; const COLS = board[0].length;
   let path = new Set();

   function dfs(r, c, i) {
      if (i == word.length) return true;

      if (
            r < 0 || c < 0 || // left or top is undefined
            r >= ROWS || c >= COLS || // right or bottom is undefined
            word[i] !== board[r][c] || // current char on board is not the same with current char on word
            path.has(`${r}${c}`) // current coordinate is already in path
         ) return false;
      
      path.add(`${r}${c}`);
      const result = (dfs(r+1, c, i+1) || dfs(r-1, c, i+1) || dfs(r, c+1, i+1) || dfs(r, c-1, i+1));
      path.delete(`${r}${c}`);
      return result;
   }
   // Search over every cell for the first char on word.
   for (let r = 0; r < ROWS; r++) {
      for (let c = 0; c < COLS; c++) {
         if (dfs(r, c, 0)) return true;
      }
   }
   return false;
}
const board = [
   ['A', 'B', 'C', 'E'],
   ['B', 'F', 'C', 'S'],
   ['C', 'D', 'E', 'E'],
]; const word = 'ABCCED';
const board2 = [
   ["C", "A", "A"],
   ["A", "A", "A"],
   ["B", "C", "D"]
]; const word2 = 'AAB';
const board3 = [
   ["A", "B", "C", "E"],
   ["S", "F", "E", "S"],
   ["A", "D", "E", "E"]
]; const word3 = 'ABCESEEEFS';
console.log(wordSearch(board2, word2)); // true
