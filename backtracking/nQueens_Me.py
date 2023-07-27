'''
    (backtracking) leetcode: 51. N-Queens (hard)

    The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

    Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

    Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

    

    Example 1:
        [ ][Q][ ][ ]        [ ][ ][Q][ ]
        [ ][ ][ ][Q]        [Q][ ][ ][ ]
        [Q][ ][ ][ ]        [ ][ ][ ][Q]
        [ ][ ][Q][ ]        [ ][Q][ ][ ]

        Input: n = 4
        Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
        Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

    Example 2:
        [Q]

        Input: n = 1
        Output: [["Q"]]
    

    Constraints:
        -1 <= n <= 9
    
    Related topics:

    ==========================================================================

    Solution by myself
        backtracking
    
    leetcode submission: 
        runtime: 168 ms, beats 10.97%
        memory: 16.78 MB, beats 80.76%
'''
def solveNQueens(n):
    res = []
    def backtrack(board, i): 
        print('board', board, 'i', i)
        if i == n: 
            res.append(board.copy())
            return True

        s = ''
        for j in range(n): 
            print('i', i, 'j', j)
            s += 'Q'
            board.append(s.ljust(n, '.'))

            # can we place queen in this cell [START] ===========
            isTrue = True
            l = j-1 # left diagonal
            r = j+1 # right diagonal
            up = i-1
            # check border top
            b = j-1
            for x in range(b, b+3):
                if up < 0 or x < 0 or x == n: continue 
                cell = board[up][x]
                if cell == 'Q': 
                    print('False, there is a Queen')
                    isTrue = False
                    break
            
            if isTrue:
               while up > -1: 
                  # check diagonal left 
                  if l > -1: 
                     print('diagonal left', board[up][l])
                     if board[up][l] == 'Q':
                           isTrue = False
                           break
                  # check up
                  print('up', board[up][i])
                  if board[up][j] == 'Q': 
                     isTrue = False
                     break
                  if r < n:
                     print('diagonal right', board[up][r])
                     if board[up][r] == 'Q':
                           isTrue = False
                           break
                           
                  up -= 1
                  l -= 1
                  r += 1
            # can we place queen in this cell [END] ===========
            if isTrue:
                backtrack(board, i+1)
            s = s[:-1]
            board.pop() 
            s += '.'

        return False

    
    backtrack([], 0)
    return res


# str = '...Q'
# print(str.ljust(4, '.'))
print('RESULT :', solveNQueens(2))


'''
    [Q][ ][ ][ ]
    [ ][ ][Q][ ]
    [ ][ ][ ][ ]
    [ ][ ][ ][ ]
'''
