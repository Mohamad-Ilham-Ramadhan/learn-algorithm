'''
    (graph) leetcode (premium) 286, lintcode: 663. Walls and gates (medium)

    You are given a m x n 2D grid initialized with these three possible values.

    `-1` - A wall or an obstacle.
    `0` - A gate.
    `INF` - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

    Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with INF


    Example 1
        Input:
            [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
        Output:
            [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

        Explanation:
            the 2D grid is:
            INF   -1   0   INF
            INF  INF  INF  -1
            INF   -1  INF  -1
            0    -1   INF  INF
            the answer is:
            3  -1   0   1
            2   2   1  -1
            1  -1   2  -1
            0  -1   3   4

    Example 2
        Input:
            [[0,-1],[2147483647,2147483647]]
        Output:
            [[0,-1],[1,2]]

    Related Topics 
        (Breadth-first search)
    
    Company
        [Facebook, Google, OpenAI]

    ======================================================================

    Solution by myself
        breadth-first search

    Lintcode submission:
        runtime: 572 ms
        Memory: 9.67 MB
        beats: 89.40%
'''

from collections import deque
INF = 2147483647
def walls_and_gates(rooms): 
    rows = len(rooms)
    cols = len(rooms[0])
    for r in range(rows):
        for c in range(cols): 
            if rooms[r][c] <= 0: continue 
            # breadth first search
            q = deque() # (row, col, distance)
            visited = set()
            visited.add((r,c)) # current
            q.append((r,c+1,1)) # right
            q.append((r+1,c,1)) # bottom
            q.append((r,c-1,1)) # left
            q.append((r-1,c,1)) # top
            while len(q):
                [row,col,d] = q.popleft()
                if (row,col) in visited or row < 0 or row == rows or col < 0 or col == cols or rooms[row][col] == -1: continue 

                visited.add((row,col))

                if rooms[row][col] == 0: 
                    rooms[r][c] = d 
                    break
                
                # collect all 4 direction
                q.append((row,col+1,d+1)) # right
                q.append((row+1,col,d+1)) # bottom
                q.append((row,col-1,d+1)) # left
                q.append((row-1,col,d+1)) # top
    
    print('new rooms', rooms)



r1 = [
    [INF,   -1,    0,   INF],
    [INF,   INF,   INF, -1],
    [INF,   -1,    INF, -1],
    [0,     -1,    INF, INF]
] # [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
r2 = [[0,-1],[INF,INF]] # [[0,-1],[1,2]]
walls_and_gates(r2)