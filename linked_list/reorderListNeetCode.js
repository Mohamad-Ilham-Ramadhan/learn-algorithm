/*
   LeetCode problem: Reorder List (medium)

   You are given the head of a singly linked-list. The list can be represented as:

      L0 → L1 → … → Ln - 1 → Ln

   Reorder the list to be on the following form:

      L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

   You may not modify the values in the list's nodes. Only nodes themselves may be changed.

   Example 1:
      Input: head = [1,2,3,4]
      Output: [1,4,2,3]
   Example 2:
      Input: head = [1,2,3,4,5]
      Output: [1,5,2,4,3]

   Constraints:
      - The number of nodes in the list is in the range [1, 5 * 104].
      - 1 <= Node.val <= 1000

   Solution By NeetCode:
      using two pointers (slow and fast), slow jumps one node at a time and fast jumps two nodes at a time.
      when the fast is null or fast.next is null then stop, the slow pointer already points to the end node of the first part of the list and the next until the fast is the second part of the list.
      Reverse the second part of the list.
      then we can reorder the list 
      1->2->3->4 
      first list: 1->2 
      second list: 3->4 
      reversed second: 4->3
      reorder list 
      1->4->2->3

   
   LeetCode submission: 
      Runtime: 86 ms, beats 81.82%
      Memory: 50 MB, beats 78.32%

*/
class ListNode {
   constructor(val, next) {
      this.val = (val === undefined ? 0 : val)
      this.next = (next === undefined ? null : next)
   }
}
// O(n)
function reorderList(head) {
   // find middle 
   let slow = head; let fast = head.next;
   while (fast && fast.next) {
      slow = slow.next;
      fast = fast.next.next;
   }

   // reverse second half
   let second = slow.next;
   let prev = slow.next = null;
   while (second) {
      let tmp = second.next;
      second.next = prev;
      prev = second;
      second = tmp;
   }

   first = head;
   second = prev;
   // merge two halves;
   while (second) {
      let tmp1 = first.next;
      let tmp2 = second.next;
      first.next = second;
      second.next = tmp1;
      first = tmp1;
      second = tmp2;
   }
   console.log('head', head);
}
let head1 = new ListNode(1,
   new ListNode(2,
      new ListNode(3,
         new ListNode(4)
      )
   )
); // 1->4->2->3
const head2 = new ListNode(1,
   new ListNode(2,
      new ListNode(3,
         new ListNode(4,
            new ListNode(5)
         )
      )
   )
); // 1->5->2->4->3
const head3 = new ListNode(1,
   new ListNode(2,
      new ListNode(3,
         new ListNode(4,
            new ListNode(5,
               new ListNode(6,
                  new ListNode(7)
               )
            )
         )
      )
   )
); // 1->7->2->6->3->5->4
const head4 = new ListNode(1);
const head5 = new ListNode(1,
   new ListNode(2)
);
const head6 = new ListNode(1,
   new ListNode(2,
      new ListNode(3)
   )
);
console.log(reorderList(head2));