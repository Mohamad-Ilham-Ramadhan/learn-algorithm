'''
   (tree) 199. Binary Tree Right Side View (medium). Companies (Facebook)

   Given the `root` of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

   Example 1:
         1
      2        3
         5        4

      Input: root = [1,2,3,null,5,null,4]
      Output: [1,3,4]

   Example 2:
      1
         3

      Input: root = [1,null,3]
      Output: [1,3]

   Example 3:

      Input: root = []
      Output: []
   

   Constraints:
      - The number of nodes in the tree is in the range [0, 100].
      - -100 <= Node.val <= 100

   Related topics:   
      (Tree) (Depth-First Search) (Breadth-First Search) (Binary Tree)
   
   ====================================================================

   Solution by NeetCode:
      Breadth First Search
   
   Leetcode submission:
      runtime: 44 ms, 81.22%
      memory: 16.3MB, 43.16%
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
def rightSideView(root):
   res = [] 
   q = deque([root])

   while q: 
      rightSide = None 
      qLen = len(q)

      for i in range(qLen): 
         node = q.popleft() 
         if node: 
            rightSide = node 
            q.append(node.left)
            q.append(node.right)

      if rightSide:
         res.append(rightSide.val)
   return res
'''
[1,2,3,null,5,null,4,null,null,7]
      1
  2          3
    5           4
            7
   [1,3,4,7]
'''
r1 = TreeNode(1,
         TreeNode(2,None,
            TreeNode(5)
         ),
         TreeNode(3,None,
            TreeNode(4,
               TreeNode(7)
            )
         ),
      ) # [1,3,4,7]
'''
[1,2,3,null,5,null,4,6,null,7,null,8,null,null,null,9]

        1
     2      3
      5      4
     6      7
    8
   9
   [1,3,4,7,8,9]
'''
r2 = TreeNode(1,
         TreeNode(2,None,
            TreeNode(5, TreeNode(6, TreeNode(8, TreeNode(9))))
         ),
         TreeNode(3,None,
            TreeNode(4,
               TreeNode(7)
            )
         ),
      ) # [1,3,4,7,8,9]
print('RESULT :', rightSideView(r1))