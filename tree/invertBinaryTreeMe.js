/*
   LeetCode problem: Invert Binary Tree (easy)

   Given the root of a binary tree, invert the tree, and return its root.

 

   Example 1:
           4                     4
        2    7   -------->    7    1
      1  3  6  9            9  6  3  1

      Input: root = [4,2,7,1,3,6,9]
      Output: [4,7,2,9,6,3,1]

   Example 2:
        2  ------------>   2
      1  3                3  1

      Input: root = [2,1,3]
      Output: [2,3,1]

   Example 3:
      Input: root = []
      Output: []
   

   Constraints:

   The number of nodes in the tree is in the range [0, 100].
   -100 <= Node.val <= 100

   LeetCode submission:
      Runtime: 68 ms, beats 12.5%
      Memory: 42.5 MB, beats 29.55%
*/
/*
  Definition for a binary tree node.
*/
class TreeNode {
   constructor(val, left, right) {
      this.val = (val === undefined ? 0 : val)
      this.left = (left === undefined ? null : left)
      this.right = (right === undefined ? null : right)
   }
}

function invertBinaryTree(root) {
   if (root === null || (root.left === null && root.right === null)) return root;

   let left = root.left
   root.left = root.right;
   root.right = left;

   invertBinaryTree(root.left); invertBinaryTree(root.right);

   return root;
}
/*
           4                     4
        2    7   -------->    7    2
      1  3  6  9            9  6  3  1
*/
const root1 = new TreeNode(4,
   new TreeNode(2,
      new TreeNode(1),
      new TreeNode(3)
   ),
   new TreeNode(7,
      new TreeNode(6),
      new TreeNode(9)
   )   
);
const root2 = new TreeNode(1,null, 
   new TreeNode(2,
      new TreeNode(4), 
      new TreeNode(3)
   )
)
/*
      1              1
       2   ----->   2
      4 3          3 4
*/
console.log('INVERT: ', invertBinaryTree(root2))