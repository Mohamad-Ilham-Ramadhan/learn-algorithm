''' 
   (tree) 110. Balanced Binary Tree (easy). Companies (Amazon)

   Given a binary tree, determine if it is height-balanced (A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.).
   

   Example 1:
           3
      9        20
            15    7

      Input: root = [3,9,20,null,null,15,7]
      Output: true

   Example 2:
                 1
              2        2
           3     3
      4      4

      Input: root = [1,2,2,3,3,null,null,4,4]
      Output: false

   Example 3:

      Input: root = []
      Output: true
   

   Constraints:
      - The number of nodes in the tree is in the range [0, 5000].
      - -10^4 <= Node.val <= 10^4

   Related Topics:
      (Tree) (Depth-First Search) (Binary Tree)
   
   ====================================================================

   Solution by NeetCode

   Leetcode submissison: 
      runtime: 64 ms, beats 72.67%
      memory: 21.5 MB, beats 7.81%
'''
# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def isBalanced(root): 
   def dfs(root): 
      if not root: return [True, 0]

      left, right = dfs(root.left), dfs(root.right)
      balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

      return [balanced, 1 + max(left[1], right[1])]
   
   return dfs(root)

print('0 == False', 0 == False, isinstance(0, bool))
'''
            3
      9        20
            15    7
'''
r1 = TreeNode(3,
      TreeNode(9),
      TreeNode(20, 
         TreeNode(15),
         TreeNode(7),
      )
   ) # True
'''
                 1
              2        2
           3     3
      4      4
'''
r2 = TreeNode(1,
      TreeNode(2,
         TreeNode(3,
            TreeNode(4),
            TreeNode(4)
         ),
         TreeNode(3),
      ),
      TreeNode(2)
   ) # False
'''
        1
     2     2
    3       3
   4         4
   [1,2,2,3,null,null,3,4,null,null,4] # expect: False
'''
r3 =  TreeNode(1,
         TreeNode(2,
            TreeNode(3,
               TreeNode(4)
            )
         ),
         TreeNode(2,None, 
            TreeNode(3,None,
               TreeNode(4)
            )
         ),
      )

print('RESULT : ', isBalanced(r2))