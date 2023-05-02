class Graph {
   constructor() {
     this.adjacencyList = new Map();
   }
 
   addVertex(vertex) {
     if (!this.adjacencyList.has(vertex)) {
       this.adjacencyList.set(vertex, []);
     }
   }
 
   addEdge(vertex1, vertex2) {
     if (!this.adjacencyList.has(vertex1)) {
       this.addVertex(vertex1);
     }
     if (!this.adjacencyList.has(vertex2)) {
       this.addVertex(vertex2);
     }
     this.adjacencyList.get(vertex1).push(vertex2);
     this.adjacencyList.get(vertex2).push(vertex1);
   }
 
   dfs(startVertex) {
     const visited = new Set();
     this._dfsHelper(startVertex, visited);
   }
 
   _dfsHelper(vertex, visited) {
     visited.add(vertex);
     console.log(vertex);
 
     const neighbors = this.adjacencyList.get(vertex);
 
     for (const neighbor of neighbors) {
       if (!visited.has(neighbor)) {
         this._dfsHelper(neighbor, visited);
       }
     }
   }
 }
 
 // Example usage
 const graph = new Graph();
 graph.addEdge("0", "1"); graph.addEdge("0", "9");
 graph.addEdge("1", "0"); graph.addEdge("1", "8");
 graph.addEdge("9", "0"); graph.addEdge("9", "8");
 graph.addEdge("8", "1"); graph.addEdge("8", "7"); graph.addEdge("8", "9");
 graph.addEdge("7", "3"); graph.addEdge("7", "6"); graph.addEdge("7", "8"); graph.addEdge("7", "10"); graph.addEdge("7", "11");
 graph.addEdge("6", "7"); graph.addEdge("6", "5");
 graph.addEdge("3", "7"); graph.addEdge("3", "2"); graph.addEdge("3", "4"); graph.addEdge("3", "5");
 graph.addEdge("5", "3"); graph.addEdge("5", "6");
 graph.addEdge("2", "3");
 graph.addEdge("4", "3");
 
 console.log("DFS traversal starting from vertex A:");
 graph.dfs("0");
 