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
		runtime: 2661 ms, beats 18.59%
		memory: 178.90 MB, beats 7.23%
"""
import heapq
# Solution by NeetCode's
def minCostConnectPoints(points):
    N = len(points)

    adj = { i:[] for i in range(N) } # list of [cost, node]

    for i in range(N):
        x1, y1 = points[i]
        for j in range(i + 1, N):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            adj[i].append([dist, j])
            adj[j].append([dist, i])

    # Prim's
    res = 0
    visit = set()
    minH = [[0, 0]] # [cost, node]
    while len(visit) < N:
        cost, i = heapq.heappop(minH)
        if i in visit: continue 

        res += cost 
        visit.add(i)
        for neiCost, nei in adj[i]:
            if nei not in visit:
                heapq.heappush(minH, [neiCost, nei])

    return res

p1 = [[0,0],[2,2],[3,10],[5,2],[7,0]] # 20
p2 = [[3,12],[-2,5],[-4,1]] # 18
p3 = [[0,0]] # 0
p4 = [[-14,-14],[-18,5],[18,-10],[18,18],[10,-2]] # 102
p5 = [[0,0],[1,1],[1,0],[-1,1]] # 4

print('RESULT: ', minCostConnectPoints(p1))