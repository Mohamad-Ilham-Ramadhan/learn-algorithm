/*
   LeetCode problem: Remove Nth Node From End of List (medium)

   Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

   Example 1:
      1->2->3->4->5
            |
            v
      1->2->3---->5

      Input: head = [1,2,3,4,5], n = 2
      Output: [1,2,3,5]
   Example 2:
      Input: head = [1], n = 1
      Output: []

   Example 3:
      Input: head = [1,2], n = 1
      Output: [1]

   Constraints:
      - The number of nodes in the list is sz.
      - 1 <= sz <= 30
      - 0 <= Node.val <= 100
      - 1 <= n <= sz

   Solution by NeetCode in O(n) while mine is O(sz * n): https://www.youtube.com/watch?v=XVuQxVej6y8
      - using dummy node : dummyNode->head 
      - and two pointer: l and r when r reach end (null) then l is in the deleted node 
      - because we need prev node to connect to the next node of the deleted node, so we use a dummy node here, so when r reach null the l is in prev node of deleted node

   LeetCode submission:
      #1
      Runtime: 78 ms, beats 5.43%;
      Memory: 43 MB, beats 69.61%
      #2
      Runtime: 50 ms, beats 97.6%
      Memory: 43.2 MB, beats 59.92%

*/

class ListNode {
   constructor(val, next) {
      this.val = (val === undefined ? 0 : val);
      this.next = (next === undefined ? null : next);
   }
}
// O(n) + O(sz)
function removeNthFromEnd(head, n) {
   let dummy = new ListNode(0, head);
   let left = dummy;
   let right = head;

   while (n > 0 && right) {
      right = right.next;
      n--;
   }

   while (right) {
      left = left.next;
      right = right.next;
   }

   // delete 
   left.next = left.next.next;
   return dummy.next;
}
const head1 = new ListNode(1,
   new ListNode(2, 
      new ListNode(3,
         new ListNode(4,
            new ListNode(5)
         )
      )
   )
);
const n1 = 2; // expect: 1->2->3->5
const head2 = new ListNode(1);
const n2 = 1; // expect: null
const head3 = new ListNode(1,
   new ListNode(2)
);
const n3 = 1; // expect: 1
const head4 = new ListNode(1,
   new ListNode(2)
); // [1,2]
const n4 = 2; // expect: 2
console.log(removeNthFromEnd(head1, n1));
// [1,2,3]
