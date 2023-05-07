/*
   LeetCode problem: Min Stack (medium)
   
   Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

   Implement the MinStack class:

   MinStack() initializes the stack object.
   void push(int val) pushes the element val onto the stack.
   void pop() removes the element on the top of the stack.
   int top() gets the top element of the stack.
   int getMin() retrieves the minimum element in the stack.
   You must implement a solution with O(1) time complexity for each function.

   

   Example 1:

   Input
   ["MinStack","push","push","push","getMin","pop","top","getMin"]
   [[],[-2],[0],[-3],[],[],[],[]]

   Output
   [null,null,null,null,-3,null,0,-2]

   Explanation
   MinStack minStack = new MinStack();
   minStack.push(-2);
   minStack.push(0);
   minStack.push(-3);
   minStack.getMin(); // return -3
   minStack.pop();
   minStack.top();    // return 0
   minStack.getMin(); // return -2
   

   Constraints:

   -231 <= val <= 231 - 1
   Methods pop, top and getMin operations will always be called on non-empty stacks.
   At most 3 * 104 calls will be made to push, pop, top, and getMin.

   Solution by myself: 
      the min also using stack 
      All operation is O(1)

   LeetCode submission:
      Runtime: 102 ms, beats 67.58%
      Memory: 49.4 MB, beats 77%
   
*/
function l(param) {
   console.log(param);
}
var MinStack = function() {
    this.min = []; // also a stack
    this.stack = [];
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
   if (this.min.length === 0) {
      this.min.push(val);
   } else if (val <= this.min[this.min.length - 1]) {
      this.min.push(val)
   }
    this.stack.push(val);
    return null;
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
   if (this.stack.pop() === this.min[this.min.length - 1]) this.min.pop();
   return null;
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.stack[this.stack.length - 1];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
   return this.min[this.min.length - 1];
};

// ["MinStack","push","push","push","push","getMin","pop","getMin","pop","getMin","pop","getMin"]
// [[],[2],[0],[3],[0],[],[],[],[],[],[],[]]
const s = new MinStack();
s.push(2);
s.push(0);
s.push(3);
s.push(0);
l(s.min);
l(s.getMin());
l(s.pop());
l(s.getMin());
l(s.pop());
l(s.getMin());
l(s.pop());
l(s.getMin());

