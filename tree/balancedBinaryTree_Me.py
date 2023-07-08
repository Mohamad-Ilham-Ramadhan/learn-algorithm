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

   Solution by myself: 
      depth first search

   Leetcode submissison: 
      runtime: 75 ms, beats 25.64%
      memory: 21.1 MB, beats 79.42%
'''
# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def isBalanced(root): 
   if root == None: return True

   # return count of nodes. r = node, c = count
   def recursion(r):
      if r == None: return 0

      left, right = recursion(r.left), recursion(r.right)
      print('recursion', r.val, 'left count', left, 'right count', right)
      if isinstance(left, bool) or isinstance(right, bool) or abs(left - right) > 1: 
         return False 
      
      return max(left, right) + 1

   left = recursion(root.left)
   right = recursion(root.right) 
   print('FInal left count', left, 'right count', right)
   if isinstance(left, bool) or isinstance(right, bool) or abs(left - right) > 1: 
         return False 
   return True

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

print('RESULT : ', isBalanced(r3))