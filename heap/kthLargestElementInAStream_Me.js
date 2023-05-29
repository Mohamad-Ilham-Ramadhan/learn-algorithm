
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

  Solution by myself:
    Not using heap. I still don't understand using heap know.

  LeetCode submission:
    #1
    - Runtime: 183 ms, beats 50.6%
    - Memory: 49 MB, beats 94.67%
    #2
    - Runtime: 163 ms, beats 57.42%
    - Memory: 49 MB, beats 94.67%
*/

// Not using heap. I still don't understand using heap know.
class KL {
   // initialization is O(n log n)
   constructor(k, nums) {
     this.k = k;
     this.nums = nums;
     this.nums.sort( (a,b) => a-b );
   }
 
   // O(n * 2)
   add(val) {
     if (this.nums.length === 0) {
       this.nums.push(val);
       return val;
     }
     // #2 [start]
     if (val <= this.nums[0]) {
       this.nums.splice(0,0,val);
       return this.nums[this.nums.length - this.k];
     }
     // let i; <--- delete
     // #2 [start]
     for (let i = this.nums.length - 1; i >= 0; i--) {
       const n = this.nums[i];
       if (val >= n) {
         this.nums.splice(i+1, 0, val);
         break;
       }
     }
     // #2 [start]
     // if (i === -1) {
     //   this.nums.splice(0,0,val);
     // }
     // #2 [end]
     return this.nums[this.nums.length - this.k];
   }
 }
 // const kl = new KL(3, [4,5,8,2]);
 // console.log('add 3 -> ', kl.add(3)); // 4
 // console.log('add 5 -> ', kl.add(5)); // 5
 // console.log('add 10 -> ', kl.add(10)); // 5
 // console.log('add 9 -> ', kl.add(9)); // 8
 // console.log('add 4 -> ', kl.add(4)); // 8
 // console.log('kl.nums', kl.nums);
 
 // const kl = new KL(1, []);
 // console.log('add 3 -> ', kl.add(-3)); // 
 // console.log('add 5 -> ', kl.add(-2)); // 
 // console.log('add 10 -> ', kl.add(-4)); // 
 // console.log('add 9 -> ', kl.add(0)); // 
 // console.log('add 4 -> ', kl.add(4)); // 
 // console.log('kl.nums', kl.nums);
 
 const kl = new KL(2, [0]);
 console.log('add -1 -> ', kl.add(-1)); // -1
 console.log('add 1 -> ', kl.add(1)); // 0
 console.log('add -2 -> ', kl.add(-2)); // 0
 console.log('add -4 -> ', kl.add(-4)); // 0
 console.log('add 3 -> ', kl.add(3)); // 1
 console.log('kl.nums', kl.nums);