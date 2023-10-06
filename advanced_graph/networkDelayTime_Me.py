"""
	(Advanced Graph) leetcode: 743. Network Delay Time (medium)

	Link: https://leetcode.com/problems/network-delay-time/
    
	Tags: Depth-first search, breadth-first search, graph, heap(priority queue), shortest path

	Constraints:
      - 1 <= k <= n <= 100
      - 1 <= times.length <= 6000
      - times[i].length == 3
      - 1 <= ui, vi <= n
      - ui != vi
      - 0 <= wi <= 100
      - All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
	======================================================================

	Submissions: 
		runtime: 3893 ms, beats 5.02%
		memory: 20.96 MB, beats 7.72%
"""

def networkDelayTime(times, n, k):
    graph = {} # list of [node, time]
    for t in times: 
        if t[0] not in graph: graph[t[0]] = [[t[1], t[2]]]
        else: graph[t[0]].append([t[1], t[2]])

    print('graph', graph)
    visited = {k: 0} # node: times
    def dfs(node, cTimes):
        print('node', node, 'cTimes', cTimes)
        print('visited', visited)

        if node not in graph: return 

        for neiNode, neiTime in graph[node]: 
            print('neiNode', neiNode, 'cTimes + neiTime', cTimes + neiTime)
            if neiNode not in visited or (neiNode in visited and cTimes + neiTime < visited[neiNode]):
                visited[neiNode] = cTimes + neiTime
                tTimes = dfs(neiNode, cTimes + neiTime)
                print('tTimes', tTimes, 'neiNode', neiNode)

    dfs(k, 0)
    print('visited', visited)
    if len(visited) < n: return -1 
    res = 0 
    for times in visited.values(): 
        res = max(times, res)

    return res

t1 = [[2,1,1],[2,3,1],[3,4,1]]; n1 = 4; k1 = 2 # 2
t2 = [[2,1,1],[2,3,1],[3,4,1],[3,5,2],[2,5,2]]; n2 = 5; k2 = 2 # 2
t3 = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]]; n3 = 3; k3 = 2 # 6
print('RESULT: ', networkDelayTime(t1, n1, k1))