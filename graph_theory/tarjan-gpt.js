function tarjanAlgorithm(graph) {
   let index = 0;
   let stack = [];
   let indexes = new Map();
   let lowLinks = new Map();
   let onStack = new Set();
   let sccs = [];
 
   for (let node of graph.keys()) {
     if (!indexes.has(node)) {
       strongConnect(node);
     }
   }
 
   function strongConnect(node) {
     indexes.set(node, index);
     lowLinks.set(node, index);
     index++;
     stack.push(node);
     onStack.add(node);
 
     for (let neighbor of graph.get(node)) {
       if (!indexes.has(neighbor)) {
         strongConnect(neighbor);
         lowLinks.set(node, Math.min(lowLinks.get(node), lowLinks.get(neighbor)));
       } else if (onStack.has(neighbor)) {
         lowLinks.set(node, Math.min(lowLinks.get(node), indexes.get(neighbor)));
       }
     }
 
     if (lowLinks.get(node) === indexes.get(node)) {
       let scc = [];
       let curr;
 
       do {
         curr = stack.pop();
         onStack.delete(curr);
         scc.push(curr);
       } while (curr !== node);
 
       sccs.push(scc);
     }
   }
 
   return sccs;
 }

 const graph = new Map([
   ["A", ["B"]],
   ["B", ["C"]],
   ["C", ["A", "D"]],
   ["D", ["E"]],
   ["E", ["F"]],
   ["F", ["D"]],
 ]);
 
 const sccs = tarjanAlgorithm(graph);
 console.log(sccs); // Output: [ ['F', 'E', 'D'], [ 'C', 'B', 'A' ] ]

 