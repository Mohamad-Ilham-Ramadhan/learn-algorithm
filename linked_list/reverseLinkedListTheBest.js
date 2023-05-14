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

   Solution: the best submitted solution in LeetCode

   LeetCode submission:
      Runtime: 58 ms, beats 84.59%
      Memory: 44.7 MB, beats 26.10%
*/

class ListNode {
   constructor(val, next) {
      this.val = (val === undefined ? 0 : val);
      this.next = (next === undefined ? null : next);
   }
}

// Iteratively
function reverseLinkedList(head) {
   // this is other's submitten solution (the best) 
   // I only use this for checking how much it beats percentage
   let prev = null;
   let next = head;
 
   while(next){
       let temp = next.next; // copying object's properties is copy by value not refrence
       next.next = prev; // so this will not change `temp` to `null`
       prev = next;
       next = temp;
   }
 
   return prev;
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