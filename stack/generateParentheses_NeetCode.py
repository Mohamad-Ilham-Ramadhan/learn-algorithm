"""
   (stack) leetcode: 22. Generate Parentheses (medium)

   Related topics: [string, dynamic programming, backtracking]

   Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 

   Example 1:
      Input: n = 3
      Output: ["((()))","(()())","(())()","()(())","()()()"]

   Example 2:
      Input: n = 1
      Output: ["()"]
   

   Constraints:
      - 1 <= n <= 8

   ===============================================

   Solution by NeetCode:
      stack and backtracking

   LeetCode submission:
      - runtime: 48 ms, beats 71.25%
      - memory: 16.6 MB, beats 92.89%


"""


# attempt #1
def generateParenthesis(n):
   stack = []
   res = []
   def backtrack(openN, closedN):
      if openN == closedN ==n:
         res.append(''.join(stack))
      
      if openN < n:
         stack.append('(')
         backtrack(openN + 1, closedN)
         stack.pop()
      
      if closedN < openN:
         stack.append(')')
         backtrack(openN, closedN + 1)
         stack.pop()
   
   backtrack(0, 0)
   return res



n1 = 1
n2 = 2
n3 = 3
n4 = 4
print("RESULT : ", generateParenthesis(3))

"""
   n = 4

   ( -> ()( -> ()()( -> ()()()()
   ( -> ()( -> ()()(())
   ( -> ()(( -> ()(()())
   ( -> ()(( -> ()(())()
   ( -> ()((( -> ()((()))
   
   (( -> (()( -> (()()())
   (( -> (()( -> (()())()
   (( -> (()(( -> (()(()))
   (( -> (())( -> (())()()
   (( -> (())(( -> (())(())

   ((( -> ((()())   
   ((( -> ((())())  
   ((( -> ((()))()
   
   (((())))
"""
