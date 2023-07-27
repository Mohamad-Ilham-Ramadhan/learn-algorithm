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

    Solution by NeetCode
    
    Lintcode submission:
        runtime: 732 ms
        Memory: 23.57 MB
        beats: 68.60%
'''

from collections import deque
INF = 2147483647
def walls_and_gates(rooms): 
    ROWS, COLS = len(rooms), len(rooms[0])
    visit = set() 
    q = deque()
    print('ROWS', ROWS, 'COLS', COLS)
    def addRoom(r,c):
        print('addroom', r,c)
        if (r < 0 or r == ROWS or c < 0 or c == COLS or
            (r,c) in visit or rooms[r][c] == -1):
            return 
        visit.add((r,c))
        q.append([r,c])

    for r in range(ROWS):
        for c in range(COLS):
            if rooms[r][c] == 0: 
                q.append([r,c])
                visit.add((r,c))

    dist = 0 # distance 
    while q: 
        for i in range(len(q)):
            r, c = q.popleft()
            rooms[r][c] = dist 
            addRoom(r + 1, c)
            addRoom(r - 1, c)
            addRoom(r, c + 1)
            addRoom(r, c - 1)
        
        dist += 1

    print('new rooms', rooms)



r1 = [
    [INF,   -1,    0,   INF],
    [INF,   INF,   INF, -1],
    [INF,   -1,    INF, -1],
    [0,     -1,    INF, INF]
] # [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
r2 = [[0,-1],[INF,INF]] # [[0,-1],[1,2]]
walls_and_gates(r1)