/*
   LeetCode: Binary Tree Level Order Traversal (medium)

   Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

   Example 1:
            3
          9   20
             15  7

      Input: root = [3,9,20,null,null,15,7]
      Output: [[3],[9,20],[15,7]]

   Example 2:

      Input: root = [1]
      Output: [[1]]

   Example 3:

      Input: root = []
      Output: []
   

   Constraints:
      - The number of nodes in the tree is in the range [0, 2000].
      - -1000 <= Node.val <= 1000

   Solution by Myself:
      - uses Breadth first search
      - queue 
      - give level each node start from 0 and increment it 
      - use its level for indexing in the result array

   LeetCode submission: 
      # with queue
      Runtime: 88 ms, beats 5.31%
      Memory: 45.4 MB, beats 7.73%
      # without queue 
      Runtime: 79 ms, beats 8.33%
      Memory: 45.6 MB, beats 6.47%
   
*/
class TreeNode {
   constructor(val, left, right) {
      this.val = (val === undefined ? 0 : val)
      this.left = (left === undefined ? null : left)
      this.right = (right === undefined ? null : right)
   }
}

function levelOrder(root) {
   if (root === null) return [];
   class Queue {
      constructor() {
         this.queue = {};
         this.head = 0;
         this.tail = 0;
      }
      enqueue(val) {
         this.queue[this.tail++] = val;
      }
      dequeue() {
         const val = this.queue[this.head];
         delete this.queue[this.head++];
         return val;
      }
      peak() {
         return this.queue[this.head];
      }
      clear() {
         this.head = 0;
         this.tail = 0;
         this.queue = {};
      }
      size() {
         return this.tail - this.head;
      }
   }

   const q = new Queue();
   q.enqueue({ node: root, level: 0 });
   let result = [];
   while (q.size() > 0) {
      const cur = q.dequeue();
      console.log('val', cur.node, 'level', cur.level);
      console.log('result[cur.level]', result[cur.level]);
      if (result[cur.level]) {
         result[cur.level].push(cur.node.val);
      } else {
         result[cur.level] = [cur.node.val];
      }
      if (cur.node.left) {
         q.enqueue({ node: cur.node.left, level: cur.level + 1 });
      }
      if (cur.node.right) {
         q.enqueue({ node: cur.node.right, level: cur.level + 1 });
      }
   }
   return result;

}
// without queue
function bfs(root) {
   if (root === null) return [];
   let result = [];
   let levelNodes = [root]; // Start with the root node
   result = [];
   let level = 0;
   while (levelNodes.length > 0) {
      let nextLevelNodes = [];
      console.log('levelNodes', levelNodes);
      result[level] = [];
      // Process nodes at the current level
      for (let i = 0; i < levelNodes.length; i++) {
         let currentNode = levelNodes[i];
         console.log(currentNode.val); // Process the node value
         result[level].push(currentNode.val);
         // Add children of the current node to the next level
            if (currentNode.left) {
               nextLevelNodes.push(currentNode.left)
               // result[level] = [...]
            };
            if (currentNode.right) { 
               nextLevelNodes.push(currentNode.right)
            };
      }

      levelNodes = nextLevelNodes; // Move to the next level
      level++;
   }
   return result;
}
/*
            3
          9   20
             15  7
*/
const r1 = new TreeNode(3,
   new TreeNode(9),
   new TreeNode(20,
      new TreeNode(15),
      new TreeNode(7)
   ),
)
/*
              3
          9     20
        8  10  15  7
*/
const r2 = new TreeNode(3,
   new TreeNode(9,
      new TreeNode(8),
      new TreeNode(10),
   ),
   new TreeNode(20,
      new TreeNode(15),
      new TreeNode(7)
   ),
)

// console.log('RESULT:', levelOrder(r1));
console.log('RESULT:', bfs(r2));