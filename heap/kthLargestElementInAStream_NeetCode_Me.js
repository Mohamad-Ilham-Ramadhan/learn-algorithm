
/*
  LeetCode: 703. Kth Largest Element in a Stream (easy)

  Design a class to find the `kth` largest element in a stream. Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

  Implement `KthLargest` class:

  `KthLargest(int k, int[] nums)` Initializes the object with the integer `k` and the stream of integers `nums`.
  `int add(int val)` Appends the integer `val` to the stream and returns the element representing the `kth` largest element in the stream.
  

  Example 1:
    Input
      ["KthLargest", "add", "add", "add", "add", "add"]
      [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    Output
      [null, 4, 5, 5, 8, 8]
    Explanation
      KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
      kthLargest.add(3);   // return 4
      kthLargest.add(5);   // return 5
      kthLargest.add(10);  // return 5
      kthLargest.add(9);   // return 8
      kthLargest.add(4);   // return 8
  

  Constraints:
    - 1 <= k <= 104
    - 0 <= nums.length <= 104
    - -104 <= nums[i] <= 104
    - -104 <= val <= 104
    - At most 104 calls will be made to add.
    - It is guaranteed that there will be at least k elements in the array when you search for the kth element.

  Solution by NeetCode:
    using min heap and mantain heap size of k
    then the peek is the kth element

  LeetCode submission:
    #1 My code after watching of half NeetCode's solution explanation (NeetCode's solution similar)
    - Runtime: 124 ms, beats 84.12%
    - Memory: 51.2 MB, beats 64.56%
*/


// It turns out that NeetCode's implementation is pretty the same with mine. The difference is that Python have built-in heap.


// My code after watching of half NeetCode's solution explanation
class MinHeap {
   constructor() {
    this.heap = [];
  }

  insert(value) {
    this.heap.push(value);
    this.heapifyUp();
  }

  extractMin() {
    if (this.isEmpty()) {
      return null;
    }

    const min = this.heap[0];
    const last = this.heap.pop();

    if (!this.isEmpty()) {
      this.heap[0] = last;
      this.heapifyDown();
    }

    return min;
  }

  heapifyUp() {
    let currentIndex = this.heap.length - 1;

    while (currentIndex > 0) {
      const parentIndex = Math.floor((currentIndex - 1) / 2);

      if (this.heap[currentIndex] >= this.heap[parentIndex]) {
        break;
      }

      [this.heap[currentIndex], this.heap[parentIndex]] = [
        this.heap[parentIndex],
        this.heap[currentIndex],
      ];
      currentIndex = parentIndex;
    }
  }

  heapifyDown() {
    let currentIndex = 0;

    while (true) {
      const leftChildIndex = 2 * currentIndex + 1;
      const rightChildIndex = 2 * currentIndex + 2;
      let minIndex = currentIndex;

      if (
        leftChildIndex < this.heap.length &&
        this.heap[leftChildIndex] < this.heap[minIndex]
      ) {
        minIndex = leftChildIndex;
      }

      if (
        rightChildIndex < this.heap.length &&
        this.heap[rightChildIndex] < this.heap[minIndex]
      ) {
        minIndex = rightChildIndex;
      }

      if (minIndex === currentIndex) {
        break;
      }

      [this.heap[currentIndex], this.heap[minIndex]] = [
        this.heap[minIndex],
        this.heap[currentIndex],
      ];
      currentIndex = minIndex;
    }
  }

  isEmpty() {
    return this.heap.length === 0;
  }

  peek() {
    return this.isEmpty() ? null : this.heap[0];
  }

  size() {
    return this.heap.length;
  }
}
const mh = new MinHeap();
// mh.insert(30);
// mh.insert(50);
// mh.insert(100);
// mh.insert(40);
// mh.insert(40);
// mh.insert(15);
// mh.insert(10);
// // k = 6
// console.log(mh.peek()); 
// console.log(mh.extractMin());
// console.log(mh.size());
// console.log(mh.peek());

class KL {
  constructor(k, nums) {
    this.heap = new MinHeap();
    this.k = k;
    for (let i = 0; i < nums.length; i++) {
      this.heap.insert(nums[i]);
    }
    while (this.heap.size() > this.k) {
      this.heap.extractMin();
    }
  }
  add(val) {
    this.heap.insert(val);
    // console.log('heap after insert val', Object.assign({},this.heap.heap));
    // this.heap.extractMin();
    // return this.heap.peek();
    while (this.heap.size() > this.k) {
      this.heap.extractMin();
    }
    return this.heap.peek();
  }
}

// const kl = new KL(3, [4,5,8,2]);
// console.log('kl.heap', kl.heap);
// console.log('add 3 -> ', kl.add(3), 'epxect :', 4); //
// console.log('add 5 -> ', kl.add(5), 'epxect :', 5); //
// console.log('add 10 -> ', kl.add(10), 'epxect :', 5); //
// console.log('add 9 -> ', kl.add(9), 'epxect :', 8); //
// console.log('add 4 -> ', kl.add(4), 'epxect :', 8); //

const kl = new KL(2, [0]);
console.log('kl.heap', kl.heap);
console.log('add -1 -> ', kl.add(-1), 'epxect :', -1); //
console.log('add 1 -> ', kl.add(1), 'epxect :', 0); //
console.log('add -2 -> ', kl.add(-2), 'epxect :', 0); //
console.log('add -4 -> ', kl.add(-4), 'epxect :', 0); //
console.log('add 3 -> ', kl.add(3), 'epxect :', 1); //