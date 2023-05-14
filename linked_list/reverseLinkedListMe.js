/*
   LeetCode problem: Reverse Linked List (easy)

   Given the `head` of a singly linked list, reverse the list, and return the reversed list.

 
   Example 1:
      Input: head = [1,2,3,4,5]
      Output: [5,4,3,2,1]
   Example 2:
      Input: head = [1,2]
      Output: [2,1]
   Example 3:
      Input: head = []
      Output: []

   Constraints:
      - The number of nodes in the list is the range [0, 5000].
      - -5000 <= Node.val <= 5000


   Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

   LeetCode submission:
      # iteratively
      Runtime: 74 ms, 9.56%
      Memory: 44.7 MB, 26.10%
      
      # recursively
      Runtime: 67 ms, 39.33%
      Memory: 45 MB, 7.36%
*/

class ListNode {
   constructor(val, next) {
      this.val = (val === undefined ? 0 : val);
      this.next = (next === undefined ? null : next);
   }
}

// Iteratively
function reverseLinkedList(head) {
   let newHead = null;
   while (head !== null) {
      let current = Object.assign({}, head)
      current.next = newHead;
      newHead = current;
      if (head.next === null) {
         head = null;
      } else {
         head = head.next;
      }
   }
   return newHead;
}
function recursively(head) {
   if (head === null) return null;
   let newHead = null;
   function _recurs(list) {
      if (list === null) return;
      let current = Object.assign({}, list);
      current.next = newHead;
      newHead = current;
      if (list.next === null) {
         list = null;
      } else {
         _recurs(list.next);
      }
   }
   _recurs(head);
   return newHead;
}
const head1 = new ListNode(1, 
   new ListNode(2, 
      new ListNode(3, 
         new ListNode(4, 
            new ListNode(5)   
         )   
      )
   )
); // 5->4->3->2->1
const head2 = new ListNode(1,
   new ListNode(2)
);
const head3 = null;
console.log('RESULT', recursively(head1));