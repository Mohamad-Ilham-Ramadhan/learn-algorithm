'''
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
      runtime: 52 ms, beats 83.10%
      memory: 16.41 MB, beats 13.78%
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def deleteDuplicates(head): 
   curr = head 
   while curr: 
      if curr.next and curr.next.val == curr.val:
         curr.next = curr.next.next
         continue

      curr = curr.next
   
   # debbug result 
   curr = head
   while curr: 
      print('curr', curr.val)
      curr = curr.next
      
   return head
   

# 1->1->2->2->3->3
# 1->2->3

# Input: head = [1,1,2,3,3]
# Output: [1,2,3] 
h1 = ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(3))))))
h2 = ListNode(1, ListNode(2))
h3 = None
h4 = ListNode(1, ListNode(1, ListNode(1)))
deleteDuplicates(h4)