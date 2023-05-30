/*
  Leetcode: 1046. Last Stone Weight (easy)

  You are given an array of integers `stones` where `stones[i]` is the weight of the `ith` stone.

  We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:

  If `x == y`, both stones are destroyed, and
  If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.
  At the end of the game, there is at most one stone left.

  Return the weight of the last remaining stone. If there are no stones left, return `0`.

  Example 1:
    Input: stones = [2,7,4,1,8,1]
    Output: 1
    Explanation: 
      We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
      we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
      we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
      we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

  Example 2:
    Input: stones = [1]
    Output: 1
  

  Constraints:
    - 1 <= stones.length <= 30
    - 1 <= stones[i] <= 1000

  Solution by myself: 
   use maxheap to get the first and second greatest number 
      while (heap.size > 1) 
         if x == y then continue 
         else insert the difference to the maxheap
   return the heap[0] or zero if the heap is empty
      Time complexity using max heap is: O(n log n) for first insertion + ( O(log n) * 3 ) for extracting x and y and insert the difference if exists;

   use sort 
      Time complexity: O(n log n) for first sort + O(n) for compare and insert the difference
   

  LeetCode submission:
    #1 (max heap)
    - Runtime: 57 ms, beats 78.21%;
    - Memory: 44.6 MB, beats 9.12%
    #2 (sorted array)
    - Runtime: 68 ms, beats 31.61%
    - Memory: 42 MB, beats 94.65%
*/
class MaxHeap {
   constructor() {
     this.heap = [];
   }
   peek() {
     return this.heap[0];
   }
   insert(val) {
     if (this.heap.length === 0) {
       this.heap.push(val);
       return;
     }
     this.heap.push(val);
     this.heapifyUp();
   }
   heapifyUp() {
     let currentIndex = this.heap.length - 1;
     while ( currentIndex > 0 ) {
       let maxIndex = currentIndex;
       let parentIndex = Math.floor( (currentIndex - 1) / 2);
       if ( parentIndex >= 0 && this.heap[parentIndex] < this.heap[currentIndex] ) {
         maxIndex = parentIndex;
       }
       if (currentIndex === maxIndex) break;
       [ this.heap[currentIndex], this.heap[parentIndex] ] = [ this.heap[parentIndex], this.heap[currentIndex] ];
       currentIndex = maxIndex;
     }
   }
   extractMax() {
     if (this.size() === 0) return null;
     let max = this.heap[0];
     let last = this.heap.pop();
     if (this.size() > 0) {
       this.heap[0] = last;
       this.heapifyDown();
     }
     return max;
   }
   heapifyDown() {
     let currentIndex = 0;
     while (true) {
       let maxIndex = currentIndex;
       let leftIndex = 2 * currentIndex + 1;
       let rightIndex = 2 * currentIndex + 2;
       if (this.heap[maxIndex] < this.heap[leftIndex]) {
         maxIndex = leftIndex;
       }
       if (this.heap[maxIndex] < this.heap[rightIndex]) {
         maxIndex = rightIndex;
       }
       if (maxIndex === currentIndex) {
         break;
       }
       [ this.heap[currentIndex], this.heap[maxIndex] ] = [ this.heap[maxIndex], this.heap[currentIndex] ];
       currentIndex = maxIndex;
     }
   }
   size() {
     return this.heap.length;
   }
 }
 const mh = new MaxHeap();
 mh.insert(2);
 console.log('mh.heap', Object.assign([], mh.heap));
 mh.extractMax();
 console.log('mh.heap', Object.assign([], mh.heap));

 // use max heap
 function lastStoneWeight(stones) {
   const maxHeap = new MaxHeap();
   // O(n log n)
   for (let i = 0; i < stones.length; i++) {
     const stone = stones[i];
     maxHeap.insert(stone);
   }
   // O(log n) * 3
   while (maxHeap.size() > 1) {
     console.log(Object.assign([], maxHeap.heap));
     let y = maxHeap.extractMax();
     let x = maxHeap.extractMax();
     if (y !== x) {
       y = y - x;
       maxHeap.insert(y);
     }
   }
   return maxHeap.heap[0] ? maxHeap.heap[0] : 0;
 }
 const stones1 = [2,7,4,1,8,1]; // 1
 const stones2 = [2]; // 2
 const stones3 = [2,2]; // 0
 // console.log('RESULT: ', lastStoneWeight(stones3));
 
 // use sorting solution
 function lastStoneWeightSort(stones) {
   // O(n log n)
   stones.sort( (a,b) => a - b);
   // O(n)
   while (stones.length > 1) {
     console.log('stones', stones);
     let y = stones.pop();
     let x = stones.pop();
     if (y != x) {
       y = y - x;
       let inserted = false;
       if (y <= stones[0]) {stones.splice(0, 0, y); inserted = true;}
       else if (y >= stones[stones.length - 1]) {stones.push(y); inserted = true;}
       if (!inserted) {
         for (let i = 1; i < stones.length - 1; i++) {
           const n = stones[i];
           if (y <= n) {
             stones.splice(i,0,y);
             inserted = true;
             break;
           }
         }
       }
       if (!inserted) stones.splice(stones.length - 2, 0, y);
     }
   }
   return stones[0] ? stones[0] : 0;
 }
 console.log('RESULT sort: ', lastStoneWeightSort(stones3));
 