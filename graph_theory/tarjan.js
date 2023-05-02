// NGODING SENDIRI 
// Finding Strongly Connected Components using Tarjan's algorithm

function tarjan(graph) {

   const UNVISITED = -1;
   let id = 0;       // used to give each node an id
   let sccCount = 0; // used to count number of SCCs found
   
   let stack = [];
   let onStack = new Map();
   let ids = new Map(); 
   let low = new Map();
   for (let i of graph.keys()) {
     onStack[i] = false;
     ids.set(i, 0);
     low.set(i, 0);
   }
 
   function findScss() {
     for (let i of graph.keys()) {
       ids.set(i,UNVISITED);
     }
     for (let i of graph.keys()) {
       if (ids.get(i) === UNVISITED) {
         console.log('i', i);
         dfs(i);
       }
     }
     return low; // final output of the algorithm;
   }
 
   // A: 0, B: 1, C: 0, X: 3, D: 4, E: 5, F: 6
 
   function dfs(at) {
     console.log('dfs', at);
     stack.push(at);
     onStack.set(at, true);
     ids.set(at, id); low.set(at, id); id++;
 
     const neighbors = graph.get(at);
     // Visit all neighbors & min low-link on callback 
     for (let neighbor of neighbors) {
       console.log('at', at, 'neightbor', neighbor, 'ids.get(neighbor) === UNVISITED', ids.get(neighbor) === UNVISITED);
       if (ids.get(neighbor) === UNVISITED) {
         dfs(neighbor);
       }
       if (onStack.get(neighbor) === true) {
         console.log('ON STACK WOI');
       console.log('at', at, 'neightbor', neighbor, 'onStack.get(neighbor)', onStack.get(neighbor));
       console.log('low.get(at)', low.get(at));
 
         low.set(at, Math.min(low.get(neighbor), low.get(at))) ;
       }
     }
 
     // After having visited all the neighbours of 'at' 
     // If we're at the start of a SCC empty the seen stack until we're back to the start of SCC.
     if (ids.get(at) === low.get(at)) {
       console.log('visited all', 'at', at);
       let node;
       while( node = stack.pop()) {
         onStack.set(node, false);
         low.set(node, ids.get(at))
         if( node === at) break;
       }
       sccCount++;
     }
   }
 
   return findScss();
 
 }
 
 const graph = new Map([
   ["A", ["B"]],
   ["B", ["C"]],
   ["C", ["A", "D"]],
   ["D", ["E"]],
   ["E", ["F"]],
   ["F", ["D"]],
 ]);
 
 const graphX = new Map([
   ["A", ["B"]],
   ["B", ["C"]],
   ["C", ["A", "X"]],
   ["X", ["D"]],
   ["D", ["E"]],
   ["E", ["F"]],
   ["F", ["D"]],
 ]);
 
 console.log('RESULT:', tarjan(graphX));