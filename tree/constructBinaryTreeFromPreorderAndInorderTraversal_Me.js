/*
   LeetCode: Construct a binary tree from preorder and inorder traversal (medium)

   Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

 

   Example 1:
         3
      9       20
            5    7

      Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
      Output: [3,9,20,null,null,15,7]

   Example 2:
      Input: preorder = [-1], inorder = [-1]
      Output: [-1]
      

   Constraints:
      - 1 <= preorder.length <= 3000
      - inorder.length == preorder.length
      - -3000 <= preorder[i], inorder[i] <= 3000
      - preorder and inorder consist of unique values.
      - Each value of inorder also appears in preorder.
      - preorder is guaranteed to be the preorder traversal of the tree.
      - inorder is guaranteed to be the inorder traversal of the tree.

   Solution by myself: 
      - use stack for 
      - two pointers for preorder and inorder
      - var current for current node (pointer)

      - while current inorder.val === last stack element's value
         - current = stack.pop();
         - inorder = next inorder 
         - next add is right side 
      
      - current.left/right = preorder[i];
      - current = current.left/right
      - stack.push(current);
      - next add is left side

   LeetCode submission (Pretty Good :D ):
      - Runtime: 64 ms, beats 98.95%
      - Memory: 44.7 MB, beats 91.32%
*/

class TreeNode {
   constructor(val, left, right) {
      this.val = (val === undefined ? 0 : val)
      this.left = (left === undefined ? null : left)
      this.right = (right === undefined ? null : right)
   }
}

function buildTree(preorder, inorder) {
   let result = new TreeNode(preorder[0]);
   let stack = [result];
   let current = result;
   let j = 0; // inorder pointer
   let addSide = 0; // 0 left, 1 right
   for (let i = 1; i < preorder.length; i++) {
      console.log('ADD LEFT', current.val);
      console.log('stack[stack.length - 1]', stack[stack.length - 1].val);

      // going up the tree;
      while (inorder[j] === stack[stack.length - 1].val) {
         current = stack.pop();
         j++;
         addSide = 1; // if going up then the next add side is right
         if (stack[stack.length - 1] === undefined) break;
      }

      // going down the tree after adding
      if (addSide === 0) {
         current.left = new TreeNode(preorder[i]);
         current = current.left;
      } else {
         current.right = new TreeNode(preorder[i]);
         current = current.right;
      }
      stack.push(current);
      addSide = 0;

      /*
                         25
                 15                 50
           10         22        35        70
         4    7     18   24   31   40   55   66
         preorder [25,15,10,4,7,22,18,24,50,35,31,40,70,55,66] inorder [4,10,7,15,18,22,24,25,31,35,40,50,55,70,66]
         in 31
         cur 25
         add 50
         stack []
            kanan
         add kanan jika up
         after add jadi down
      */
   }
   return result;
}
const preorder1 = [3, 9, 20, 15, 7]; const inorder1 = [9, 3, 15, 20, 7]; // true 
const preorder2 = [-1]; const inorder2 = [-1];
const preorder3 = [25, 15, 10, 4, 12, 22, 18, 24, 50, 35, 31, 44, 70, 66, 90]; const inorder3 = [4, 10, 12, 15, 18, 22, 24, 25, 31, 35, 44, 50, 66, 70, 90];
const preorder4 = [25, 15, 10, 4, 12, 22, 18, 24, 50, 35, 31, 70, 66]; const inorder4 = [4, 10, 12, 15, 18, 22, 24, 25, 31, 35, 50, 66, 70];

const preorder5 = [25, 15, 10, 4, 7, 22, 18, 24, 50, 35, 31, 40, 70, 55, 66]; const inorder5 = [4, 10, 7, 15, 18, 22, 24, 25, 31, 35, 40, 50, 55, 70, 66]; // true
/*
                   25
           15                 50
     10         22        35        70
   4    7     18   24   31   40   55   66
   preorder [25,15,10,4,7,22,18,24,50,35,31,40,70,55,66] inorder [4,10,7,15,18,22,24,25,31,35,40,50,55,70,66]
*/
const preorder6 = [5, 4, 3, 6, 7]; const inorder6 = [3, 4, 5, 6, 7]; // true
const preorder7 = [6, 4, 3, 5, 8, 7, 9]; const inorder7 = [3, 4, 5, 6, 7, 8, 9] // true 
/*
              6
           4     8
         3   5  7  9
*/
const preorder8 = [25, 15, 10, 4, 22, 24, 50, 35, 31, 70, 66]; const inorder8 = [4, 10, 15, 22, 24, 25, 31, 35, 50, 70, 66]; // true
/*
                   25
           15                 50
     10         22        35      70
   4               24   31           66
   preorder [25,15,10,4,22,24,50,35,31,70,66] inorder [4,10,15,22,24,25,31,35,50,70,66]
*/
const preorder9 = [1, 2]; const inorder9 = [1, 2]; // true
const preorder10 = [1, 2]; const inorder10 = [2, 1]; // 


