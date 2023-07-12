'''
   (backtracking) leetcode: 130. Surrounded Regions (medium)

   Given an `m x n` matrix `board` containing `'X'` and `'O'`, capture all regions that are 4-directionally surrounded by `'X'`.

   A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region.

   

   Example 1:


   Input: board = [
      ["X","X","X","X"],
      ["X","O","O","X"],
      ["X","X","O","X"],
      ["X","O","X","X"]
   ]
   Output: [
      ["X","X","X","X"],
      ["X","X","X","X"],
      ["X","X","X","X"],
      ["X","O","X","X"]
   ]
   Explanation: Notice that an 'O' should not be flipped if:
         - It is on the border, or
         - It is adjacent to an 'O' that should not be flipped.
         The bottom 'O' is on the border, so it is not flipped.
         The other three 'O' form a surrounded region, so they are flipped.

   Example 2:
      Input: board = [["X"]]
      Output: [["X"]]
   

   Constraints:
      - m == board.length
      - n == board[i].length
      - 1 <= m, n <= 200
      - board[i][j] is 'X' or 'O'.

   Related Topics: 
      (Array) (Depth-first search) (Breadth-first search) (Union find) (Matrix)
   ==============================================================

   solution by myself
      Depth-first search

   leetcode submission: 
      # solution #2
         runtime: 168 ms, beats 35.92%
         memory: 18.4 MB, beats 34.41%
'''
def solve(board):
   visited = {} # (x,y) : [left,top,right,bottom](True/False) True means not flip, False means flip

   z = 0
   def dfs(x,y,direction):
      # nonlocal z
      # if z == 30: return False 
      # z+=1
      # print('x', x, 'y', y)
      if (  x < 0 or y < 0 or 
            x == len(board[0]) or y == len(board) 
         ) : return True
      
      if board[y][x] == 'X': return False
      if (x,y) in visited and board[y][x] == 'O': 
         print('VISITED AND STOP', x,y, visited[(x,y)][direction])
         return visited[(x,y)][direction]
      
      if (x,y) not in visited: 
         visited[(x,y)] = [None,None,None,None]

      left = dfs(x-1,y,0) # to left
      print('left', x,y, left)
      visited[(x,y)][0] = left
      top = dfs(x,y-1,1) # to top
      visited[(x,y)][1] = top
      right = dfs(x+1,y,2) # to right
      visited[(x,y)][2] = right
      bottom = dfs(x,y+1,3) # to bottom
      visited[(x,y)][3] = bottom

      
      if left or top or right or bottom: 
         print('True NOT FLIP', x,y)
         return True 
      print('FALSE FLIP', x,y)
      board[y][x] = 'X'
      return False
   
   for y in range(len(board)):
      for x in range(len(board[0])):
         print('for loop', x, y, board[y][x])
         if (x,y) in visited or board[y][x] == 'X': continue 
         dfs(x,y,0)

   print('new board', board)

def solution2(board): 
   marked = set() # if cell is marked then it will not be flipped
   def dfs(x,y): 
      if (x < 0 or y < 0 or x == len(board[0]) or y == len(board) or board[y][x] == 'X' or (x,y) in marked): 
         return 
      marked.add((x,y))
      dfs(x-1,y) # left
      dfs(x+1,y) # right
      dfs(x,y-1) # top
      dfs(x,y+1) # bottom
   
   y = 0
   while y < len(board): 
      x = 0 
      while x < len(board[0]):
         print('frame', y,x)
         if y == 0 or y == len(board) - 1: 
            if (x,y) not in marked and board[y][x] == 'O':
               print('push')
               dfs(x,y)
         elif (x == 0 or x == (len(board[0]) - 1)) and (x,y) not in marked and board[y][x] == 'O': 
               print('push edge', board[y][x])
               dfs(x,y)
         
         x += 1
      
      y += 1
   
   # flip cell not marked
   # print('marked', marked)
   print('FLIP ======================== FLIP')
   y = 1
   while y < (len(board)-1):
      x = 1
      while x < (len(board[0])-1): 
         print(board[y][x])
         if (x,y) not in marked: 
            board[y][x] = 'X'
         x += 1
      y += 1

   print('final board', board)

b1 = [
      ["X","X","X","X"],
      ["X","O","O","X"],
      ["X","X","O","X"],
      ["X","O","X","X"]
   ]
''''
      ["X","X","X","X"],
      ["X","X","X","X"],
      ["X","X","X","X"],
      ["X","O","X","X"]
'''
b2  = [
      ["X","X","X","X"],
      ["X","O","O","X"],
      ["X","X","O","X"],
      ["X","O","O","X"]
   ]
'''
      ["X","X","X","X"],
      ["X","O","O","X"],
      ["X","X","O","X"],
      ["X","O","O","X"]
'''
solution2(b1)
b3 = [
   ["O","O","O","O","X","X"],
   ["O","O","O","O","O","O"],
   ["O","X","O","X","O","O"],
   ["O","X","O","O","X","O"],
   ["O","X","O","X","O","O"],
   ["O","X","O","O","O","O"]]
'''
   [
      ["O","O","O","O","X","X"],
      ["O","O","O","O","O","O"],
      ["O","X","O","X","O","O"],
      ["O","X","O","O","X","O"],
      ["O","X","O","X","O","O"],
      ["O","X","O","O","O","O"]]
'''
# solve(b3)