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

   Solution:
      using queue to store l1, l2, l3 ... 
      using stack to store ln-1, ln-2, ln-3 ...
      count the length of the list
      set mid point where Ceil.((count - 2) / 2)
      collect l1, l2, l3 ... when <= mid 
      collect ln-1, ln-2, ln-3 ... when > mid 
      reorder list;
      set tail.next = null
   
   LeetCode submission: 
      Runtime: 367 ms, beats 5.16%
      Memory: 50.5 MB, beats 27.10%

*/
class ListNode {
   constructor(val, next) {
      this.val = (val === undefined ? 0 : val)
      this.next = (next === undefined ? null : next)
   }
}
// O(n * 3)
function reorderList(head) {
   let queue = []; // for l1, l2, l3
   let stack = []; // for ln-1, ln-2, ln-3

   let next = head;
   let count = 0; // count of length of list
   let tail;
   while (next) {
      console.log('counting list length')
      if (next.next === null) {
         tail = Object.assign(next);
      }
      next = next.next;
      count++;
   }
   const mid = Math.ceil((count - 2) / 2);
   console.log(tail, count, mid);

   // collecting l1,l2,l3... and ln-1, ln-2, ln-3...
   next = head.next;
   for (let i = 1; i <= count - 2; i++) {
      console.log('collecting');
      if (i <= mid) {
         queue.push(next);
      } else {
         stack.push(next);
      }
      next = next.next;
   }

   // reordering list
   head.next = tail;
   next = tail;
   console.log('head', head)
   let x = 0; // x === 0 means queue else if x === 1 means stack
   while (queue.length || stack.length) {
      console.log('reordering')

      if (x === 0) {
         next.next = queue.shift();
         x = 1;
      } else {
         next.next = stack.pop();
         x = 0;
      }
      next = next.next;
   }
   next.next = null;
   return head;
}
const head1 = new ListNode(1,
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
); // 1->4->2->3
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
console.log(reorderList(head3));