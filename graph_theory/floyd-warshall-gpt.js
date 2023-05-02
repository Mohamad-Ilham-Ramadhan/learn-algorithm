// Belum dipahami secara manual, susah terlalu banyak soalnya v^3

function floydWarshall(graph) {
   const dist = []; // memo table for dynamic programming
   const n = graph.length;
   
   // Initialize the distance matrix
   for (let i = 0; i < n; i++) {
     dist[i] = [];
     for (let j = 0; j < n; j++) {
       dist[i][j] = graph[i][j];
     }
   }
   const x = [...dist];
   console.log('Dist after initializing distance matrix', x);
   
   // Compute the shortest path between all pairs of vertices
   for (let k = 0; k < n; k++) { // 0
     for (let i = 0; i < n; i++) { // 0
       for (let j = 0; j < n; j++) { // 1
         console.log('k', k, 'i', i, 'j', j);
         console.log('dist[i][j]', dist[i][j], 'dist[i][k]', dist[i][k], 'dist[k][j]', dist[k][j]);
         if (dist[i][j] > dist[i][k] + dist[k][j]) {
           dist[i][j] = dist[i][k] + dist[k][j];
         }
       }
       console.log('=== i++ ===');
     }
     console.log('=== k++ ===');
   }
   
   return dist;
 }
 
 // Example usage
 const graph = [  
   [0, 11, 5, Infinity],
   [Infinity, 0, Infinity, Infinity],
   [Infinity, Infinity, 0, 2],
   [Infinity, 2, Infinity, 0]
 ]; // infinity means not connected
 
 const shortestDistances = floydWarshall(graph);
 console.log(shortestDistances); // Output: [[0, 5, 8, 9], [Infinity, 0, 3, 4], [Infinity, Infinity, 0, 1], [Infinity, Infinity, Infinity, 0]]
 