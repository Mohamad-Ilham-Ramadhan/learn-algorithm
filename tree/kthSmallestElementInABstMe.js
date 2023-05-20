/*
   LeetCode: Kth Smallest Element in a BST (medium)

   Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

   Example 1:
              3
           1     4
            2

      Input: root = [3,1,4,null,2], k = 1
      Output: 1

   Example 2:
               5
             3    6
           2  4
         1

      Input: root = [5,3,6,2,4,null,null,1], k = 3
   Output: 3
   

   Constraints:
      - The number of nodes in the tree is n.
      - 1 <= k <= n <= 104
      - 0 <= Node.val <= 104
   

   FOLLOW UP: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

   Solution by myself: 
      - use post order traversal it will visit from smallest to largest
      - use index and increment it after visiting each node 
      - if index === k then the result is node.val

   LeetCode submission: 
      #1
      Runtime: 74 ms, beats 58.13%
      Memory: 48.4 MB, beats 53.28%;
      #2
      Runtime: 79 ms, beats 35.67%
      Memory: 48.6 MB, beats 38.36%;
*/

class TreeNode {
   constructor(val, left, right) {
      this.val = (val === undefined ? 0 : val);
      this.left = (left === undefined ? null : left);
      this.right = (right === undefined ? null : right);
   }
}

function kthSmallest(root, k) {
   // Attempt #1 [start]
   let index = 1;
   let result = null;
   function postOrder(node) {
      if (!node) return;
      postOrder(node.left);
      // if (k === 0) return;
      console.log('val', node.val, 'k', k, 'index', index);
      if (k === index) {
         /* Attempt #1
            result = node.val;
         */
         // Attempt #2 [start]
         result = result === null ? node.val : result;
         return;
         // Attempt #2 [end]
      };
      index++;
      postOrder(node.right);
   }
   postOrder(root);
   return result;
   // Attempt #1 [end]
}
/*
              3
           1     4
            2
*/
const r1 = new TreeNode(3,
   new TreeNode(1,
      null,
      new TreeNode(2)
   ),
   new TreeNode(4),
); const k1 = 1;
console.log('RESULT: ', kthSmallest(r1, k1));