// A* algorithm (CODINGAN SENDIRI)
// Psuedo code dari wikipedia 

function astar(board, start, destination) {
   console.log('a* board', board);
   function reconstructPath(cameFrom, current, board) {
     // const newBoard = _.cloneDeep(board);
     let path = [current];
     // newBoard[current[1]][current[0]] = 2;
     // console.log('current', current, 'nodeToKey', nodeToKey(current), 'cameFrom.get("9,9")', cameFrom.get('9,9'));
     // console.log('cameFrom.get(nodeToKey(current))', cameFrom.get(nodeToKey(current)));
     while (cameFrom.get(nodeToKey(current)) !== undefined) {
       current = cameFrom.get(nodeToKey(current));
       // newBoard[current[1]][current[0]] = 2;
       path.unshift(current)
     }
     return { path };
 
   }
 
   // Manhattan distance heuristic function 
   function h(n) {
     const x1 = n[0];
     const x2 = destination[0];
     const y1 = n[1];
     const y2 = destination[1];
     return Math.abs(x1 - x2) + Math.abs(y1 - y2);
   }
 
   function nodeToKey(n) {
     return `${n[0]},${n[1]}`;
   }
 
   // openSet is a priority queue
   let openSet = [start];
   let cameFrom = new Map();
 
   // O(n^2) (harus diakali ini)
   let gScore = {};
   for (let y = 0; y < board.length; y++) {
     for (let x = 0; x < board[y].length; x++) {
       gScore[`${x},${y}`] = Infinity;
     }
   }
   // For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
   // how cheap a path could be from start to finish if it goes through n.
   let fScore = Object.assign({}, gScore);
 
   gScore[nodeToKey(start)] = 0;
   fScore[nodeToKey(start)] = h(start);
 
   while (openSet.length > 0) {
     const current = openSet.pop();
     if (current[0] == destination[0] && current[1] == destination[1]) {
       return reconstructPath(cameFrom, current, board);
     }
 
     let neighbors = [];
     if (board[current[1]] !== undefined) {
       const left = board[current[1]][current[0] - 1];
       // console.log('left', left);
       if (left !== undefined && left !== 0) {
         neighbors.push([current[0] - 1, current[1]]);
       }
     }
     if (board[current[1] - 1]) {
       const top = board[current[1] - 1][current[0]];
       // console.log('top', top);
       if (top !== undefined && top !== 0) {
         neighbors.push([current[0], current[1] - 1]);
       }
     }
     if (board[current[1]]) {
       const right = board[current[1]][current[0] + 1];
       // console.log('right', right);
       if (right !== undefined && right !== 0) {
         neighbors.push([current[0] + 1, current[1]]);
       }
     }
     if (board[current[1] + 1]) {
       const bottom = board[current[1] + 1][current[0]];
       // console.log('bottom', bottom);
       if (bottom !== undefined && bottom !== 0) {
         neighbors.push([current[0], current[1] + 1]);
       }
     }
     for (let neighbor of neighbors) {
 
       // console.log('gScore[nodeToKey(neighbor)]', gScore[nodeToKey(neighbor)]);
 
       // tentative_gScore is the distance from start to the neighbor through current
       const tentative_gScore = gScore[nodeToKey(current)] + 1; // gScore[current] + d(current, neighbor), d(current,neighbor) is the weight of the edge from current to neighbor
 
       gScore[nodeToKey(neighbor)] = gScore[nodeToKey(neighbor)] === undefined ? Infinity : gScore[nodeToKey(neighbor)];
 
       if (tentative_gScore < gScore[nodeToKey(neighbor)]) {
         // console.log('asdf');
         // This path to neighbor is better than any previous one. Record it!
         cameFrom.set(nodeToKey(neighbor), current);
         gScore[nodeToKey(neighbor)] = tentative_gScore;
         fScore[nodeToKey(neighbor)] = tentative_gScore + h(neighbor);
 
         if (!openSet.find(x => x[0] === neighbor[0] && x[1] === neighbor[1])) {
           // add to priority queue 
           // arr.sort( (a, b) => b - a );
           openSet.push(neighbor);
           openSet.sort((a, b) => fScore[nodeToKey(b)] - fScore[nodeToKey(a)]);
         }
       }
     }
   }
   console.log('SAMPE SINI!', board);
   return { path: null, board };
 }
 
 // 0 = disabled, 1 = available path, 2 = path to the goal/end/destination
 
 const board = [
   [1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
   [1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
   [1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
   [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
   [1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
   [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
   [1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
   [1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
   [1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
   [1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
 ];
 
 
 // expected result: [ [0, 0], [0, 1], [0, 2], [0, 3], [1, 3], [2, 3], [2, 4], [2, 5], [3, 5], [4, 5], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [6, 9], [7, 9], [8, 9], [9, 9] ]
 
 
 // ========= html =============
 
 const $xInput = document.getElementById('x-length');
 const $yInput = document.getElementById('y-length');
 const $btnGenerate = document.getElementById('btn-generate');
 let x = 20;
 let y = 20;
 let generatedBoard = [];
 let start = { node: null };
 let end = { node: null };
 
 function generateBoard() {
   generatedBoard = [];
   start =  { node: null };
   end = { node: null };
   for (let i = 0; i < y; i++) {
     generatedBoard[i] = [];
     for (let j = 0; j < x; j++) {
       const rand = Math.round(Math.random() * 10);
       generatedBoard[i][j] = rand > 2 ? 1 : 0;
     }
   }
 }
 
 // initial board generation
 generateBoard();
 // initialize the board 
 renderBoard(generatedBoard, start, end);
 
 
 function maxCap(e) {
   if (e.target.value > 30) {
     e.target.value = 30;
   }
 }
 $xInput.addEventListener('input', maxCap);
 $yInput.addEventListener('input', maxCap);
 $btnGenerate.addEventListener('click', () => {
   x = Number($xInput.value);
   y = Number($yInput.value);
   console.log(x, y);
   generateBoard();
   renderBoard(generatedBoard, start, end);
   path = null;
 });
 
 
 function renderBoard(b, start, end) {
   console.log('b', b);
   const $board = document.getElementById('board');
   $board.innerHTML = '';
   const yLength = b.length;
   const xLength = b[0].length;
   const boardWidth = 20 * xLength;
   const boardHeight = 20 * yLength;
 
   $board.style.gridTemplateRows = `repeat(${yLength}, 20px)`;
   $board.style.gridTemplateColumns = `repeat(${xLength}, 20px)`;
   $board.style.width = `${boardWidth}px`;
   $board.style.height = `${boardHeight}px`;
 
   for (let y = 0; y < b.length; y++) {
     for (let x = 0; x < b[y].length; x++) {
       const $box = document.createElement('div');
       $box.classList.add('box');
 
       if (b[y][x] === 0) $box.classList.add('disabled');
 
 
       // render color for path node
       if (start.node !== null && end.node !== null) {
         const isStart = x === start.node[0] && y === start.node[1];
         const isEnd = x === end.node[0] && y === end.node[1];
         if (b[y][x] === 2 && !isStart && !isEnd) $box.classList.add('path');
       }
       // render start node
       if (start.node !== null) {
         const isStart = x === start.node[0] && y === start.node[1];
         if (isStart) { $box.classList.add('start'); }
       }
       // render end node
       if (end.node !== null) {
         const isEnd = x === end.node[0] && y === end.node[1];
         if (isEnd) { $box.classList.add('end'); }
       }
 
 
 
       $box.dataset.x = x; $box.dataset.y = y;
 
       // event listener for setup start/end node
       $box.addEventListener('click', (e) => {
         const $boxes = document.querySelectorAll('.box');
         if (isSelectingStart) {
           if (start.node !== null) {
             console.log(start.node[1], xLength, start.node[0]);
             $boxes[start.node[1] * xLength + start.node[0]].classList.remove('start')
           }
           start.node = [x, y];
           // $boxes[Number(`${start.node[1]}${start.node[0]}`)].classList.add('start');
           $box.classList.add('start');
           b[y][x] = 1;
           $box.classList.remove('end', 'disabled');
 
           // renderBoard(b, start, end);
         }
         if (isSelectingEnd) {
           if (end.node !== null) {
             $boxes[end.node[1] * xLength + end.node[0]].classList.remove('end')
           }
           end.node = [x, y];
           $box.classList.add('end');
           b[y][x] = 1;
           $box.classList.remove('start', 'disabled');
           // renderBoard(b, start, end);
         }
         if (isSelectingWall) {
           const { x, y } = $box.dataset;
           console.log(x, y, b);
           $box.classList.remove('start', 'end', 'path');
           $box.classList.toggle('disabled');
           if (b[y][x] === 1) {
             console.log('build a wall');
             b[y][x] = 0;
           } else if (b[y][x] === 0 || b[y][x] === 2) {
             console.log('remove a wall');
             b[y][x] = 1;
           }
         }
 
         // drawing wall/disabled node 
       });
       $board.append($box);
     }
   }
 
 }
 
 // let start = {node: [0, 0]};
 // let end = {node: [9, 9]};
 let path = null; // the path of start to end after executing start button
 
 
 const $start = document.getElementById('start');
 const $clear = document.getElementById('clear');
 const $startInfo = document.getElementById('start-info');
 const $endInfo = document.getElementById('end-info');
 const $wallInfo = document.getElementById('draw-wall');
 let isSelectingStart = false;
 let isSelectingEnd = false;
 let isSelectingWall = false;
 
 
 $wallInfo.addEventListener('click', (e) => {
   isSelectingWall = !isSelectingWall;
 
   isSelectingEnd = false;
   isSelectingStart = false;
   $endInfo.querySelector('.wrapper').classList.remove('active');
   $startInfo.querySelector('.wrapper').classList.remove('active');
 
   $wallInfo.querySelector('.wrapper').classList.toggle('active');
 });
 $startInfo.addEventListener('click', (e) => {
   isSelectingStart = !isSelectingStart;
 
   isSelectingEnd = false;
   isSelectingWall = false
   $endInfo.querySelector('.wrapper').classList.remove('active');
   $wallInfo.querySelector('.wrapper').classList.remove('active');
 
 
   $startInfo.querySelector('.wrapper').classList.toggle('active');
 });
 $endInfo.addEventListener('click', (e) => {
   isSelectingEnd = !isSelectingEnd;
 
   isSelectingStart = false;
   isSelectingWall = false;
   $startInfo.querySelector('.wrapper').classList.remove('active');
   $wallInfo.querySelector('.wrapper').classList.remove('active');
 
   $endInfo.querySelector('.wrapper').classList.toggle('active');
 });
 
 
 
 function clearPaths() {
   if (path !== null) {
     let $boxes = document.querySelectorAll('.box');
     for (let i = 0; i < path.length; i++) {
 
       const node = path[i];
       let boardNode = generatedBoard[node[1]][node[0]];
       if (boardNode === 0) continue;
       const boxIndex = node[1] * x + node[0];
       const $box = $boxes[boxIndex];
       boardNode = 1;
       $box.classList.remove('path')
     }
   }
   path = null;
 }
 
 
 $start.addEventListener('click', () => {
   clearPaths();
 
   if (start.node === null) {
     return alert('Please select start node first.');
   } else if (end.node === null) {
     return alert('Please select end node first.');
   } else if (start.node === null && end.node === null) {
     return alert('Please select start node and end node first.');
   }
 
   // after doing a* algorithm
   const { board: newBoard, path: p } = astar(generatedBoard, start.node, end.node);
   path = p;
   console.log('path', path);
   // render the new board 
   if (path !== null) {
     let $boxes = document.querySelectorAll('.box');
     // make path 
     for (let i = 0; i < path.length; i++) {
       setTimeout(() => {
         const node = path[i];
         console.log('node', node, 'x', x)
         generatedBoard[node[1]][node[0]] = 1;
         const boxIndex = node[1] * x + node[0];
         if (!$boxes[boxIndex].classList.contains('start') && !$boxes[boxIndex].classList.contains('end')) {
           console.log('CAT', boxIndex, $boxes);
           $boxes[boxIndex].classList.add('path');
           console.log('LAH');
         }
       }, i * 50);
     }
   } else {
     alert('Goal is not reachable!!! Try to remove some walls that blocked the path.');
   }
 
 });
 $clear.addEventListener('click', () => {
   clearPaths();
 });
 
 // generate board 
 
 
 
 