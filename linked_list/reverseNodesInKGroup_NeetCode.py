'''
   (linked list) leetcode: 25. Reverse Nodes in k-Group (hard). Companies (Microsoft)

   Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

   `k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

   You may not alter the values in the list's nodes, only nodes themselves may be changed.

   

   Example 1:
      1->2->3->4->5
      2->1->4->3->5

      Input: head = [1,2,3,4,5], k = 2
      Output: [2,1,4,3,5]

   Example 2:
      1->2->3->4->5
      3->2->1->4->5

      Input: head = [1,2,3,4,5], k = 3
      Output: [3,2,1,4,5]
   

   Constraints:
      - The number of nodes in the list is n.
      - 1 <= k <= n <= 5000
      - 0 <= Node.val <= 1000

   Follow-up: Can you solve the problem in O(1) extra memory space?

   Related Topics:
      (Linked list) (Recursion)

   ======================================================================

   Solution by NeetCode

   leetcode submission:
      runtime: 68 ms, beats 39.92%
      memory: 17.3 MB, beats 94.93%

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getKth(curr, k): 
   while curr and k > 0: 
      curr = curr.next
      k -= 1 
   return curr

def reverseKGroup(head, k):
   dummy = ListNode(0, head)
   groupPrev = dummy

   while True: 
      kth = getKth(groupPrev, k)
      if not kth: 
         break 
      groupNext = kth.next 

      # reverse group
      prev, curr = kth.next, groupPrev.next 

      while curr != groupNext: 
         tmp = curr.next 
         curr.next = prev
         prev = curr 
         curr = tmp
      
      tmp = groupPrev.next 
      groupPrev.next = kth 
      groupPrev = tmp
   
   return dummy.next

h1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))); k1 = 2
k2 = 3

print('RESULT :', reverseKGroup(h1, k1))