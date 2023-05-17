/*
   LeetCode problem: Maximum Depth of Binary Tree (easy)

   Given the root of a binary tree, return its maximum depth.

   A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

   

   Example 1:
         3
       9  20
         15  7

      Input: root = [3,9,20,null,null,15,7]
      Output: 3

   Example 2:
      Input: root = [1,null,2]
      Output: 2
   

   Constraints:
      - The number of nodes in the tree is in the range [0, 104].
      - -100 <= Node.val <= 100

   Solution by Myself 

   LeetCode submission:
      #1
      Runtime: 79 ms, beats 11.21%
      Memory: 45.8 MB, beats 27.6%

      Runtime: 70 ms, beats 51.53%
      Memory: 44.8 MB, beats 84.71%

      #2
      Runtime: 63 ms, beats 83.73%
      Memory: 45.6 MB, beats 33.52%

      Runtime: 67 ms, beats 66.95%
      Memory: 45.1 MB, beats 67.86%
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

function maximumDepthOfBinaryTree(root) {
   if (!root) return 0;

   function _dfs(node, count) {
      if (!node) return count;
      count++;
      let left = _dfs(node.left, count);
      let right = _dfs(node.right, count);
      // return Math.max(left, right); // <--------- Attempt #1
      return left >= right ? left : right; // <--------- Attempt #2
   }

   let left = _dfs(root.left, 1);
   let right = _dfs(root.right, 1);

   // return Math.max(left, right); // <--------- Attempt #1
   return left >= right ? left : right; // <--------- Attempt #2

}
const root1 = new TreeNode(3,
   new TreeNode(9),
   new TreeNode(20,
      new TreeNode(15),
      new TreeNode(7)
   )
);
/*
        3
      9   20
         15  7
*/
const root2 = new TreeNode(1, 
   null, 
   new TreeNode(2, 
      null, 
      new TreeNode(3, 
         null,
         new TreeNode(4,
            new TreeNode(5)                  
         )
      )
   )
); 
/*
            1
              2
                3
                  4
                5
*/
const root3 = new TreeNode(666);
const root4 = null;
const root5 = new TreeNode(3,
   new TreeNode(9),
   new TreeNode(20,
      new TreeNode(15),
      new TreeNode(7,
         null,
         new TreeNode(8,
            null,
            new TreeNode(11)
         )
      )
   )
);
/*
        3
      9   20
         15  7
               8
                 11
*/
console.log('RESULT: ', maximumDepthOfBinaryTree(root5));