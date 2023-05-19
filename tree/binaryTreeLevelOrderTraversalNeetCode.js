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

   Solution by NeetCode

   LeetCode submission: 
      Runtime: 78 ms, beats 11.52%
      Memory: 46.3 MB, beats 5.50%
   
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

   let res = [];

   let q = new Queue();
   q.enqueue(root);

   while (q.size()) {
      const qLen = q.size();
      let level = [];
      for (let i = 0; i < qLen; i++) {
         const node = q.dequeue();
         if (node) {
            level.push(node.val);
            q.enqueue(node.left);
            q.enqueue(node.right);
         }
      }
      if (level.length) res.push(level);
   }
   
   return res;
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