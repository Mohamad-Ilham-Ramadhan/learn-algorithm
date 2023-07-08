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

   ======================================================================

   Solution by myself

   leetcode submission:
      runtime: 69 ms, beats 34.90%
      memory: 17.6 MB< beats 63.19%

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# time: O(n), space: O(1)
def reverseKGroup(head, k):
   root = ListNode()
   root.next = head 
   prev, cur = root, head
   next = None
   count = 0
   while cur: 
      count += 1
      # print('count', count, 'cur', cur.val)
      # reverse the next chain
      if count == k: 
         # print('REVERSE')
         next = cur.next # 3
         revNext = prev.next # 1
         revPrev = prev.next # 1 (for the next prev)
         revCur = revNext.next # 2
         revNext.next = next # 1->3
         # print('next', next.val, 'revNext.val', revNext.val, 'revCur', revCur.val, 'temp', revCur.next.val)
         while revCur and revCur != next: 
            # 1->2->3->4->5
            # 2->1->4->3->5

            temp = revCur.next  # 3
            revCur.next = revNext # 2->1
            # print('revcur before', revCur.val, revCur.next.val, revCur.next.next.val)
            revNext = revCur
            revCur = temp
            # print('INSIDE REVERSE WHILE', 'temp', temp.val, 'revCur', revCur.val, 'revNext', revNext.val, 'revCur.next', revCur.next.val if revCur.next else None)

         prev.next = revNext
         prev = revPrev
         count = 0
         cur = revCur
         # print('check reverse root ====') 
         # curX = root
         # while curX: 
         # print('curX.val', curX.val)
         #    curX = curX.next 
         # print('check reverse head ====') 
         # curX = head
         # while curX: 
         # print('curX.val', curX.val)
         #    curX = curX.next 
         continue


      # print('cur', cur.val, 'cur.next', cur.next.val)
      

      cur = cur.next
      # print('===========================================')
      
   # print('check result') 
   # cur = head
   # while cur: 
   #    print('cur.val', cur.val)
   #    cur = cur.next 
   
   return root.next

h1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))); k1 = 2
k2 = 3

print('RESULT :', reverseKGroup(h1, k1))