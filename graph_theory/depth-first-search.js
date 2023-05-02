// CODINGAN SENDIRI
// mencari jalur traversal dan component-component pada graph

function dfs(g, start) {
  // simpan neighbors di priority queue 
  let visited = {};
  for (let v in g) {
    visited[v] = false;
  }

  let traversal = [];
  let components = {};
  let id = 1;


  function _dfsHelper(g, v) {
    traversal.push(v);
    // if (visited[v]) return;
    visited[v] = true;
    components[id] = components[id] !== undefined ? [...components[id], v] : [v];
    for (let neighbor of g[v]) {
      if (!visited[neighbor]) {
        _dfsHelper(g, neighbor);
      }
    }
  }

  // search for other components if there is still not visited vertexs
  // let unvisited = visited
  for ( let v in visited ) {
    if (visited[v] === false) {
      _dfsHelper(g, Number(v));  
      id++;
    }
  }

  return {traversal, components};
}

const graphx = {
  0: [9, 1],
  1: [0, 8],
  9: [8, 0],
  8: [1, 7, 9],
  7: [3, 6, 8, 10, 11],
  6: [7, 5],
  3: [7, 2, 4, 5],
  5: [3, 6],
  2: [3],
  4: [3],
  10: [7, 11],
  11: [7, 10],
  // other component 
  12: [13, 14],
  13: [14, 12],
  14: [12, 13],
  // other component 
  15: [16],
  16: [15],
  17: [],
}; // adjacency list

console.log('RESULT:', dfs(graphx, 0));





