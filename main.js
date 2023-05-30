/*
  leetcode: 973. K Closest Points to Origin (medium)

  Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

  The distance between two points on the X-Y plane is the Euclidean distance (i.e., `√(x1 - x2)2 + (y1 - y2)2)`.

  You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

  

  Example 1:
                   5
                   4
                   3 .
                   2    
                   1
    -5 -4 -3 -2 -1 0  1  2  3  4  5
                   -1
              .    -2
                   -3
                   -4
                   -5
    Input: points = [[1,3],[-2,2]], k = 1
    Output: [[-2,2]]
    Explanation:
      - The distance between (1, 3) and the origin is sqrt(10).
      - The distance between (-2, 2) and the origin is sqrt(8).
      - Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
      - We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

  Example 2:

    Input: points = [[3,3],[5,-1],[-2,4]], k = 2
    Output: [[3,3],[-2,4]]
    Explanation: The answer [[-2,4],[3,3]] would also be accepted.
  

  Constraints:
    - 1 <= k <= points.length <= 104
    - -104 < xi, yi < 104

  Solution by myself:
    use max heap to store the points
    size of the max heap is equal to k 
    the max number become thresholder
    if a points is smaller than the max number then extract the max and insert the points 

  LeetCode submission: 
    #1 
      - Runtime: 217 ms, beats 66.16%
      - Memory: 63.1 MB, beats 23.93%
    #2 
      - Runtime: 230 ms, beats 53.78%
      - Memory: 63.8 MB, beats 22.40%
*/

// max heap designed only for this problem
class MaxHeap {
  constructor() {
    this.heap = [];
  }
  peek() {
    return this.heap[0] ? this.heap[0] : null;
  }
  heapifyUp() {
    let currentIndex = this.heap.length - 1;
    while (currentIndex > 0) {
      let parrentIndex = Math.floor( (currentIndex - 1) / 2);
      let maxIndex = currentIndex;
      if (this.heap[currentIndex]?.distance > this.heap[parrentIndex]?.distance) {
        maxIndex = parrentIndex;
      }
      if (currentIndex === maxIndex) return;
      [ this.heap[currentIndex], this.heap[parrentIndex] ] = [ this.heap[parrentIndex], this.heap[currentIndex] ];
      currentIndex = maxIndex;
    }
  }
  // { distance: float, point: [x,y]}
  insert(val) {
    if (this.heap.length === 0) { this.heap.push(val); return;}
    this.heap.push(val);
    this.heapifyUp(); 
  }
  heapifyDown() {
    let currentIndex = 0;
    while (true) {
      let leftIndex = 2 * currentIndex + 1;
      let rightIndex = 2 * currentIndex + 2;
      let maxIndex = currentIndex;

      if ( this.heap[leftIndex]?.distance > this.heap[maxIndex]?.distance) maxIndex = leftIndex; 
      if ( this.heap[rightIndex]?.distance > this.heap[maxIndex]?.distance) maxIndex = rightIndex; 

      if (maxIndex === currentIndex) return;

      [ this.heap[currentIndex], this.heap[maxIndex] ] = [ this.heap[maxIndex], this.heap[currentIndex] ];
      
      currentIndex = maxIndex;
    }
  }
  extractMax() {
    const max = this.heap[0];
    const last = this.heap.pop();
    if (this.heap.length > 0) {
      this.heap[0] = last;
      this.heapifyDown();
    }
    return max ? max : null;
  }
}
const mh = new MaxHeap();

function kClosest(points, k) {
  // #2 [start]
  if (points.length === k) {console.log('same'); return points;}
  // #2 [end]
  const mh = new MaxHeap();
  for (let i = 0; i < points.length; i++) {
    const point = points[i];
    const distance = Math.sqrt( Math.pow(0 - point[0] , 2) + Math.pow(0 - point[1], 2) );
    if (mh.heap.length < k) {
      mh.insert({point, distance});
      continue;
    }
    if (distance < mh.peek().distance) {
      mh.extractMax();
      mh.insert({point, distance});
    }
  }
  let result = [];
  for (let value of mh.heap) {
    result.push(value.point);
  }
  return result;
}
const points1 = [[1,3],[-2,2]]; 
const k1 = 1;
const points2 = [[3,3], [5,-1], [-2,4]];
const k2 = 2
const points3 = [[3,5]];
const k3 = 1;
const points4 = [[1,2], [2,3], [3,4]];
const k4 = 3
console.log('RESULT: ', kClosest(points4, k4));