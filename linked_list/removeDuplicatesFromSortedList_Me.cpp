/*
   (linked list) leetcode: 83. Remove Duplicates from Sorted List (easy)

   Given the `head` of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.



   Example 1:
      1->1->2
      1->2

      Input: head = [1,1,2]
      Output: [1,2]

   Example 2:
      1->1->2->2->3->3
      1->2->3

      Input: head = [1,1,2,3,3]
      Output: [1,2,3]


   Constraints:
      - The number of nodes in the list is in the range [0, 300].
      - -100 <= Node.val <= 100
      - The list is guaranteed to be sorted in ascending order.

   Related topics:
      (linked list)

   =======================================================================================

   Solution by myself

   leetcode submission
      runtime: 8 ms, beats 85.91%
      memory: 11.41 MB, beats 94.67%
*/

#include <iostream>
#include <cmath>
using namespace std;

// Definition for singly-linked list.
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
   ListNode *deleteDuplicates(ListNode *head)
   {
      auto ptr = head;
      while (ptr) {
         if ((*ptr).next && (*ptr).val == (*(*ptr).next).val) {
            (*ptr).next = (*(*ptr).next).next;
            continue;
         }
         ptr = (*ptr).next;
      }
      return head;
   }
};

int main()
{
   ListNode h1; 
   h1.val = 1;
   ListNode h2(1);
   h1.next = &h2;
   ListNode h3(2);
   h2.next = &h3;
   ListNode h4(2);
   h3.next = &h4; 
   ListNode h5(3);
   h4.next = &h5;

   Solution s;
   auto newHead = s.deleteDuplicates(&h1);

   cout << "Check fakta \n";

   auto ptr = newHead;
   while (ptr) {
      ListNode n = *ptr;
      cout << n.val << "\n";
      ptr = n.next;
   }
   return 0;
}