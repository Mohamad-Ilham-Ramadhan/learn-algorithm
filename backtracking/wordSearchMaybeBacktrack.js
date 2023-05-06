// Backtracking technique 

// LeetCode Word Search (medium) 

/*
   Given an m * n grid of characters (board) and a string (word), return true if word exists in the grid. 

   The word can be constructed from letters of sequential adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
*/

// My solution maybe using backtracking algorithm (I'm not learned it yet, I'm straight solve backtracking problem)
function wordSearch(board, word) {
   let container = []; // 

   // loop search the first letter 
   for (let i = 0; i < board.length; i++) { // y
      const row = board[i];
      for (let j = 0; j < row.length; j++) { // x
         const letter = row[j];
         let wordIndex = 0; // word letter index to find
         if (letter === word[0]) {

            // stack.push({ coor: [j, i], wordIndex: nextIndex, letter: word[0], visited: [[j, i]] });
            // DFS
            // if a neighbor is not the next sequence of previous letter
            // collecting neighbors by its left, top, right, bottom
            // if cells is not visited && the next sequence then add to the stack 

            // const { coor, wordIndex, letter, visited } = stack.pop();
            const coor = [j,i];
            const nextIndex = wordIndex + 1;
            container[wordIndex] = letter;
            // console.log('while', 'letter', letter, 'container', container);

            if (dfs(container, coor, [coor], nextIndex, letter, wordIndex)) return true;

            function dfs(container, coor, visited, nextIndex, letter, wordIndex) {
               
               container[wordIndex] = letter;
               container = [...container];
               const nextLetter = word[nextIndex];
               // console.log(letter, 'DFS', 'container', container, 'coor', coor, 'visited', visited); 
               if (container.join('') === word) return true;


               // left
               const leftCell = board[coor[1]][coor[0] - 1];
               const leftCoor = [coor[0] - 1, coor[1]];
               if (leftCell !== undefined) {
                  if (!visited.find((c) => c[0] === leftCoor[0] && c[1] === leftCoor[1]) && nextLetter === leftCell) {
                     // stack.push({ coor: leftCoor, wordIndex: nextIndex, letter: word[nextIndex], visited: [...visited, leftCoor] });
                     if(dfs(container,leftCoor, [...visited, leftCoor], nextIndex+1, nextLetter, nextIndex)) return true;
                  }
               }
               // top
               if (board[coor[1] - 1] !== undefined) {
                  const topCell = board[coor[1] - 1][coor[0]];
                  const topCoor = [coor[0], coor[1] - 1];
                  if (topCell !== undefined) {
                     if (!visited.find((c) => c[0] === topCoor[0] && c[1] === topCoor[1]) && nextLetter === topCell) {
                        // stack.push({ coor: topCoor, wordIndex: nextIndex, letter: word[nextIndex], visited: [...visited, topCoor] });
                        if(dfs(container, topCoor, [...visited, topCoor], nextIndex+1, nextLetter, nextIndex)) return true;
                     }
                  }
               }
               // right
               const rightCell = board[coor[1]][coor[0] + 1];
               const rightCoor = [coor[0] + 1, coor[1]];
               if (rightCell !== undefined) {
                  if (!visited.find((c) => c[0] === rightCoor[0] && c[1] === rightCoor[1]) && nextLetter === rightCell) {
                     // stack.push({ coor: rightCoor, wordIndex: nextIndex, letter: word[nextIndex], visited: [...visited, rightCoor] });
                     if(dfs(container, rightCoor, [...visited, rightCoor], nextIndex+1, nextLetter, nextIndex)) return true;
                  }
               }
               // bottom
               if (board[coor[1] + 1] !== undefined) {
                  const bottomCell = board[coor[1] + 1][coor[0]];
                  const bottomCoor = [coor[0], coor[1] + 1];
                  if (bottomCell !== undefined) {
                     if (!visited.find((c) => c[0] === bottomCoor[0] && c[1] === bottomCoor[1]) && nextLetter === bottomCell) {
                        // stack.push({ coor: bottomCoor, wordIndex: nextIndex, letter: word[nextIndex], visited: [...visited, bottomCoor] })
                        if(dfs(container, bottomCoor, [...visited, bottomCoor], nextIndex+1, nextLetter, nextIndex)) return true;
                     }
                  }
               }
            }
         }
      }
   }
   // console.log('container', container);
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
console.log(wordSearch(board3, word3)); // true
