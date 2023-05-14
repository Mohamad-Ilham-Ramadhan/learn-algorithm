/*
   LeetCode problem: Merge Two Sorted Lists (easy)

   You are given the heads of two sorted linked lists list1 and list2.

   Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

   Return the head of the merged linked list.

   

   Example 1:
      Input: list1 = [1,2,4], list2 = [1,3,4]
      Output: [1,1,2,3,4,4]
   Example 2:
      Input: list1 = [], list2 = []
      Output: []
   Example 3:
      Input: list1 = [], list2 = [0]
      Output: [0]
   

   Constraints:
      - The number of nodes in both lists is in the range [0, 50].
      - -100 <= Node.val <= 100
      - Both list1 and list2 are sorted in non-decreasing order.

   LeetCode submission:
      Runtime: 66 ms, beats 65.36%
      Memory: 43.7 MB, beats 90%
*/

class ListNode {
   constructor(val, next) {
      this.val = (val === undefined ? 0 : val)
      this.next = (next === undefined ? null : next)
   }
}

/*
    4
    5->6->7
    
    1->2

    1->2->4
    1->3->4
    1
*/

function mergeTwoSortedList(list1, list2) {
   // return;
   if (list1 === null && list2 === null) return null;
   let newList = {};
   let next; // for reference of newList tail's 

   // initial
   if (list2 === null) {
      newList = list1;
      next = newList;
      list1 = list1.next;
   } else if (list1 === null) {
      newList = list2;
      next = newList;
      list2 = list2.next;
   } else if (list1.val <= list2.val) { 
      newList = list1;
      next = newList;
      list1 = list1.next;
   } else if (list2.val <= list1.val) {
      newList = list2;
      next = newList;
      list2 = list2.next;
   }


   while (list1 || list2) {
      if (list2 === null ) {
         next.next = list1;
         list1 = list1.next;
      } else if (list1 === null) {
         next.next = list2;
         list2 = list2.next;
      } else if (list1.val <= list2.val) { 
         next.next = list1;
         list1 = list1.next;
      } else if (list2.val <= list1.val) {
         next.next = list2;
         list2 = list2.next;
      }
      next = next.next;
   }

   return newList;
}
let list1 = new ListNode(1,
   new ListNode(2, 
      new ListNode(4)
   )
)
let list2 = new ListNode(1,
   new ListNode(3, 
      new ListNode(4)
   )
)

let list12 = new ListNode(1);
let list22 = null
let list13 = new ListNode(2);
let list23 = new ListNode(1);
console.log(mergeTwoSortedList(list13, list23))