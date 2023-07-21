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
      #2 (iterative)
         runtime: 51 ms, beats 29.59%
         memory: 16.17 MB, beats 96.60%
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

# iteratively 
def iterative(root): 
   result = []
   visited = set()
   stack = [root] 

   while len(stack): 
      print('current val', stack[-1].val,  stack[-1].left.val if stack[-1].left else None)
      if stack[-1] in visited: 
         print('in stack', stack[-1].val)
         right = stack[-1].right
         result.append(stack.pop().val)
         if right and right not in visited:
            stack.append(right)
         continue
      visited.add(stack[-1])
      if stack[-1].left and stack[-1].left not in visited: 
         stack.append(stack[-1].left)
         continue
      
   
   return result

r1 = TreeNode(1, 
         TreeNode(2,
            TreeNode(4),
            TreeNode(5)
         ),
         TreeNode(3,
            TreeNode(6),
            TreeNode(7)
         )
      )
r2 =  TreeNode(37,
         TreeNode(-34,None,TreeNode(-100)),
         TreeNode(-48,
            TreeNode(-100),
            TreeNode(48,
               TreeNode(-54,
                  TreeNode(-71),
                  TreeNode(-22, None, TreeNode(8)),
               )
            )
         )
      ) # [-34,-100,37,-100,-48,-71,-54,-22,8,48]
print('RESULT: ', iterative(r2))
'''
   result = [4]
   [1,2,5]
'''