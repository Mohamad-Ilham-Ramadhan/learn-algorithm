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
  
  Solution by NeetCode:
    using bfs

  Leetcode submission: 
    #1
    Runtime: 111 ms, 26.36%
    Memory: 54.1 MB, 20.37%
    #2 
    Runtime: 122 ms, 21.60%
    Memory: 54 MB, 20.58%
*/

// Needs deque for BFS. Since Javascript doesn't have deque out of the box, I created it.
// if the items using array, add/remove the front will have time complexity O(n) because it needs to rearrange the indexes.
// the items using object/hashmap so add/remove front time complexity is O(1).
class Deque {
  constructor() {
    this.items = {};
    this.frontIndex = 0;
    this.endIndex = 1;
    this.size = 0;
  }

  // Add an element to the front of the deque
  addFront(element) {
    this.items[this.frontIndex] = element;
    // this.endIndex = this.frontIndex === 0 && this.endIndex === 0 ? 1 : this.endIndex;
    this.frontIndex--;
    this.size++;
  }

  // Add an element to the rear of the deque
  addRear(element) {
    this.items[this.endIndex] = element;
    // this.frontIndex = this.endIndex === 0 && this.frontIndex === 0 ? -1 : this.frontIndex;
    this.endIndex++;
    this.size++;
  }

  // Remove and return the element from the front of the deque
  removeFront() {
    if (this.isEmpty()) {
      return null;
    }
    const front = this.items[this.frontIndex + 1];
    delete this.items[this.frontIndex + 1];
    this.frontIndex++;
    this.size--;
    return front;
  }

  // Remove and return the element from the rear of the deque
  removeRear() {
    if (this.isEmpty()) {
      return null;
    }
    const end = this.items[this.endIndex - 1];
    delete this.items[this.endIndex - 1];
    this.endIndex--;
    this.size--;
    return end;  
  }

  // Return the element at the front of the deque without removing it
  peekFront() {
    if (this.isEmpty()) {
      return null;
    }
    return this.items[this.frontIndex + 1];
  }

  // Return the element at the rear of the deque without removing it
  peekRear() {
    if (this.isEmpty()) {
      return null;
    }
    return this.items[this.endIndex - 1];
  }

  // Check if the deque is empty
  isEmpty() {
    return this.size === 0;
  }

  // Return the size of the deque

  // Clear the deque
  clear() {
    this.items = {};
    this.frontIndex = 0;
    this.endIndex = 0;
    this.size = 0;
  }
}



function numIslands(grid) {
  if (grid.length === 0) return 0;

  const rows = grid.length;
  const cols = grid[0].length;
  const visit = new Set();
  let islands = 0;

  function bfs(r,c) {
    q = new Deque();
    visit.add((r * cols) + c);
    q.addRear([r,c]);

    while (q.size > 0) {
      const [ row, col ] = q.removeFront();
      const directions = [ [1,0], [-1,0], [0,1], [0,-1] ];
      for (let [dr, dc] of directions) {
        const r = row + dr; const c = col + dc;
        if (
          (r >= 0 && r < rows) && 
          (c >= 0 && c < cols) && 
          (grid[r][c] === '1') && 
          (!visit.has( ( r * cols ) + c ))
        ) {
          q.addRear([r, c]);
          visit.add(( r * cols ) + c);
        }
      }
    }
  }

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (grid[r][c] === '1' && !visit.has((r * cols) + c)) {
        bfs(r,c);
        islands++;
      }
    }
  }

  return islands;
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
// console.log('sum :', 3+4+2+2+0+4+4+1+2+5+3+4+4+3+2+6+4+3+1+1);
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
console.log('RESULT: ', numIslands(grid5));