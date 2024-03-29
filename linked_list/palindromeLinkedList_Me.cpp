/*
   (linked list) leetcode: 234. Palindrome Linked List (easy)

   Given the head of a singly linked list, return true if it is a palindrome or false otherwise.



   Example 1:
      1->2->2->1

      Input: head = [1,2,2,1]
      Output: true

   Example 2:
      1->2

      Input: head = [1,2]
      Output: false


   Constraints:
      The number of nodes in the list is in the range [1, 10^5].
      0 <= Node.val <= 9

   Follow up: Could you do it in O(n) time and O(1) space?


   Related topics:
      (linked list) (two pointers) (stack) (recursion)

   =======================================================================

   Solution by myself:
      #1
         but firstly, we store all listnode value to an array/list
         using two pointers to check is it a palindrome
      #2
         using two pointers (hare and turtle), the first is slow, the second is fast (it is two step next)
         reverse the part two (mid to end) using slow as the first next value for part two
         then check is it palindrome by using two pointer, the first is point to the head argument, and the second is the part two.next because part two is None initialy.


   Leetcode submission:
      #1 time O(n), space O(n)
         runtime: 274 ms, beats 44.01%
         memory: 128.23, beats 20.35%
      #2 time O(n), space O(1)
         runtime: 217 ms, beats 94.70%
         memory: 114.15 MB, beats 76.12%
*/

// Definition for singly-linked list.
#include <bits/stdc++.h>
using namespace std;

struct ListNode
{
   int val;
   ListNode *next;
   ListNode() : val(0), next(nullptr) {}
   ListNode(int x) : val(x), next(nullptr) {}
   ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
   // #1 time O(n*2), space O(n)
   bool isPalindrome(ListNode *head)
   {
      vector<int> nums;
      ListNode *cur = head;
      while (cur)
      {
         nums.push_back(cur->val);
         cur = cur->next;
      }
      int l;
      int r;
      if (nums.size() % 2)
      { // odd
         l = r = nums.size() / 2;
      }
      else
      { // even
         r = nums.size() / 2;
         l = r - 1;
      }
      while (l > -1 && r < nums.size())
      {
         if (nums[l] != nums[r])
            return false;
         l--;
         r++;
      }
      return true;
   }

   // #2 time O(n * 1.5), space O(1)
   bool solution2(ListNode *head)
   {
      ListNode *slow = head;
      ListNode *fast = head->next;
      while (fast)
      {
         slow = slow->next;
         if (fast->next == NULL || fast->next->next == NULL)
         {
            break;
         }
         fast = fast->next->next;
      }

      // Reverse the part two
      ListNode n(-666);
      ListNode *partTwo = &n;
      ListNode *next = slow;
      while (next)
      {
         ListNode *temp = next->next;
         next->next = partTwo->next;
         partTwo->next = next;
         next = temp;
      }

      ListNode *start = partTwo->next;
      while (start)
      {
         if (head->val != start->val)
         {
            return false;
         }
         start = start->next;
         head = head->next;
      }
      return true;
   }
};

int main()
{
   // 1->2->2->1
   ListNode h1(1);
   ListNode h2(2);
   h1.next = &h2;
   ListNode h3(2);
   h2.next = &h3;
   ListNode h4(1);
   h3.next = &h4;

   Solution s;
   cout << "result :" << s.isPalindrome(&h1);
   int len = 9;
   cout << 9 / 2;
   return 0;
}