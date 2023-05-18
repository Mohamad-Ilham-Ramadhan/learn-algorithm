/*
   Lowest Common Ancestor of a Binary Search Tree (medium)

   Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

   According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

   

   Example 1:
             6
        2        8
      0   4    7  9
         3  5


      Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
      Output: 6
      Explanation: The LCA of nodes 2 and 8 is 6.

   Example 2:
             6
        2        8
      0   4    7  9
         3  5

      Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
      Output: 2
      Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

   Example 3:
         2
       1
      Input: root = [2,1], p = 2, q = 1
      Output: 2
   

   Constraints:
      - The number of nodes in the tree is in the range [2, 105].
      - -109 <= Node.val <= 109
      - All Node.val are unique.
      - p != q
      - p and q will exist in the BST.

   Solution by NeetCode

   LeetCode submission: 
      Runtime: 82 ms, beats 66.79%
      Memory: 52.2 MB, beats 40.57%
*/


// Definition for a binary tree node.
class TreeNode {
   constructor(val) {
      this.val = val;
      this.left = null;
      this.right = null;
   }
}

// Time complexity: O( log n) and space complexity O(1)
function lowestCommonAncestor(root, p, q) {
   while (root) {
      if (p.val > root.val && q.val > root.val) {
         root = root.right;
      } else if (p.val < root.val && q.val < root.val) {
         root = root.left;
      } else {
         return root;
      }
   }
}


/*
         6
       /   \
      2     8
     / \   / \
    0   4 7   9
       / \
      3   5
*/

let r1 = new TreeNode(6);
r1.left = new TreeNode(2);
r1.right = new TreeNode(8);
r1.left.left = new TreeNode(0);
r1.left.right = new TreeNode(4);
r1.right.left = new TreeNode(7);
r1.right.right = new TreeNode(9);
r1.left.right.left = new TreeNode(3);
r1.left.right.right = new TreeNode(5);
const p1 = 2; const q1 = 8;
console.log('RESULT:', lowestCommonAncestor(r1, r1.left, r1.right)) // TreeNode(6)
console.log('RESULT:', lowestCommonAncestor(r1, r1.left, r1.left.right)) // TreeNode(2)
console.log('RESULT:', lowestCommonAncestor(r1, r1.left.right.left, r1.left.right.right)) // TreeNode(4)






