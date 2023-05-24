/*
   Leetcode: serialize and deserialize binary tree (hard)

   Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

   Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

   Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.



   Example 1:
        1
      2    3
         4   5

      Input: root = [1,2,3,null,null,4,5]
      Output: [1,2,3,null,null,4,5]

   Example 2:

      Input: root = []
      Output: []


   Constraints:
      - The number of nodes in the tree is in the range [0, 104].
      - -1000 <= Node.val <= 1000
*/


class TreeNode {
   constructor(val) {
      this.val = val;
      this.left = this.right = null;
   }
}


/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function (root) {
   console.log(JSON.stringify(root));
   return JSON.stringify(root);
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function (data) {
   console.log(JSON.parse(data))
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */

const root1 = new TreeNode(1);
root1.left = new TreeNode(2);
root1.right = new TreeNode(3);
/*
        1
      2   3
*/
const root2 = new TreeNode(1);
root2.left = new TreeNode(2);
root2.right = new TreeNode(3);
root2.right.left = new TreeNode(4);
root2.right.right = new TreeNode(5);

/*
         1
      2     3
           4  5
*/
const root3 = null;
console.log('RESULT: ',deserialize(serialize(root3)));