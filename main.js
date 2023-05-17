/*
   LeetCode problem: Same Tree (easy)

   Given the roots of two binary trees p and q, write a function to check if they are the same or not.

   Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



   Example 1:
        1      1
      2   3  2   3

      Input: p = [1,2,3], q = [1,2,3]
      Output: true

   Example 2:
        1 1
      2     2

      Input: p = [1,2], q = [1,null,2]
      Output: false

   Example 3:
        1       1
      2   1   1   2
   
      Input: p = [1,2,1], q = [1,1,2]
      Output: false


   Constraints:
      - The number of nodes in both trees is in the range [0, 100].
      - -104 <= Node.val <= 104

   LeetCode submission:
      Attempt #1
      Runtime: 68 ms, beats 10.55%;
      Memory: 44.1 MB, beats 5.9%;

      Attempt #2
      Runtime: 59 ms, beats 55.90%
      Memory: 42.1 MB, beats 74.22%

      Attempt #3
      Runtime: 61 ms, beats 42.91%
      Memory: 41.9 MB, beats 88.3%

      Attempt #4
      Runtime: 53 ms, beats 82.67%
      Memory: 41.9 MB, beats 82.6%
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

// depth first search
function sameTree(p, q) {
   if (!p && !q) return true;
   if (!p || !q || p.val !== q.val ) return false;
   return (sameTree(p.left, q.left) && sameTree(p.right, q.right));
}
const p1 = new TreeNode(1,
   new TreeNode(2),
   new TreeNode(3)
);
/*
        1
      2   3
*/
const q1 = new TreeNode(1,
   new TreeNode(2),
   new TreeNode(3)
);
/*
         1
       2   3
*/
// ----------------------------------------------------------------
const p2 = new TreeNode(1,
   new TreeNode(2),
   new TreeNode(3)
);
/*
        1
      2   3
*/
const q2 = new TreeNode(1,
   new TreeNode(3),
   new TreeNode(2)
);
/*
         1
       3   2
*/
// ----------------------------------------------------------------
const p3 = new TreeNode(1,
   new TreeNode(2)
);
/*
        1
      2   
*/
const q3 = new TreeNode(1,
   null,
   new TreeNode(2)
);
/*
         1
           2
*/
// ----------------------------------------------------------------
const p4 = null;
const q4 = null;
// ----------------------------------------------------------------
const p5 = null;
const q5 = new TreeNode(5);
console.log('RESULT: ', sameTree(p1, q1));