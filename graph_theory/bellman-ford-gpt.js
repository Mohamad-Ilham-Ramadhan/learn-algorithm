function bellmanFord(edges, source) {
   let distances = {};
   let parents = {};
   let vertices = [];
 
   // Step 1: Initialize distances and parents
   for (let edge of edges) {
     let [u, v, weight] = edge;
     if (distances[u] === undefined) {
       distances[u] = Infinity;
       parents[u] = null;
       vertices.push(u);
     }
     if (distances[v] === undefined) {
       distances[v] = Infinity;
       parents[v] = null;
       vertices.push(v);
     }
   }
   distances[source] = 0;
 
   // Step 2: Relax edges repeatedly => O(V*E). Dengan menggunakan loop Bellman-Ford bisa keluar dari jebakan negative-weight cycle
   for (let i = 0; i < vertices.length - 1; i++) {
     let relaxed = 0;
     for (let edge of edges) {
       let [u, v, weight] = edge;
       if (distances[u] + weight < distances[v]) {
         distances[v] = distances[u] + weight;
         parents[v] = u;
         relaxed++;
       }
     }
     console.log('================================================================');
     if (relaxed === 0) break; // jika gak ada yang di relax maka sudahi relax edges (untuk optimisasi) berarti semua distances sudah benar (shortest). Jika ada NEGATIVE-WEIGHT CYCLES maka akan selalu ada edge yang di relax.
   }
 
   // Step 3: Check for negative-weight cycles
   for (let edge of edges) {
     let [u, v, weight] = edge;
     if (distances[u] + weight < distances[v]) {
       throw new Error('Graph contains a negative-weight cycle' + ' u '+ u+ ' v '+ v);
     }
   }
 
   return { distances, parents };
 }
 
 // Example usage:
 let edges = [
   ['s', 'a', 10],
   ['s', 'e', 8],
   ['e', 'd', 1],
   ['a', 'c', 2],
   ['d', 'c', -1], 
   ['d', 'a', -4], 
   ['c', 'b', -2], 
   ['b', 'a', 1],
 ];
 let edgesWithNegativeWeightCycle = [
   ['s', 'a', 10],
   ['s', 'e', 8],
   // negative-weight cycle
   ['s', 'f', 1],
   ['f', 'g', -1],
   ['g', 'h', 2],
   ['h', 'f', -4],
   // negative-weight cycle
   ['e', 'd', 1],
   ['a', 'c', 2],
   ['d', 'c', -1], 
   ['d', 'a', -4], 
   ['c', 'b', -2], 
   ['b', 'a', 1],
 ];
 let source = 's';
 let { distances, parents } = bellmanFord(edges, source);
 console.log('distances', distances); 
 console.log('parents', parents); 