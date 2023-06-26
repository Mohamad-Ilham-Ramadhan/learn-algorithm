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

   Solution by myself:
      Depth first search and backtracking

   LeetCode submission:
      #1
         - runtime: 50 ms, beats 62.3%
         - memory: 16.8 MB, beats 24.56%
      #2 (hashmap power up)
         - runtime: 57 ms, beats 21.55%
         - memory: 16.7 MB, beats 60.97%
      #3 (hashmap power up and is statement order revamped)
         - runtime: 46 ms, beats 81.43%
         - memory: 16.6 MB, beats 60.94%

"""


# attempt #1
def generateParenthesis(n):
    """
    ( -> () -> ()( -> ()() -> ()()()
    ( -> () -> ()(( -> ()(())
    (( -> (() -> (()(
    (((
    """

    def dfs(s, o, c, operation):
        # print('s', s, 'o', o, 'c', c)
        if len(s) == n * 2:
            res.append(s)
            return
        if operation == "o":
            for i in range(1, (n - o) + 1):
                po = ""
                for j in range(1, i + 1):
                    po += "("
                dfs(s + po, o + j, c, "c")
        else:
            for i in range(1, (o - c) + 1):
                pc = ""
                for j in range(1, i + 1):
                    pc += ")"
                dfs(s + pc, o, c + j, "o")
        pass

    res = []
    dfs("", 0, 0, "o")
    return res

# hashmap power up
def solution2(n):
   mo = {}  # map of open parentheses
   mc = {}  # map of close parentheses

   def dfs(s, o, c, operation):
      print('============')
      #   print("mo", mo, "mc", mc)
      if len(s) == n * 2:
         res.append(s)
         return
      if operation == "o":
         for i in range(1, (n - o) + 1):
            po = ""
            if i - 1 in mo: 
               print('Prev open parenthes exist dont loop just append one', i - 1, i, i in mo)
               mo[i] = mo[i-1] + '('
               dfs(s + mo[i], o + i, c, "c")
               continue
            if i in mo: 
               print('hash map cheat!', i)
               dfs(s + mo[i], o + i, c, "c")
               continue
            for j in range(1, i + 1):
               print('open manual')
               po += "("
            mo[j] = po
            dfs(s + po, o + j, c, "c")
      else:
         for i in range(1, (o - c) + 1):
            pc = ""
            if i - 1 in mc: 
               print('Prev close parenthes exist dont loop just append one', i - 1, i, i in mc)
               mc[i] = mc[i-1] + ')'
               dfs(s + mc[i], o, c + i, "o")
               continue
            if i in mc: 
               print('hash map cheat!', i)
               dfs(s + mc[i], o, c + i, "o")
               continue
            for j in range(1, i + 1):
               print('close manual')
               pc += ")"
            mc[j] = pc
            dfs(s + pc, o, c + j, "o")

   res = []
   dfs("", 0, 0, "o")
   return res

# hashmap power up (if statement order revamped)
def solution3(n):
   mo = {}  # map of open parentheses
   mc = {}  # map of close parentheses

   def dfs(s, o, c, operation):
      print('============')
      #   print("mo", mo, "mc", mc)
      if len(s) == n * 2:
         res.append(s)
         return
      if operation == "o":
         for i in range(1, (n - o) + 1):
            po = ""
            if i in mo: 
               print('hash map cheat!', i)
               dfs(s + mo[i], o + i, c, "c")
               continue
            if i - 1 in mo: 
               print('Prev open parenthes exist dont loop just append one', i - 1, i, i in mo)
               mo[i] = mo[i-1] + '('
               dfs(s + mo[i], o + i, c, "c")
               continue
            for j in range(1, i + 1):
               print('open manual')
               po += "("
            mo[j] = po
            dfs(s + po, o + j, c, "c")
      else:
         for i in range(1, (o - c) + 1):
            pc = ""
            if i in mc: 
               print('hash map cheat!', i)
               dfs(s + mc[i], o, c + i, "o")
               continue
            if i - 1 in mc: 
               print('Prev close parenthes exist dont loop just append one', i - 1, i, i in mc)
               mc[i] = mc[i-1] + ')'
               dfs(s + mc[i], o, c + i, "o")
               continue
            for j in range(1, i + 1):
               print('close manual')
               pc += ")"
            mc[j] = pc
            dfs(s + pc, o, c + j, "o")

   res = []
   dfs("", 0, 0, "o")
   return res



n1 = 1
n2 = 2
n3 = 3
n4 = 4
print("RESULT : ", solution3(4))

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
