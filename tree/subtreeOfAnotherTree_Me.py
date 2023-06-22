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
   
   Solution by Myself:
      - traverse root tree to get all potentials node
      - store the potentials in a stack
      - while stack.length > 0 
         - stack pop()
         - dfs subtree and potential root
            if all node same return True 
            else continue while loop

      - Return False because nothing same
         
   LeetCode submission
      #1 
         runtime: 109 ms, beats 92.3%
         memory: 17.6 MB, beats 50.86
"""


# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

# attempt #1
def isSubtree(root, subRoot):
   stack = [] # to store potential node/root
   def dfs(root):
      if root == None: return 
      if root.val == subRoot.val:
         stack.append(root)
      dfs(root.left)
      dfs(root.right)
   dfs(root)
   print('stack', stack)

   def dfsCheck(root1, root2):
      if (root1 == None or root2 == None):
         if root1 == None and root2 == None:
            return True 
         else: 
            return False
      return (root1.val == root2.val) and dfsCheck(root1.left, root2.left) and dfsCheck(root1.right, root2.right)
   # check every potential roots
   while len(stack) > 0:
      r = stack.pop() 
      if dfsCheck(r, subRoot): return True
   
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
print('RESULT :', isSubtree(r3, sr3))