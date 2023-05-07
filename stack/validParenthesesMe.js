/*
   LeetCode problem: Valid Parentheses (easy)

   Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

   An input string is valid if:

   Open brackets must be closed by the same type of brackets.
   Open brackets must be closed in the correct order.
   Every close bracket has a corresponding open bracket of the same type.
   

   Example 1:
      Input: s = "()"
      Output: true

   Example 2:
      Input: s = "()[]{}"
      Output: true

   Example 3:
      Input: s = "(]"
      Output: false

   Example 4:
      Input: s = "{[]}"
      Output: true
   
   Constraints:
      1 <= s.length <= 104
      s consists of parentheses only '()[]{}'.
   
   Solution by myself: 
      if s.length is odd then it's not a valid. 
      
      we create a stack of opening parentheses
      when we find a closing parentheses in the loop then pop it off the stack
      then we match it, if it doesn't match then return false 
      if the loop is over and the stack is still containing open parentheses then return false;
   
   LeetCode submission:
      Runtime: 58 ms, beats 82.17%
      Memory: 41.9 MB, beats 87.76%

   Time complexity: O(n) because we just have to loop over the `s`
   Space complexity: O(n) because we must store the openning parentheses in the stack
*/

function validParentheses(s) {
   if (s.length % 2 === 1) return false;
   let stack = [];
   for (let i = 0; i < s.length; i++) {
      // if s[i] is a closing parenthesis so we check the last element of stack
      if (s[i] === '}') {
         if (stack.pop() !== '{') return false;
      } else if (s[i] === ']') {
         if (stack.pop() !== '[') return false;
      } else if (s[i] === ')') {
         if (stack.pop() !== '(') return false;
      } else {
         stack.push(s[i]);
      }
   }
   if (stack.length !== 0) return false;
   return true;
}
const s1 = "()"; const s2 = '()[]{}'; const s3 = '(]'; const s4 = "{[]}";
console.log(validParentheses(s4));