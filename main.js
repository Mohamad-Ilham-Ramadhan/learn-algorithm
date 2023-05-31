/*
  133. Clone Graph (medium)

  Given a reference of a node in a connected undirected graph.

  Return a deep copy (clone) of the graph.

  Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

  class Node {
      public int val;
      public List<Node> neighbors;
  }
  

  Test case format:

  For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with `val == 1`, the second node with `val == 2`, and so on. The graph is represented in the test case using an adjacency list.

  An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

  The given node will always be the first node with `val = 1`. You must return the copy of the given node as a reference to the cloned graph.

  

  Example 1:
                          1--------------------2
                          |   you can't return |
               |-------x  |    the same graph  |
               |          4--------------------3
               |
    1--------------------2                1-----------------------------2
    |    original        |   -------->    |    This looks like a        |
    |     graph          |                |    clone. The nodes are     |
    4--------------------3                |  New. Graph looks the same  |
              |                           4-----------------------------3
              |
              |             1---------------------------3              
              |             |   The nodes were          |
              |--------x    |   cloned. But the graph   |
                            |   is messed up. Doesn't   |
                            |    have same connections. |         
                            4---------------------------2

    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
    Explanation: There are 4 nodes in the graph.
      1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
      2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
      3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
      4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

  Example 2:


    Input: adjList = [[]]
    Output: [[]]
    Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

  Example 3:
    Input: adjList = []
    Output: []
    Explanation: This an empty graph, it does not have any nodes.
  

  Constraints:
    - The number of nodes in the graph is in the range [0, 100].
    - 1 <= Node.val <= 100
    - Node.val is unique for each node.
    - There are no repeated edges and no self-loops in the graph.
    - The Graph is connected and all nodes can be visited starting from the given node.

  Solution by myself:
    using bfs -> deque 
    hashmap to store all new created nodes reference 
  

  LeetCode submission: 
    Runtime: 64 ms, beats 48.9%
    Memory: 44.2 MB, beats 23.21%
*/

// Definition for a Node.
class Node {
  constructor(val, neighbors) {
    this.val = val === undefined ? 0 : val;
    this.neighbors = neighbors === undefined ? [] : neighbors;
  }
};

// self made deque
class Deque {
  constructor() {
    this.items = {};
    this.frontIndex = 0;
    this.endIndex = 1;
    this.size = 0;
  }

  // Add an element to the front of the deque
  addFront(element) {
    this.items[this.frontIndex] = element;
    // this.endIndex = this.frontIndex === 0 && this.endIndex === 0 ? 1 : this.endIndex;
    this.frontIndex--;
    this.size++;
  }

  // Add an element to the rear of the deque
  addRear(element) {
    this.items[this.endIndex] = element;
    // this.frontIndex = this.endIndex === 0 && this.frontIndex === 0 ? -1 : this.frontIndex;
    this.endIndex++;
    this.size++;
  }

  // Remove and return the element from the front of the deque
  removeFront() {
    if (this.isEmpty()) {
      return null;
    }
    const front = this.items[this.frontIndex + 1];
    delete this.items[this.frontIndex + 1];
    this.frontIndex++;
    this.size--;
    return front;
  }

  // Remove and return the element from the rear of the deque
  removeRear() {
    if (this.isEmpty()) {
      return null;
    }
    const end = this.items[this.endIndex - 1];
    delete this.items[this.endIndex - 1];
    this.endIndex--;
    this.size--;
    return end;  
  }

  // Return the element at the front of the deque without removing it
  peekFront() {
    if (this.isEmpty()) {
      return null;
    }
    return this.items[this.frontIndex + 1];
  }

  // Return the element at the rear of the deque without removing it
  peekRear() {
    if (this.isEmpty()) {
      return null;
    }
    return this.items[this.endIndex - 1];
  }

  // Check if the deque is empty
  isEmpty() {
    return this.size === 0;
  }

  // Return the size of the deque

  // Clear the deque
  clear() {
    this.items = {};
    this.frontIndex = 0;
    this.endIndex = 0;
    this.size = 0;
  }
}

/**
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function(node) {
  if (node === null) return null;
  let nodeMap = {}; // to store all new nodes reference
  let visited = new Set();
  let q = new Deque();

  nodeMap[node.val] = new Node(node.val, []);

  for (let neighbor of node.neighbors) {
    nodeMap[neighbor.val] = new Node(neighbor.val, []);
    nodeMap[node.val].neighbors.push(nodeMap[neighbor.val]);
    q.addFront(neighbor);
  }
  visited.add(node.val);

  while (q.size > 0) {
    const curNode = q.removeRear();
    if (visited.has(curNode.val)) continue;
    nodeMap[curNode.val] = nodeMap[curNode.val] ? nodeMap[curNode.val] : new Node(curNode.val, []);

    for (let neighbor of curNode.neighbors) {
      nodeMap[neighbor.val] = nodeMap[neighbor.val] ? nodeMap[neighbor.val] : new Node(neighbor.val, []);
      nodeMap[curNode.val].neighbors.push(nodeMap[neighbor.val]);
      if (!visited.has(neighbor.val)) {
        q.addFront(neighbor);
      }
    }
    visited.add(curNode.val);
  }
  return nodeMap[1];
};
let n4 = new  Node(4,[])
let n3 = new  Node(3,[])
let n2 = new  Node(2,[])
let n1 = new  Node(1,[])
n4.neighbors.push(n1); n4.neighbors.push(n3);
n3.neighbors.push(n2); n3.neighbors.push(n4);
n2.neighbors.push(n1); n2.neighbors.push(n3);
n1.neighbors.push(n2); n1.neighbors.push(n4);

console.log('RESULT: ', cloneGraph(n1));
