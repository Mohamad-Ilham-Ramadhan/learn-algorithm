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

    Solution by NeetCode
        backtracking
    
    leetcode submission: 
        runtime: 58 ms, beats 94.68%
        memory: 16.94 MB, beats 19.23%
'''
def solveNQueens(n):
    col = set()
    posDiag = set() 
    negDiag = set() 

    res = []
    board = [['.'] * n for i in range(n)]

    def backtrack(r):
        if r == n: 
            copy = [''.join(row) for row in board]
            res.append(copy)
            return 
        
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue 

            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c] = 'Q'

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = '.'
    
    backtrack(0)
    return res

# str = '...Q'
# print(str.ljust(4, '.'))
print('RESULT :', solveNQueens(4))
n = 4
board = [['.'] * n for i in range(n)]
copy = [''.join(row) for row in board]
print('copy', copy)


'''
    [Q][ ][ ][ ]
    [ ][ ][Q][ ]
    [ ][ ][ ][ ]
    [ ][ ][ ][ ]
'''
