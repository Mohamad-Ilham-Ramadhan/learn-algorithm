/*
   LeetCode: Validate Binary Search Tree (medium)

   Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

   A valid BST is defined as follows:

   The left 
   subtree
   of a node contains only nodes with keys less than the node's key.
   The right subtree of a node contains only nodes with keys greater than the node's key.
   Both the left and right subtrees must also be binary search trees.
   

   Example 1:
        2
      1   3

      Input: root = [2,1,3]
      Output: true

   Example 2:
         5
      1    4
         3   6

      Input: root = [5,1,4,null,null,3,6]
      Output: false
      Explanation: The root node's value is 5 but its right child's value is 4.
   

   Constraints:
      - The number of nodes in the tree is in the range [1, 104].
      - -231 <= Node.val <= 231 - 1

   Solution by NeetCode

   LeetCode submission:
      Runtime: 71 ms, beats 59.32%
      Memory: 46.1 MB, beats 85.80%
*/

class TreeNode {
   constructor(val, left, right) {
      this.val = (val === undefined ? 0 : val)
      this.left = (left === undefined ? null : left)
      this.right = (right === undefined ? null : right)
   }
}

// Time complexity O(n) space complexity O(1)
function isValidBST(root) {
   function isValid(node, left, right) {
      if (!node) return true;
      if (! (node.val < right && node.val > left) ) return false;

      return (isValid(node.left, left, node.val) && isValid(node.right, node.val, right));
   }

   return isValid(root, -Infinity, Infinity);
}
/*
        2
      1   3
*/
const r1 = new TreeNode(2,
   new TreeNode(1),
   new TreeNode(3)
); // expect: TRUE
/*
          5
      1      4
           3   6
*/
const r2 = new TreeNode(5,
   new TreeNode(1),
   new TreeNode(4,
      new TreeNode(3),
      new TreeNode(6)
   )
); // expect: FALSE
const r3 = new TreeNode(5); // expect: TRUE
/*
          5
      1      6
           7   8
*/
const r4 = new TreeNode(5,
   new TreeNode(1),
   new TreeNode(6,
      new TreeNode(7),
      new TreeNode(8)
   )
); // expect: FALSE
/*
          5
      4      6
           3   7
*/
const r5 = new TreeNode(5,
   new TreeNode(1),
   new TreeNode(6,
      new TreeNode(3), // <---- harusnya ada di left tree (FALSE)
      new TreeNode(7)
   )
);
/*
         9
    8         22
          15      25
      10   17   14   26
*/
const r6 = new TreeNode(9, 
   new TreeNode(8,
      new TreeNode(1),
      new TreeNode(11),
   ),
   new TreeNode(22,
      new TreeNode(15,
         new TreeNode(10),
         new TreeNode(17),
      ),
      new TreeNode(25,
         new TreeNode(14),
         new TreeNode(26),
      ),
   ),
);
/*
           2
         2   2
*/
const r7 = new TreeNode(2,
   new TreeNode(2),
   new TreeNode(2),
); // expect: FALSE
console.log('RESULT: ', isValidBST(r7));