console.log('RESULT: ', buildTree(preorder8, inorder8));

/*
   inorder undefined
   cur 70
   stack [25, 70]
   
   jika ketemu dan kanan kiri null maka ke atas
   jika naik dan kanan null maka turun ke kanan

*/

/*
                   25
           15                 50
     10         22        35      70
   4   12    18   24   31       66
*/
const root1 = new TreeNode(25,
   new TreeNode(15,
      new TreeNode(10,
         new TreeNode(4),
         new TreeNode(12),
      ),
      new TreeNode(22,
         new TreeNode(18),
         new TreeNode(24),
      ),
   ),
   new TreeNode(50,
      new TreeNode(35,
         new TreeNode(31),
         // new TreeNode(44),
      ),
      new TreeNode(70,
         new TreeNode(66),
         // new TreeNode(90)
      ),
   ),
);

/*
              5
           4     6
         3         7

         preorder [5,4,3,6,7] inorder [3,4,5,6,7]

         in null
         cur 7
         next add null
         stack []

         add kanan jika stack kosong
      
*/
const root2 = new TreeNode(5,
   new TreeNode(4,
      new TreeNode(3)
   ),
   new TreeNode(6,
      null,
      new TreeNode(7),
   )
);

const root3 = new TreeNode(6,
   new TreeNode(4,
      new TreeNode(3),
      new TreeNode(5),
   ),
   new TreeNode(8,
      new TreeNode(7),
      new TreeNode(9)
   )
);
/*
              6
           4     8
         3   5  7  9
*/
// preorder = [6,4,3,5,8,7,9]; inroder = [3,4,5,6,7,8,9]
// in null
// cur 9
// next add 9
// stack[]

// add kanan jika kiri ada dan in dan stack.last !==


const root4 = new TreeNode(25,
   new TreeNode(15,
      new TreeNode(10,
         new TreeNode(4),
      ),
      new TreeNode(22,
         new TreeNode(24)
      ),
   ),
   new TreeNode(50,
      new TreeNode(35,
         new TreeNode(31),
      ),
      new TreeNode(70,
         new TreeNode(66),
      ),
   ),
);
/*
                      25
           15                 50
     10         22        35      70
   4          24       31       66
*/
/*
add kanan ketka (stack.left && in === stack.last)
         preorder [25,15,10,4,22,24,50,35,31,70,66] inorder [4,10,15,24,22,25,31,35,50,66,70]
         in null
         cur 70
         next add null
         stack []
*/
const root5 = new TreeNode(25,
   new TreeNode(15,
      new TreeNode(10,
         new TreeNode(4),
      ),
      new TreeNode(22,
         null,
         new TreeNode(24)
      ),
   ),
   new TreeNode(50,
      new TreeNode(35,
         new TreeNode(31),
      ),
      new TreeNode(70,
         null,
         new TreeNode(66),
      ),
   ),
);
/*
                   25
           15                 50
     10         22        35      70
   4               24   31           66
   preorder [25,15,10,4,22,24,50,35,31,70,66] inorder [4,10,15,22,24,25,31,35,50,70,66]
   in null
   cur 66
   add null
   stack []
      
   add kanan jika up
*/
const root6 = new TreeNode(25,
   new TreeNode(15,
      new TreeNode(10,
         new TreeNode(4),
         new TreeNode(7),
      ),
      new TreeNode(22,
         new TreeNode(18),
         new TreeNode(24)
      ),
   ),
   new TreeNode(50,
      new TreeNode(35,
         new TreeNode(31),
         new TreeNode(40),
      ),
      new TreeNode(70,
         new TreeNode(55),
         new TreeNode(66),
      ),
   ),
);
/*
                   25
           15                 50
     10         22        35        70
   4    7     18   24   31   40   55   66
   preorder [25,15,10,4,7,22,18,24,50,35,31,40,70,55,66] inorder [4,10,7,15,18,22,24,25,31,35,40,50,55,70,66]
   in null
   cur 66
   add null
   stack []
      kiri
   add kanan jika up
   after add jadi down
*/
const root7 = new TreeNode(1,
   null,
   new TreeNode(2),
);
/*
   1
     2
   preorder = [1,2]; inorder = [1,2];
   in 2
   cur 1
   add 2
   stack [2]
*/
const root8 = new TreeNode(1,
   new TreeNode(2),
   null,
);
/*
      1
   2
   preorder = [1,2]; inorder = [2,1];
   in 2
   cur 1
   add 2
   stack [1,2]
*/
function preorder(node) {
   if (node === null) return;
   console.log(node.val);
   preorder(node.left);
   preorder(node.right);
}
console.log('preorder', preorder(root8));
function inorder(node) {
   if (node === null) return;
   inorder(node.left);
   console.log(node.val);
   inorder(node.right);
}
console.log('inorder', inorder(root8));