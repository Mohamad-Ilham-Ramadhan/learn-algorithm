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

   Solution by myself:
      - use BFS
      - check every node if it is in the right side by tracking their path

   LeetCode submission:
      Attempt #1
      Runtime: 94 ms, beats 5.18%
      Memory: 49.4 MB, beats 5%
      Attempt #2
      Runtime: 86 ms, beats 7.8%
      Memory: 49.7 MB, beats 5%
      ### The Best Solution
      Runtime : 46 ms, beats 99.93%
      Memory: : 44.9 MB, beats 99.93%
*/

class TreeNode {
   constructor(val, left, right) {
      this.val = (val === undefined ? 0 : val)
      this.left = (left === undefined ? null : left)
      this.right = (right === undefined ? null : right)
   }
}

function isValidBST(root) {
   let nodes = [{node: root, path: []}];
   while (nodes.length) {
      let newNodes = [];

      for (let i = 0; i < nodes.length; i++) {
         const {node, path} = nodes[i];
         if (node) {
            console.log(node.val);
            console.log(path);

            // check if the node valid 
            let current = root;
            for (let x = 0; x < path.length; x++) {
               if (path[x] === 'l') {
                  if (node.val >= current.val) return false;
                  current = current.left;
               }
               if (path[x] === 'r') {
                  if (node.val <= current.val) return false;
                  current = current.right;
               }
            }
            // Attempt #2 [start]
            // if (node.left !== null && node.left.val >= node.val) {
            //    console.log('node left smaller', node.left)
            //    return false
            // };
            // if (node.right !== null && node.right.val <= node.val) {
            //    console.log('node right smaller', node.right)
            //    return false
            // };
            // Attempt #2 [end]

            newNodes.push({ node: node.left, path: path.concat('l') });
            newNodes.push({ node: node.right, path: path.concat('r')});
         }

      }

      nodes = newNodes;
   }
   return true;
}

// This is the best solution from other people on LeetCode
var isValidBSTTheBest = function(root) {

   var dfs = function(root, lower, upper) {
       if (!root) {
           return true
       }

       if (root.val <= lower || root.val >= upper) {
           return false
       }

       return dfs(root.left, lower, root.val) && dfs(root.right, root.val, upper)
   }

   return dfs(root, -Infinity, Infinity)

};
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
console.log('--------------------------------');
console.log('THE BEST :', isValidBSTTheBest(r5));