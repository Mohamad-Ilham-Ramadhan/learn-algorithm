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

   Solution by NeetCode:
      
      Total time complexity is O(n log k);

   LeetCode:
      Runtime: 81 ms, beats 92.3%
      Memory: 47.8 MB, beats 48.42%
*/
class ListNode {
   constructor(val, next) {
      this.val = (val === undefined ? 0 : val)
      this.next = (next === undefined ? null : next)
   }
}
function mergeList(l1, l2) {
   let dummy = new ListNode();
   let tail = dummy;

   while (l1 && l2) {
      if (l1.val < l2.val) {
         tail.next = l1;
         l1 = l1.next;
      } else {
         tail.next = l2;
         l2 = l2.next;
      }
      tail = tail.next
   }
   if (l1) {
      tail.next = l1;
   } 
   if (l2) {
      tail.next = l2;
   }
   return dummy.next;
}
/*
   mergedList = [1->1, 2->6]
*/
function mergeKsort(lists) {
   if (!lists || lists.length === 0 ) return null;
   // console.log('lists before', lists);
   while (lists.length > 1) {
      let mergedLists = [];

      for (let i = 0; i < lists.length; i = i + 2) {
         let l1 = lists[i];
         let l2 = (i + 1) < lists.length ? lists[i + 1] : null;
         // kenapa tiap list langsung di merge karena tiap list udah sorted, merge sort bekarja dari bawah atau unit terkecil di sort hingga naik ke atas, lalu pada bagian paling atar merge bagian pertama yang sorted dan bagian kedua yang udah sorted:
         // [1,3,7,4,2,5,6,8]
         // setelah kembali dari bawah (recursion) merge([1,3,4,7], [2,5,6,8])

         // l1, l2, l3, ... udah sorted tinggal di merge
         mergedLists.push(mergeList(l1, l2));
      }
      lists = mergedLists;
   }
   // console.log('new lists: ', lists);
   return lists[0];
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

