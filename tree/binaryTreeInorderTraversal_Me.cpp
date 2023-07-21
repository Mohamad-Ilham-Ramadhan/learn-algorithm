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
      #2 (iterative)
         runtime: 0 ms, beats 100%
         memory: 8.49 MB, beats 24.72%
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

// #1 recursively
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

// #2 iteratively
class Solution2
{
public:
   vector<int> inorderTraversal(TreeNode *root)
   {
      vector<int> result = {};
      if (root == NULL) return result;

      set<TreeNode*> s;
      vector<TreeNode*> stack;
      stack.push_back(root);
      while (stack.size()) {
         if (s.count(stack.back())) {
            TreeNode* right = stack.back()->right;
            result.push_back(stack.back()->val);
            stack.pop_back();
            if (right != NULL && !s.count(right)) {
               stack.push_back(right);
            }
            continue;
         }

         s.insert(stack.back());

         if (stack.back()->left != NULL && !s.count(stack.back()->left)) {
            stack.push_back(stack.back()->left);
         }
      }

      return result;
   }
};
int main()
{
   set<TreeNode*> s;
   TreeNode r1(1);
   TreeNode r2(2);
   r1.left = &r2;
   TreeNode r3(1);
   s.insert(&r1);
   vector<TreeNode*> stack;
   stack.push_back(&r2);
   stack.push_back(&r3);
   if( s.count(&r3)) {
      cout << "in set \n";
   } else {
      cout << "not in set \n" ;
   }
   cout << stack.back()->val;
   return 0;
}