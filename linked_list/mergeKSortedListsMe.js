/*
   LeetCode problem: Merge k Sorted Lists (hard)

   You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

   Merge all the linked-lists into one sorted linked-list and return it.


   Example 1:
      Input: lists = [[1,4,5],[1,3,4],[2,6]]
      Output: [1,1,2,3,4,4,5,6]
      Explanation: The linked-lists are:
      [
      1->4->5,
      1->3->4,
      2->6
      ]
      merging them into one sorted list:
      1->1->2->3->4->4->5->6

   Example 2:
      Input: lists = []
      Output: []

   Example 3:
      Input: lists = [[]]
      Output: []

      
   Constraints:
      - k == lists.length
      - 0 <= k <= 104
      - 0 <= lists[i].length <= 500
      - -104 <= lists[i][j] <= 104
      - lists[i] is sorted in ascending order.
      - The sum of lists[i].length will not exceed 104.

   Solution by myself:
      - combine the lists into a single list. Time complexity O(n)
      - then sort the list using merge sort. Time complexity O(n log n)
      - return the sorted list
      
      Total time complexity is O(n) + O(n log n);
      
   LeetCode:
      Runtime: 101 ms, beats 53.4%
      Memory: 48 MB, beats 40.35%
*/
class ListNode {
   constructor(val, next) {
      this.val = (val === undefined ? 0 : val)
      this.next = (next === undefined ? null : next)
   }
}

function mergeSortList(list) {
   if (list.next === null) return list;
   let slow = list; let fast = list.next; // slow and fast pointers

   while (fast && fast.next) {
      slow = slow.next;
      fast = fast.next.next;
   }
   let second = slow.next; // list become the first half and second is the second half
   slow.next = null;
   console.log('first', list, 'second', second);
   return mergeList(mergeSortList(list), mergeSortList(second));
}

function mergeList(left, right) {
   let leftNext = left; // leftNext is left list pointer
   let rightNext = right; // rightNext is right list pointer
   let sortedList = new ListNode('initial');
   let sortedNext = sortedList; // sortedNext is sortedList pointer


   while (leftNext && rightNext) {
      if (leftNext.val < rightNext.val) {
         sortedNext.next = leftNext
         leftNext = leftNext.next;
         sortedNext = sortedNext.next;
      } else {
         sortedNext.next = rightNext
         rightNext = rightNext.next;
         sortedNext = sortedNext.next;
      }
   }
   if (leftNext) {
      sortedNext.next = leftNext;
      sortedNext = sortedNext.next;
   }
   if (rightNext) {
      sortedNext.next = rightNext;
      sortedNext = sortedNext.next;
   }

   return sortedList.next;
}
function mergeKsort(lists) {
   let newList = new ListNode('xxx');
   let newListNext = newList; // newList pointer
   for (let i = 0; i < lists.length; i++) {
      let currentList = lists[i];
      while (currentList) {
         newListNext.next = currentList;
         currentList = currentList.next;
         newListNext = newListNext.next;
      }
   }
   return mergeSortList(newList.next);
}
const l1 = new ListNode(1,
   new ListNode(4,
      new ListNode(5)
   )
);
const l2 = new ListNode(1,
   new ListNode(3,
      new ListNode(4)
   )
);
const l3 = new ListNode(2,
   new ListNode(6)
)
const lists = [l1, l2, l3];

console.log('combined list', mergeKsort(lists));

// console.log('partition', mergeSortList(l));
const left = new ListNode(2,
   new ListNode(5)
)
const right = new ListNode(1,
   new ListNode(4)
)
// console.log('merge list', mergeList(left, right));