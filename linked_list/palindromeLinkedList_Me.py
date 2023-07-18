'''
   (linked list) leetcode: 234. Palindrome Linked List (easy)

   Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

 

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

   =======================================================================
   Solution by myself:

   Leetcode submission:
      #1 time O(n), space O(n)
      runtime: 927 ms, beats 10.54%
      memory: 49.52 MB,  beats 9.31%

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# 1
def isPalindrome(head): 
   nums = []
   cur = head 
   while cur: 
      nums.append(cur.val)
      cur = cur.next
   
   l = r = mid = 0
   if len(nums) % 2: # odd 
      l = r = len(nums) // 2
   else: # even
      r = len(nums) // 2
      l = r - 1

   while l > -1 and r < len(nums): 
      if nums[l] != nums[r]: return False 
      l -= 1
      r += 1
   return True