'''
   (stack) leetcode: 150. Evaluate Reverse Polish Notation (medium)

   You are given an array of strings `tokens` that represents an arithmetic expression in a Reverse Polish Notation.

   Evaluate the expression. Return an integer that represents the value of the expression.

   Note that:

   The valid operators are '+', '-', '*', and '/'.
   Each operand may be an integer or another expression.
   The division between two integers always truncates toward zero.
   There will not be any division by zero.
   The input represents a valid arithmetic expression in a reverse polish notation.
   The answer and all the intermediate calculations can be represented in a 32-bit integer.
   

   Example 1:
      Input: tokens = ["2","1","+","3","*"]
      Output: 9
      Explanation: ((2 + 1) * 3) = 9

   Example 2:
      Input: tokens = ["4","13","5","/","+"]
      Output: 6
      Explanation: (4 + (13 / 5)) = 6

   Example 3:
      Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
      Output: 22
      Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
      = ((10 * (6 / (12 * -11))) + 17) + 5
      = ((10 * (6 / -132)) + 17) + 5
      = ((10 * 0) + 17) + 5
      = (0 + 17) + 5
      = 17 + 5
      = 22
   

   Constraints:
      - 1 <= tokens.length <= 104
      - tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
   
   ======================================================

   Solution by myself

   Leetcode submission
      runtime: 94 ms, beats 20.35% 
      memory: 16.9 MB, beats 22.19%
'''
import math
def evalRPN(tokens):
   stack = []
   for t in tokens:
      print('stack', stack)
      if t == '+':
         n1 = stack.pop()
         n2 = stack.pop()
         stack.append(math.floor( int(n2) + int(n1) ) )
      elif t == '*':
         n1 = stack.pop()
         n2 = stack.pop()
         stack.append(math.floor( int(n2) * int(n1) ) )
      elif t == '-':
         n1 = stack.pop()
         n2 = stack.pop()
         stack.append(math.floor( int(n2) - int(n1) ) )
      elif t == '/':
         n1 = int(stack.pop())
         n2 = int(stack.pop())
         if n2 / n1 > 0:
            sum = math.floor(n2 / n1)
         else: 
            sum = math.ceil(n2 / n1)
         stack.append(sum)
      else: 
         stack.append(t)
      
   print('stack', stack)
   
   return int(stack[0]) if isinstance(stack[0], str) else stack[0] 

t1 = ["2","1","+","3","*"] # 9
t2 = ["4","13","5","/","+"] # 6
t3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] # 22
t4 = ['18']
'''
   ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
   [10, 6, 9, 3, +] [10,6,12,-11,*] [10,6,-132,/] [10,0,*] [0,17,+] [17,5,+] [22]
'''
# print('RESULT :', evalRPN(t3))
import unittest
import time
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
    
    def tearDown(self) -> None:
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_xxx(self):
        self.assertEqual(evalRPN(t1), 9) 
        self.assertEqual(evalRPN(t2), 6) 
        self.assertEqual(evalRPN(t3), 22)
        self.assertEqual(evalRPN(t4), 18)

if __name__ == "__main__":
    unittest.main()

# print(isinstance('18',str))