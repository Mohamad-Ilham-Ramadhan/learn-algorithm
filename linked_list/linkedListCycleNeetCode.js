/*
   LeetCode problem: Linked List Cycle (easy)

   Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

   There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. Note that `pos` is not passed as a parameter.

   Return `true` if there is a cycle in the linked list. Otherwise, return `false`.


   Example 1:
      3->2->0->-4 ---
         ^          |
         |-----------
      Input: head = [3,2,0,-4], pos = 1
      Output: true
      Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

   Example 2:
      1->2---
      ^     |
      |------
      Input: head = [1,2], pos = 0
      Output: true
      Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
   Example 3:
      1

      Input: head = [1], pos = -1
      Output: false
      Explanation: There is no cycle in the linked list.
   

   Constraints:
      - The number of the nodes in the list is in the range [0, 104].
      - -105 <= Node.val <= 105
      - pos is -1 or a valid index in the linked-list.

   Solution by NeetCode:
      To meet O(1) in space complexity, we need to use Floyd's tortoise and hare algorithms

      Floyd's tortoise and hare algorithms is used to detect a cycle.

   LeetCode submission:
      Runtime: 58 ms, beats: 97.96%
      Memory: 45.5 MB, beats: 22.77%
   

   Follow up: Can you solve it using O(1) (i.e. constant) memory? (I DON'T UNDERSTAND THIS)
*/

class ListNode {
   constructor(val) {
      this.val = val;
      this.next = null;
   }
}
// O(1) memory here
function linkedListCycle(head) {
   let tortoise = head; let hare = head;
   
   while (hare && hare.next) {
      tortoise = tortoise.next;
      hare = hare.next.next;
      if (tortoise === hare) return true;
   }
   return false;
}
let node2;
let node3;
let node4;
node2 = new ListNode(2);
node3 = new ListNode(0);
node2.next = node3;
node4 = new ListNode(-4);
node3.next = node4;
node4.next = node2;
const head1 = new ListNode(3);
head1.next = node2;
/*
   3->2->0->-4 ---
      ^          |
      |-----------

   output: true

*/

console.log('RESULT :', linkedListCycle(head1))