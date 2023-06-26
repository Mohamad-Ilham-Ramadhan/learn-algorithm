'''
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

   Solution by myself:
      Depth first search and backtracking

   LeetCode submission:
      #1
         - runtime: 50 ms, beats 62.3%
         - memory: 16.8 MB, beats 24.56%
'''

# attempt #1
def generateParenthesis(n): 
   '''
      ( -> () -> ()( -> ()() -> ()()()
      ( -> () -> ()(( -> ()(())
      (( -> (() -> (()(
      (((
   '''
   def dfs(s, o, c, operation):
      # print('s', s, 'o', o, 'c', c)
      if len(s) == n * 2: 
            res.append(s)
            return
      if operation == 'o': 
         for i in range(1, (n - o) + 1):
            po = ''
            for j in range(1, i + 1): 
               po += '('
            dfs(s + po, o + j, c, 'c')
      else: 
         for i in range(1, (o - c) + 1): 
            pc = ''
            for j in range(1, i + 1): 
               pc += ')'
            dfs(s + pc, o, c+j, 'o')
      pass
   
   res = []
   dfs('', 0, 0, 'o')
   return res

n1 = 1
n2 = 2
n3 = 3
n4 = 4
print('RESULT : ', generateParenthesis(3))

'''
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

   
'''