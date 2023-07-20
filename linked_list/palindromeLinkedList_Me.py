'''
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
         runtime: 927 ms, beats 10.54%
         memory: beats 9.31%
      #2 time O(n), space O(1)
         runtime: 801 ms, beats 47.78%
         memory: 41.44 MB, beats 66.97%

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

# 2 time: O(n) and space O(1)
def isPalindrome(head):
    slow = head
    fast = head.next
    while fast: 
        print('slow', slow.val)
        print('fast', fast.val)
        slow = slow.next 
        if not fast.next or not fast.next.next:
            break
        fast = fast.next.next
    partTwo = ListNode(None);
    next = slow 
    while next: 
        temp = next.next
        next.next = partTwo.next 
        partTwo.next = next
        next = temp
    
    print('check palindrome')
    partTwo = partTwo.next
    while partTwo: 
        if head.val !=  partTwo.val: 
            return False 
        
        partTwo = partTwo.next
        head = head.next  
    return True
'''
   1->2->2->3->2->2->1

   1->2->2->3->2->2->1
   1->2->2-> 2->2->1
'''