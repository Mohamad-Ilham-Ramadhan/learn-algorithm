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

   Solution by NeetCode: 
      - use iterative post order traversal

   LeetCode submission: 
      #1
      Runtime: 79 ms, beats 35.79%
      Memory: 48.4 MB, beats 61.78%
      #2
      Runtime: 71 ms, beats 71.20%
      Memory: 48.3 MB, beats 68.92%
*/

class TreeNode {
   constructor(val, left, right) {
      this.val = (val === undefined ? 0 : val);
      this.left = (left === undefined ? null : left);
      this.right = (right === undefined ? null : right);
   }
}

function kthSmallest(root, k) {
   let n = 0; // number of elements visited 
   let stack = [];
   let cur = root;

   while (cur || stack.length > 0) {
      while (cur) {
         stack.push(cur);
         cur = cur.left;
      }

      cur = stack.pop();
      n++;
      if (n === k) return cur.val;
      cur = cur.right;
   }
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