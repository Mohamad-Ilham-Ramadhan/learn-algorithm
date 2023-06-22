"""
   (Tree) LeetCode: 572. Subtree of Another Tree (easy)

   Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

   A subtree of a binary tree `tree` is a `tree` that consists of a node in tree and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

   Example 1:
         root           subRoot
            3              4
        4      5         1   2
      1   2             
      Input: root = [3,4,5,1,2], subRoot = [4,1,2]
      Output: true

   Example 2:
            3             4
        4      5        1   2
      1   2
         0
      Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
      Output: false
   

   Constraints:
      - The number of nodes in the root tree is in the range [1, 2000].
      - The number of nodes in the subRoot tree is in the range [1, 1000].
      - -104 <= root.val <= 104
      - -104 <= subRoot.val <= 104
   
   Solution by NeetCode
         
   LeetCode submission
      runtime: 127 ms, beats 80.1%
      memory: 17.6 MB, beats 23.25%
"""


# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

class Solution:
   def isSubtree(self, root, subRoot):
      if not subRoot: return True 
      if not root: return False 

      if self.sameTree(root, subRoot):
         return True

      return (self.isSubtree(root.left, subRoot) or 
              self.isSubtree(root.right, subRoot))

   def sameTree(self, s, t):
      if not s and not t:
         return True 
      if s and t and s.val == t.val:
         return (self.sameTree(s.left, t.left)) and (self.sameTree(s.right, t.right))
      return False

r1 =  TreeNode(3,
         TreeNode(4,
            TreeNode(1),
            TreeNode(2),
         ),
         TreeNode(5)
      )
sr1 = TreeNode(4,
         TreeNode(1),
         TreeNode(2),
      ) # True

r2 =  TreeNode(3,
         TreeNode(4,
            TreeNode(1),
            TreeNode(2,
               TreeNode(0),
               None
            ),
         ),
         TreeNode(5)
      )
sr2 = TreeNode(4,
         TreeNode(1),
         TreeNode(2),
      ) # False
'''
  root            subRoot
   1                1
     1            2   3
       1
      2  3
'''
r3 =  TreeNode(1, None, 
         TreeNode(1, None, 
            TreeNode(1,
               TreeNode(2),
               TreeNode(3),
            )
         )
      )
sr3 =       TreeNode(1,
               TreeNode(2),
               TreeNode(3),
            ) # True
sol = Solution()
print('RESULT :', sol.isSubtree(r3, sr3))