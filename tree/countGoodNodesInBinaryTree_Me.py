'''
   (tree) leetcode: 1448. Count Good Nodes in Binary Tree (medium). Companies (Microsoft)

   Given a binary tree `root`, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

   Return the number of good nodes in the binary tree.

   

   Example 1:

               3
         1           4
      3           1     5

      Input: root = [3,1,4,3,null,1,5]
      Output: 4
      Explanation: Nodes in blue are good.
      Root Node (3) is always a good node.
      Node 4 -> (3,4) is the maximum value in the path starting from the root.
      Node 5 -> (3,4,5) is the maximum value in the path
      Node 3 -> (3,1,3) is the maximum value in the path.

   Example 2:

            3
          3
      4        2
      
      Input: root = [3,3,null,4,2]
      Output: 3
      Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

   Example 3:

      Input: root = [1]
      Output: 1
      Explanation: Root is considered as good.
   

   Constraints:
      - The number of nodes in the binary tree is in the range [1, 10^5].
      - Each node's value is between [-10^4, 10^4].

   Related Topics:
      (Tree) (Depth-first search) (breadth-first search) (binary tree)

   ===========================================================================================

   Solution by myself:
      Depth first search 

   Leetcode submission: 
      runtime: 248 ms, beats 79.39%
      memory: 35.1 MB, beats 33.87%
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def goodNodes(root: TreeNode):
   c = 0
   def dfs(node, limit): 
      if not node: return 
      # my first intuition is using max(limit, node.val) instead of using else but it seems using max() will be slower so I choose more code but faster than concise code but slower
      if node.val >= limit:  
         nonlocal c 
         c += 1
         dfs(node.left, node.val)
         dfs(node.right, node.val)
      else: 
         dfs(node.left, limit)
         dfs(node.right, limit)
   dfs(root, float('-inf'))
   return c
'''
            3
      1           4
   3           1     5

   Input: root = [3,1,4,3,null,1,5]
   Output: 4
'''
r1 =  TreeNode(3,
         TreeNode(1, TreeNode(3)),
         TreeNode(4,
            TreeNode(1),
            TreeNode(5),
         ),
      ) # 4

print('RESULT :', goodNodes(r1))