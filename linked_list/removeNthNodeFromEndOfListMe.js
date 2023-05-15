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
      - The number of nodes in the list is `sz`.
      - 1 <= sz <= 30
      - 0 <= Node.val <= 100
      - 1 <= n <= sz

   LeetCode submission:
      Runtime: 65 ms, beats 41.31%;
      Memory: 43.7 MB, beats 17.96%
   

*/

class ListNode {
   constructor(val, next) {
      this.val = (val === undefined ? 0 : val);
      this.next = (next === undefined ? null : next);
   }
}

// time complexity O(sz * n)

function removeNthFromEnd(head, n) {
   let current = head;
   while (current) {

      let next = current;
      for (let i = 0; i <= n; i++) {
         next = next.next;
         if (next === null) {
            if (current.next === null) return null;
            if (i === n) {
               current.next = current.next.next;
               return head;
            } else {
               head = head.next;
               return head;
            }
         }
      }
      current = current.next;
   }
   return head;
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
console.log(removeNthFromEnd(head4, n4));
// [1,2,3]
