'''
   (tree) leetcode: 94. Binary Tree Inorder Traversal (easy)

   Given the root of a binary tree, return the inorder traversal of its nodes' values.

 
   Example 1:
      1
         2
        3

      Input: root = [1,null,2,3]
      Output: [1,3,2]

   Example 2:

      Input: root = []
      Output: []

   Example 3:

   Input: root = [1]
   Output: [1]
   

   Constraints:
      - The number of nodes in the tree is in the range [0, 100].
      - -100 <= Node.val <= 100
   

   Follow up: Recursive solution is trivial, could you do it iteratively?

   Related Topics 
      (stack) (tree) (depth-first search) (binary tree)


   ==========================================================================
   Solution by myself 

   Leetcode submission:
      #1 (recursive)
         runtime: 51 ms, beats 29.59%
         memory: 16.48 MB, beats 5.06%
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursively
def inorderTraversal(root): 
   result = [] 
   def inorder(root): 
      if root == None: return
      inorder(root.left)
      result.append(root.val)
      inorder(root.right)
   inorder(root)
   return result