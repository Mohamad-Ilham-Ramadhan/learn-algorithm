// CODINGAN SENDIRI
// Breadth First Search finding shortest path in unweighted undirected graph 


function bfs(g, s, d) {
   let queue = [];
   let costTable = {};
 
   queue.push(s);
   costTable[s] = {cost: 0, prev: null};
 
   function _bfsHelper() {
     while (queue.length > 0) {
       let u = queue.shift();
       console.log('Current vertex', u);
       for (let v of g[u]) {
         if (costTable[v] === undefined) {
           costTable[v] = { cost: costTable[u].cost + 1, prev: u};
           queue.push(v);
         }
       }
     }
   }
 
   _bfsHelper();
 
   function findingPath(v) {
     if (costTable[v].prev === null) return [v];
     
     return findingPath(costTable[v].prev).concat(v);
   }
 
   const shortestPath = findingPath(d);
   console.log('costTable', costTable, 'shortestPath', shortestPath);
 }
 
 // Lihat gambar: breadth-first-search-graph-image.png
 const graph = {
   10: [1, 9],
   1: [10, 8],
   9: [10, 8, 0],
   8: [1, 9, 12],
   0: [9, 7, 11],
   12: [8, 2],
   11: [0, 7],
   2: [12, 3],
   7: [0, 11, 3, 6],
   3: [2, 7, 4],
   6: [7, 5],
   4: [3],
   5: [6]
 };
 const start = 10;
 const destination = 2;
 
 bfs(graph, start, destination);