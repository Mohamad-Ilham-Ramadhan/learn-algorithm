function dijkstra(graph, start) {
   const distances = {};
   const visited = {};
   const previous = {};
   const pq = new PriorityQueue();
 
   for (let vertex in graph) {
     distances[vertex] = Infinity;
     previous[vertex] = null;
   }
 
   distances[start] = 0;
   pq.enqueue(start, 0);
 
   while (!pq.isEmpty()) {
     const currentVertex = pq.dequeue().element;
 
     if (visited[currentVertex]) continue;
 
     visited[currentVertex] = true;
 
     for (let neighbor in graph[currentVertex]) {
       const distance = graph[currentVertex][neighbor];
       const totalDistance = distances[currentVertex] + distance;
 
       if (totalDistance < distances[neighbor]) {
         distances[neighbor] = totalDistance;
         previous[neighbor] = currentVertex;
         pq.enqueue(neighbor, totalDistance);
       }
     }
   }
 
   return {
     distances,
     previous
   };
 }
 
 class PriorityQueue {
   constructor() {
     this.items = [];
   }
 
   enqueue(element, priority) {
     const item = { element, priority };
     let added = false;
 
     for (let i = 0; i < this.items.length; i++) {
       if (item.priority < this.items[i].priority) {
         this.items.splice(i, 0, item);
         added = true;
         break;
       }
     }
 
     if (!added) {
       this.items.push(item);
     }
   }
 
   dequeue() {
     return this.items.shift();
   }
 
   isEmpty() {
     return this.items.length === 0;
   }
 }

 
 const graph = {
   A: { B: 5, C: 1 },
   B: { A: 5, C: 2, D: 1 },
   C: { A: 1, B: 2, D: 4 },
   D: { B: 1, C: 4 }
 };

 const graphNegativeDirected = {
  A: { B: 3, C: 6 },
  B: { C: 4, D: 4, E: 11 },
  C: { D: 8, G: 11 },
  D: { E: -4, F: 5, G: 2 },
  E: { H: 9 },
  F: { H: 1 },
  G: { H: 2 },
 };
 
 const startVertex = 'A';
 
 const result = dijkstra(graphNegativeDirected, startVertex);
 
 console.log(result.distances); // { A: 0, B: 3, C: 1, D: 4 }
 console.log(result.previous); // { A: null, B: 'A', C: 'A', D: 'B' }