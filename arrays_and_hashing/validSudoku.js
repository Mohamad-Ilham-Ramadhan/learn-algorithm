/*
   LeetCode problem: Valid Sudoku (medium)
   

   Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

   Each row must contain the digits 1-9 without repetition.
   Each column must contain the digits 1-9 without repetition.
   Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

   Note:
   A Sudoku board (partially filled) could be valid but is not necessarily solvable.
   Only the filled cells need to be validated according to the mentioned rules.
   

   Example 1:

   Input: board = 
   [["5","3",".",".","7",".",".",".","."]
   ,["6",".",".","1","9","5",".",".","."]
   ,[".","9","8",".",".",".",".","6","."]
   ,["8",".",".",".","6",".",".",".","3"]
   ,["4",".",".","8",".","3",".",".","1"]
   ,["7",".",".",".","2",".",".",".","6"]
   ,[".","6",".",".",".",".","2","8","."]
   ,[".",".",".","4","1","9",".",".","5"]
   ,[".",".",".",".","8",".",".","7","9"]]
   Output: true
   Example 2:

   Input: board = 
   [["8","3",".",".","7",".",".",".","."]
   ,["6",".",".","1","9","5",".",".","."]
   ,[".","9","8",".",".",".",".","6","."]
   ,["8",".",".",".","6",".",".",".","3"]
   ,["4",".",".","8",".","3",".",".","1"]
   ,["7",".",".",".","2",".",".",".","6"]
   ,[".","6",".",".",".",".","2","8","."]
   ,[".",".",".","4","1","9",".",".","5"]
   ,[".",".",".",".","8",".",".","7","9"]]
   Output: false
   Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
   

   Constraints:

   board.length == 9
   board[i].length == 9
   board[i][j] is a digit 1-9 or '.'.

   Solution is pure by myself:
      Time complexity: O(n * m) where n is the nubmer of rows and m is the number of columns, since the board dimensions are fixed 9 * 9 so the time complexity is O(81)

      for checking subbox
      I create subbox 2-d arrays of sets, each sets is represents a subbox

      for checking cols I create arrays of sets

   LeetCode submission: 
      Runtime: 68 ms, beats: 89.15%;
      Memory: 45.4 MB, beats: 55.81%
*/

function isValidSudoku(board) {
   let subbox = [
      [new Set(), new Set(), new Set()],
      [new Set(), new Set(), new Set()],
      [new Set(), new Set(), new Set()]
   ]; // for checking
   let cols = []; // for checking
   for (let i = 0; i < board.length; i++) {
      cols[i] = new Set();
   }
   for (let r = 0; r < board.length; r++) {
      const row = board[r];
      const rowSet = new Set();
      for (let c = 0; c < board[0].length; c++) {
         const cell = board[r][c];
         // skip non number cell 
         if (cell === '.') continue;
         // row checking
         if (rowSet.has(cell)) {
            return false;
         } else {
            rowSet.add(cell);
         }
         // col checking 
         if (cols[c].has(cell)) {
            return false;
         } else {
            cols[c].add(cell);
         }
         // subbox checking
         // I use division by 3 because the length of subbox is 3
         if (subbox[Math.floor(r / 3)][Math.floor(c / 3)].has(cell)) {
            return false;
         } else {
            subbox[Math.floor(r / 3)][Math.floor(c / 3)].add(cell)
         }
      }
   }
   console.log('cols', cols);
   return true;
}
let board1 = board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]; // expect true
let board2 = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]; // expect false
console.log('result', isValidSudoku(board2));