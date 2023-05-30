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

  LeetCode submission:
    - Runtime: 57 ms, beats 78.21%;
    - Memory: 44.6 MB, beats 9.12%
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
function lastStoneWeight(stones) {
  const maxHeap = new MaxHeap();
  for (let i = 0; i < stones.length; i++) {
    const stone = stones[i];
    maxHeap.insert(stone);
  }
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
const stones1 = [2,7,4,1,8,1];
const stones2 = [2];
const stones3 = [2,2];
console.log('RESULT: ', lastStoneWeight(stones3))