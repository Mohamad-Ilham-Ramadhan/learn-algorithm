/*
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
         runtime: 3 ms, beats 44.65%
         memory: 8.34 MB, beats 52.76%
*/

// Definition for singly-linked list.
#include <bits/stdc++.h>
using namespace std;

// Definition for a binary tree node.
struct TreeNode
{
   int val;
   TreeNode *left;
   TreeNode *right;
   TreeNode() : val(0), left(nullptr), right(nullptr) {}
   TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
   TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
private:
   vector<int> result;
   void inorder(TreeNode *node)
   {
      if (node == NULL)
         return;
      inorder(node->left);
      result.push_back(node->val);
      inorder(node->right);
   }

public:
   vector<int> inorderTraversal(TreeNode *root)
   {
      inorder(root);
      return result;
   }
};

int main()
{
   return 0;
}