"""
	(Advanced Graph) leetcode: 1584. Min Cost to Connect All Points (medium)

	Link: https://leetcode.com/problems/min-cost-to-connect-all-points/
    
	Tags: Array, Union find, Graph, Minimum Spanning Tree

	Constraints:
        - 1 <= points.length <= 1000
        - 10^6 <= xi, yi <= 10^6
        - All pairs (xi, yi) are distinct.
	======================================================================

	Submissions: 
		runtime: 4286 ms, beats 6.61%
		memory: 147.60 MB, beats 22.96%
"""

def minCostConnectPoints(points):
    def manhattanDistance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    graph = {}
    minMd = float('inf')
    mPoints = []
    for i in range(0, len(points) - 1):
        pi = (points[i][0], points[i][1])
        if pi not in graph : graph[pi] = []
        for j in range(i + 1, len(points)): 
            pj = (points[j][0], points[j][1])
            if pj not in graph: graph[pj] = []
            md = manhattanDistance(pi, pj)
            graph[pi].append([md, pj])
            graph[pj].append([md, pi])
            if md < minMd: 
                minMd = md 
                mPoints = [pi, pj]

    for p in graph: 
        graph[p].sort(reverse=True, key=lambda x:x[0])

    print('graph', graph)
    print('minMd', minMd, 'mPoints', mPoints)

    # Prim's algorithm to search the MST (minimum spanning Tree)
    res = minMd
    visited = set(mPoints)
    while len(visited) < len(points):
        minP = [float('inf'), None]
        for fp in mPoints:
            while graph[fp]:
                if graph[fp][-1][1] in visited:
                    graph[fp].pop()
                elif graph[fp][-1][0] < minP[0]:
                    minP = graph[fp][-1]
                else: break


        print('final minP', minP)
        res += minP[0]
        mPoints.append(minP[1])
        visited.add(minP[1])

    return 0 if res == float('inf') else res

p1 = [[0,0],[2,2],[3,10],[5,2],[7,0]] # 20
p2 = [[3,12],[-2,5],[-4,1]]
p3 = [[0,0]]
'''
graph {
    (0, 0): [[13, (3, 10)], [7, (5, 2)], [7, (7, 0)], [4, (2, 2)]], 
    (2, 2): [[9, (3, 10)], [7, (7, 0)], [4, (0, 0)], [3, (5, 2)]], 
    (3, 10): [[14, (7, 0)], [13, (0, 0)], [10, (5, 2)], [9, (2, 2)]], 
    (5, 2): [[10, (3, 10)], [7, (0, 0)], [4, (7, 0)], [3, (2, 2)]], 
    (7, 0): [[14, (3, 10)], [7, (0, 0)], [7, (2, 2)], [4, (5, 2)]]}
'''
print('RESULT: ', minCostConnectPoints(p3))