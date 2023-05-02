// NGODING SENDIRI

function prim(graph) {
   let mst = [];
   let pq = [];
   const graphLength = Object.keys(graph).length;
 
   let visited = Object.keys(graph).map(key => false);
 
   let startVertex = Math.floor(Math.random() * (graphLength));
   visited[startVertex] = true;
 
   console.log('START VERTEX', startVertex);
 
   function enqueueNeighbors(vertex) {
     for (let i = 0; i < graph[vertex].length; i++) {
       const v = graph[vertex][i];
       if (visited[v[0]]) { continue;}
       let added = false;
       // enqueue 
       if (pq.length === 0) {
         pq.push(v); continue;
       }
       for (let i = 0; i < pq.length; i++) {
         if (v[1] < pq[i][1]) {
           pq.splice(i, 0, v);
           added = true;
           break;
         }
       }
       if (!added) {
         pq.push(v);
       }
     }
   }
 
   // initialize 
   enqueueNeighbors(startVertex);
 
   while (pq.length > 0 && mst.length < graphLength) {
     const vertex = pq.shift(); // dequeue
     visited[vertex[0]] = true; 
 
     if (mst[vertex[0]] === undefined ) {
       mst[vertex[0]] = vertex;
     }
 
     enqueueNeighbors(vertex[0]);
   }
 
   return {mst, mstCost: mst.reduce( (acc, ve) => acc + ve[1] ,0)}
 }
 
 const graph = {
   0: [[1, 10], [2, 1], [3, 4]],
   1: [[2, 3], [4, 0], [0, 10]],
   2: [[5, 8], [3, 2], [0, 1], [1, 3]],
   3: [[0, 4], [2, 2], [5, 2], [6, 7]],
   4: [[1, 0], [7, 8], [5, 1]],
   5: [[4, 1], [2, 8], [3, 2], [6, 6], [7, 9]],
   6: [[3, 7], [5, 6], [7, 12]],
   7: [[5, 9], [6, 12], [4, 8]]
 }; // { vertex: [[vertex, weight], [vertex, weight], ...]
 
 console.log(prim(graph));
 
 
 