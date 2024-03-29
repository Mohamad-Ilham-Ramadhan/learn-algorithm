"""
	(Advanced Graph) leetcode: 787. Cheapest flights Within K Stops (medium)

	Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
    
	Tags: Dynamic programming, Depth-first search, Breadth-first search, graph, Heap(Priority Queue), Shortest path

	Constraints:
        - 1 <= n <= 100
        - 0 <= flights.length <= (n * (n - 1) / 2)
        - flights[i].length == 3
        - 0 <= fromi, toi < n
        - fromi != toi
        - 1 <= pricei <= 10^4
        - There will not be any multiple flights between two cities.
        - 0 <= src, dst, k < n
        - src != dst
	======================================================================

	Submissions: 
		runtime: 92 ms, beats 97.76%
		memory: 17.44 MB, beats 89.77%
"""

from collections import deque
def findCheapestPrice(n, flights, src, dst, k):
    graph = {}
    minNodePrices = {}
    for s, d, p in flights: 
        minNodePrices[s] = float('inf')
        minNodePrices[d] = float('inf')
        if s not in graph: 
            graph[s] = [[d, p]]
        else: 
            graph[s].append([d, p])

    q = deque([[src, 0, 0]]) # node, stops, prices


    res = float('inf')
    while q: 
        node, stops, prices = q.popleft() 
        # print('res', res)
        if node not in graph: continue
        for d, p in graph[node]: 
            # print('minNodePrices[d]', minNodePrices[d])
            # print('d', d)
            if stops <= k and d == dst: 
                res = min(prices + p, res)
            elif stops < k and (prices + p < minNodePrices[d]): 
                minNodePrices[d] = prices + p
                q.append([d, stops + 1, prices + p])
    
    return -1 if res == float('inf') else res

n1 = 4; f1 = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]; s1 = 0; d1 = 3; k1 = 1 # 700
n2 = 11; f2 = [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]]; s2 = 0; d2 = 2; k2 = 4 # 11
n3 = 5; f3 = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]; s3 = 2; d3 = 1; k3 = 1
n4 = 17;
f4 = [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]] 
s4 = 13; d4 = 4; k4 = 13

n5 = 8; f5 = [[3,4,7],[6,2,2],[0,2,7],[0,1,2],[1,7,8],[4,5,2],[0,3,2],[7,0,6],[3,2,7],[1,3,10],[1,5,1],[4,1,6],[4,7,5],[5,7,10]]; s5 = 4; d5 = 3; k5 = 7
print('RESULT: ', findCheapestPrice(n4, f4, s4, d4, k4))
# print(len(f4))
