/*
   LeetCode problem: Subtree of Another Tree (easy) (easy-medium)

   Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

   A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

   

   Example 1:
         root         
          3         subRoot
        4   5         4
      1   2         1   2

      Input: root = [3,4,5,1,2], subRoot = [4,1,2]
      Output: true

   Example 2:
         root         
          3         subRoot
        4   5         4
      1   2         1   2         
         0
      Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2] // penulisannya bfs
      Output: false
   

   Constraints:
      - The number of nodes in the `root` tree is in the range [1, 2000].
      - The number of nodes in the `subRoot` tree is in the range [1, 1000].
      - -104 <= root.val <= 104
      - -104 <= subRoot.val <= 104

   Solution by myself:
      - left or right have the subRoot

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

/*
         root         
          3         subRoot
        4   5         4
      1   2         1   2
*/
function subtreeOfAnotherTree(root, subRoot) {
   // post order traversal
   let deepestLevel = 0;
   function collectSubroot(node, level) {
      if (node === null) {
         return [];
      }
      let left = collectSubroot(node.left, level + 1);
      let right = collectSubroot(node.right, level + 1);
      // console.log('left:', left, 'right:', right, 'node.val', node.val);
      if (deepestLevel === 0 || level > deepestLevel) {
         deepestLevel = level; // <--- this will execute first (deepest)
      }
      return [...left, ...right, {val: node.val, inverseLevel: deepestLevel - level}];
   }

   let subRootArr = collectSubroot(subRoot, 0);
   console.log('subRootArr:', subRootArr);
   let startMatching = false;
   let isMatch = false;
   let i = 0; // subRootArr pointer
   deepestLevel = 0;
   function rootTraversal(node, level) {
      if (node === null) {
         return;
      }
      rootTraversal(node.left, level + 1);
      rootTraversal(node.right, level + 1);
      if (deepestLevel === 0 || level > deepestLevel) {
         deepestLevel = level;
      }
      console.log("deepest level", deepestLevel);
      const inverseLevel = deepestLevel - level;
      console.log('root', node.val, 'inverse level', inverseLevel);

      if (isMatch) return;

      if (!startMatching && inverseLevel === 0 && node.val === subRootArr[0].val) {
         console.log('start matching');
         startMatching = true;
         i = 1; 
         // if next subroot val is undefined then we are in the end of subroot array 
         if (subRootArr[i] === undefined) {
            console.log('reach end and this subroot is TRUE');
            isMatch = true;
         }
         return;
      }
      if (subRootArr[i].inverseLevel === inverseLevel && node.val === subRootArr[i].val) {
         console.log('match');
         i++;
         // if next subroot val is undefined then we are in the end of subroot array 
         if (subRootArr[i] === undefined) {
            console.log('reach end and this subroot is TRUE');
            isMatch = true;
         }
         return;
      } else {
         // not match and node.val is equal to subRootArr[0]
         if (inverseLevel === 0 && node.val === subRootArr[0].val) {
            console.log('not match but start matching')
            i = 1;
         } else {
            // debug [start]
            if (i === 0) {
               console.log('not match the first');
            } else {
               console.log('not match the next');
            }
            // debug [end]
            i = 0;
            startMatching = false;
         }
      }

   }
   rootTraversal(root, 0);

   // console.log('subRootArr', subRootArr);
   // console.log('isMatch', isMatch);

   return isMatch;
}
const root1 = new TreeNode(3,
   new TreeNode(4,
      new TreeNode(1),
      new TreeNode(2)
   ),
   new TreeNode(5)
);
/*
         root         
          3  
        4   5
      1   2
*/
const subRoot1 = new TreeNode(4,
   new TreeNode(1),
   new TreeNode(2)
);
/*
      subRoot
        4 
      1   2
*/ // Expect: true
// ----------------------------------------------------------------
const root2 = new TreeNode(3,
   new TreeNode(4,
      new TreeNode(1),
      new TreeNode(2,
         new TreeNode(0)
      )
   ),
   new TreeNode(5)
);
/*
         root         
          3  
        4   5
      1   2
         0
*/
const subRoot2 = new TreeNode(4,
   new TreeNode(1),
   new TreeNode(2)
);
/*
      subRoot
        4 
      1   2
*/ // Expect: false
// ----------------------------------------------------------------
const root3 = new TreeNode(3,
   new TreeNode(4,
   ),
   new TreeNode(5,
      new TreeNode(1),
      new TreeNode(2)
   )
);
/*
         root         
          3  
        4   5
           1  2
*/
const subRoot3 = new TreeNode(5,
   new TreeNode(1),
   new TreeNode(2)
);
/*
      subRoot
        5 
      1   2
*/ // Expect: true
// ----------------------------------------------------------------
const root4 = new TreeNode(3,
   new TreeNode(4,
   ),
   new TreeNode(5,
      new TreeNode(1),
      new TreeNode(2,
         null,
         new TreeNode(5,
            new TreeNode(1),
            new TreeNode(2)
         )
      )
   )
);
/*
         root         
          3  
        4   5
           1  2
                5
               1  2
*/
const subRoot4 = new TreeNode(5,
   new TreeNode(1),
   new TreeNode(2)
);
/*
      subRoot
        5 
      1   2
*/ // Expect: true
// ----------------------------------------------------------------
const root5 = new TreeNode(3,
   new TreeNode(4),
   new TreeNode(5)
);
/*
         root         
          3  
        4   5
*/
const subRoot5 = new TreeNode(3,
   new TreeNode(4),
   new TreeNode(5)
);
/*
      subRoot
        3 
      4   5
*/  // Expect: true
// ----------------------------------------------------------------
const root6 = new TreeNode(3,
   new TreeNode(4),
   new TreeNode(5,
      new TreeNode(666)
   )
);
/*
         root         
          3  
        4     5
            666
*/
const subRoot6 = new TreeNode(3,
   new TreeNode(4),
   new TreeNode(5)
);
/*
      subRoot
        3 
      4   5
*/  // Expect: false
// ----------------------------------------------------------------
const root7 = new TreeNode(3);
/*
         root         
          3  
*/
const subRoot7 = new TreeNode(3);
/*
      subRoot
        3 
*/  // Expect: true
// ----------------------------------------------------------------
const root8 = new TreeNode(3);
/*
         root         
          3  
*/
const subRoot8 = new TreeNode(6);
/*
      subRoot
        6 
*/  // Expect: false 
// ----------------------------------------------------------------
const root9 = new TreeNode(3,
   new TreeNode(1,
      null,
      new TreeNode(9,
         new TreeNode(6)
      )
   )
);
/*
         root         
          3
         1
           9
         6  
*/
const subRoot9 = new TreeNode(6);
/*
      subRoot
        6 
*/  // Expect: true 
// ----------------------------------------------------------------
const root10 = new TreeNode(1,
   new TreeNode(1)
);
/*
         root         
          1
         1 
*/
const subRoot10 = new TreeNode(1);
/*
      subRoot
        1 
*/  // Expect: true 
// ----------------------------------------------------------------
const root11 = new TreeNode(1,
   new TreeNode(1)
);
/*
         root         
          1
         1 
*/
const subRoot11 = new TreeNode(1,
   new TreeNode(1),
   new TreeNode(2),
);
/*
      subRoot
        1 
      1   2
*/  // Expect: false 
// ----------------------------------------------------------------
const root12 = new TreeNode(3,
   new TreeNode(4,
      new TreeNode(1),
      new TreeNode(2)
   ),
   new TreeNode(5)
);
/*
         root         
           3
         4   5
       1  2   
*/
const subRoot12 = new TreeNode(4,
   new TreeNode(1,
      new TreeNode(1)
   ),
   new TreeNode(2),
);
/*
      subRoot
        4 
      1   2
    1
*/  // Expect: false 
// ----------------------------------------------------------------
const root13 = new TreeNode(1,
   null,
   new TreeNode(1,
      null,
      new TreeNode(1,
         null,
         new TreeNode(1,
            null,
            new TreeNode(1,
               null,
               new TreeNode(1,
                  null,
                  new TreeNode(1,
                     null,
                     new TreeNode(1,
                        null,
                        new TreeNode(1,
                           null,
                           new TreeNode(1,
                              null,
                              new TreeNode(1,
                                 new TreeNode(2)
                              )
                           )
                        )
                     )
                  )
               )
            )
         )
      )
   )
);
/*
         root         
           1
             1
               1
                 1
                   1
                     1
                       1
                         1
                           1
                             1
                               1
                             2  
*/
const subRoot13 = new TreeNode(1,
   null,
   new TreeNode(1,
      null,
      new TreeNode(1,
         null,
         new TreeNode(1,
            null,
            new TreeNode(1,
               null,
               new TreeNode(1,
                  new TreeNode(2)
               )
            )
         )
      )
   )
);
/*
      subRoot
         1
           1
             1
               1
                 1
                   1
                 2  

*/  // Expect: true
// ----------------------------------------------------------------
const root14 = new TreeNode(4,
   new TreeNode(-9,
      null,
      new TreeNode(-1,
         new TreeNode(-6,
            null,
            new TreeNode(-2,
               new TreeNode(-3)
            )
         ),
         new TreeNode(0)
      )

   ),
   new TreeNode(5,
      null,
      new TreeNode(8,
         new TreeNode(7)
      )
   )
);
/*
         root         
           4
        -9    5
          -1     8
       -6    0  7
         -2     
       -3 
*/
const subRoot14 = new TreeNode(5);
/*
      subRoot
         5 

*/  // Expect: false
// ----------------------------------------------------------------
console.log('RESULT: ', subtreeOfAnotherTree(root14, subRoot14));

let deepLevel = 0;
function postOrderTraversal(node, level) {
   if (node === null) {
      return;
   }
   postOrderTraversal(node.left, level + 1);
   postOrderTraversal(node.right, level + 1);
   if (deepLevel === 0) {
      deepLevel = level;
   }
   console.log('level', level, 'deepLevel', deepLevel, 'inverseLevel', deepLevel - level);
   console.log('root', node.val);

}


 // Perform post-order traversal from a leaf node to the root
 console.log('--------------------------------');
//  postOrderTraversal(root12, 0);
//  postOrderTraversal(subRoot12);