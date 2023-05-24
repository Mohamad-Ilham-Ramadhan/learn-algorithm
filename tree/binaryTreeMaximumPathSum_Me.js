/*
   LeetCode: Binary tree maximum path sum (Hard)

   A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

   The path sum of a path is the sum of the node's values in the path.

   Given the root of a binary tree, return the maximum path sum of any non-empty path.

   

   Example 1:
           1
         2   3

      Input: root = [1,2,3]
      Output: 6
      Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

   Example 2:
     -10
   9     20
      15    7

      Input: root = [-10,9,20,null,null,15,7]
      Output: 42
      Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
   

   Constraints:
      - The number of nodes in the tree is in the range [1, 3 * 104].
      - -1000 <= Node.val <= 1000

   Solution By myself:

   LeetCode submission:
      #1
      - runtime: 83 ms, beats 45.94%
      - memory: 50.7 MB, beats 98.73%
      #2
      - runtime: 81 ms, beats 56.73%
      - memory: 50.7 MB, beats 89.47%
*/
class TreeNode {
   constructor(val, left, right) {
      this.val = (val === undefined ? 0 : val)
      this.left = (left === undefined ? null : left)
      this.right = (right === undefined ? null : right)
   }
}

function maxPathSum(root) {
   let max = -Infinity;

   function find(node) {
      if (node === null) return -Infinity;
      /*
         50 [
         66 + 50 -4 = 112 -> max;
         66 -> max;
         -4 -> max;
         66 + 50 = [116] -> return;
         50 - 4 = 46 -> return;
         50 -> return;
        ] */
        const left = find(node.left);
        const right = find(node.right);
        const maxResult = Math.max( (left + node.val), (node.val + right), node.val );
        console.log('left', left, 'right', right);
        const maxMax = Math.max((left + node.val + right), left, right);
        console.log(node.val, 'maxMax', maxMax, 'maxResult', maxResult);
        max = Math.max( maxResult,  maxMax, max);
        console.log('max then', max);
      
      return maxResult;
   }

   let result = find(root);

   console.log('max', max, 'result', result);
   return Math.max(result, max);

}
const root1 = new TreeNode(-10,
   new TreeNode(9),
   new TreeNode(20,
      new TreeNode(15),
      new TreeNode(7),
   ),
);
const root2 = new TreeNode(25,
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

   24 + 22 + 15 + 25 + 50 + 70 + 66
*/
const root3 =   new TreeNode(15,
   new TreeNode(10,
      new TreeNode(-14),
      new TreeNode(7),
   ),
   new TreeNode(22,
      new TreeNode(18),
      new TreeNode(-20)
   ),
);
/*
           15
       10          22
   -14    7     18   -20
   
   result: 72 -> 7 + 10 + 15 + 22 + 18
      -14 -> [-14, -14]
      7 -> [7, 7]
   10 -> [3, 17]
      18 -> [18, 18]
      -20 -> [-20, -20]
   22 -> [20, 40]

   15 -> [57, 37]
   
        -10
      9     20
         15    7

         15 -> [15, 15]
         7 -> [7, 7]
      20 -> [42, 35]
      9 -> [9, 9] 
      -10 -> [
         -10 + 42 + 9 = 41
         -10 + 42 =  
         -10 + 9 =
         42
         9 
      ]

                   25
           15                 50
     -10          22        35         -70
  -4    -7    -18    24   31   -40   -55   66
   
  -4 -> [
   -4 + 0 + 0 = -4 -> max;
   -4 + 0 = -4 -> return;
   -4 + 0 = -4 -> return;
   0 -> max
   0 -> max
   -4 -> return;
  ]

  -10 -> [
      -4 + -10 + -7 = -21 -> max;
      -4 -> max;
      -7 -> max;
      -4 + -10 = -14 -> return;
      -7 + -10 = -17 -> return;
      [-10] -> return;
  ]
  22 -> [
   -18 + 22 + 24 = 28 -> max;
   -18 -> max;
   24 -> max;
   -18 + 22 = 4 -> return;
   24 + 22 = [46] -> return;
   22 -> return;
  ]
  15 -> [
   -10 + 15 + 46 = 51 -> max;
   -10 -> max;
   46 -> max;
   -10 + 15 = 5 -> return;
   15 + 46 = [61] -> return;
   15 -> return;
  ]

     25
  61    ... 


  35 -> [
   31 + 35 + -40 = 26 -> max;
   31 -> max;
   -40 -> max;
   31 + 35 = [66] -> return;
   35 + -40 = -5 -> return;
   35 -> return;
  ]
  -70 -> [
   -55 -70 + 66 = -59 -> max;
   -55 -> max;
   66 -> max;
   -55 -70 = -125 -> return;
   -70+66 = [-4] -> return;
   -70 -> return;
  ]

    50 
  66  -4

  50 [
   66 + 50 -4 = 112 -> max;
   66 -> max;
   -4 -> max;
   66 + 50 = [116] -> return;
   50 - 4 = 46 -> return;
   50 -> return;
  ]
  
     25
  61    116

  25 -> [
   61 + 25 + 116 = 202 -> result;
   61 + 25 = 86 -> result
   25 + 116 = 141  -> result
  ]
*/ 
const root4 = new TreeNode(-25,
   new TreeNode(-15,
      new TreeNode(-10,
         new TreeNode(-4),
         new TreeNode(-7),
      ),
      new TreeNode(22,
         new TreeNode(-18),
         new TreeNode(-24)
      ),
   ),
   new TreeNode(-50,
      new TreeNode(-35,
         new TreeNode(-31),
         new TreeNode(-40),
      ),
      new TreeNode(-70,
         new TreeNode(-55),
         new TreeNode(-66),
      ),
   ),
);
/*
                   -25
           -15                 -50
     -10         22        -35        -70
   -4    -7     -18   -24   -31   -40   -55   -66

   22 [TRUE]
*/
const root5 = new TreeNode(-25,
   new TreeNode(15,
      new TreeNode(-10,
         new TreeNode(12),
         new TreeNode(-7),
      ),
      new TreeNode(22,
         new TreeNode(-18),
         new TreeNode(-24)
      ),
   ),
   new TreeNode(-50,
      new TreeNode(-35,
         new TreeNode(-31),
         new TreeNode(-40),
      ),
      new TreeNode(-70,
         new TreeNode(-55),
         new TreeNode(-66),
      ),
   ),
);
/*
                   -25
           15                     -50
     -10            22         -35         -70
   12    -7     -18   -24   -31   -40   -55   -66

   12 -10 + 15 + 22 = 39 [TRUE]
*/
const root6 = new TreeNode(-10,
   new TreeNode(9),
   new TreeNode(20,
      new TreeNode(15,
         new TreeNode(-200,
            null,
            new TreeNode(100,
               new TreeNode(-12,
                  new TreeNode(13)
               ),
               new TreeNode(-8),
            )
         )
      ),
      new TreeNode(7),
   ),
);
/*
        -10
      9     20
         15    7
      -200
         100
       -12  -8
      13            
  101 [true]
*/
const root7 = new TreeNode(-3);
console.log('root1', root1);
console.log('RESULT:', maxPathSum(root3));

