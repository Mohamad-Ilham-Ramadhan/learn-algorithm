'''
   (linked list) 2. Add Two Numbers (mediums)

   You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

   You may assume the two numbers do not contain any leading zero, except the number 0 itself.

   

   Example 1:

      Input: l1 = [2,4,3], l2 = [5,6,4]
      Output: [7,0,8]
      Explanation: 342 + 465 = 807.

   Example 2:
      Input: l1 = [0], l2 = [0]
      Output: [0]

   Example 3:
      Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
      Output: [8,9,9,9,0,0,0,1]
   

   Constraints:
      - -The number of nodes in each linked list is in the range [1, 100].
      - 0 <= Node.val <= 9
      - It is guaranteed that the list represents a number that does not have leading zeros.

   Related Topics:
      (Linked list) (Math) (Recursion)

   =====================================================================

   Solution by myself 

   Leetcode submission:
      attempt #1
         runtime: 94 ms, beats 6.98%
         memory: 16.2 MB, beats 95.93%
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1
def addTwoNumbers(l1, l2):
   cur1 = l1 
   cur2 = l2 
   num1 = ''
   while cur1: 
      num1 = str(cur1.val) + num1
      cur1 = cur1.next 

   num2 = ''
   while cur2: 
      num2 = str(cur2.val) + num2
      cur2 = cur2.next 
   
   total = str(int(num1) + int(num2))

   res = ListNode(0)
   cur = res
   while len(total): 
      val = total[-1]
      total = total[:len(total)-1]
      cur.next = ListNode(val)
      cur = cur.next
      print('val', val,'total', total)
   
   return res.next
'''
   [9,9,9]
   [9,9,9]
   [8,9,9,1]

      Input: l1 = [2,4,3], l2 = [5,6,4]
      Output: [7,0,8]
      Explanation: 342 + 465 = 807.
'''
l11 = ListNode(2,ListNode(4,ListNode(3)))
l21 = ListNode(5,ListNode(6,ListNode(4)))

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
l12 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))))
l22 = ListNode(9,ListNode(9,ListNode(9,ListNode(9))))

print('RESULT :', addTwoNumbers(l12, l22)) 