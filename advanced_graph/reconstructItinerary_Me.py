"""
	(Advanced Graph) leetcode: 332. Reconstruct itinerary  (medium)

	Link: https://leetcode.com/problems/reconstruct-itinerary/
    
	Tags: Depth-first search, Graph, Eulerian Circuit

	Constraints:
        - 1 <= tickets.length <= 300
        - tickets[i].length == 2
        - fromi.length == 3
        - toi.length == 3
        - fromi and toi consist of uppercase English letters.
        - fromi != toi
	======================================================================

	Submissions: 
        # eulerian path (Hierholzer's algorithm)
		runtime: 84 ms, beats 65.38%
		memory: 16.89 MB, beats 53.03%
"""
# fail
def findItinerary(tickets):
    adjList = {}
    # adjTo = {} # { key: current to index }
    for f, t in tickets:
        print('f', f, 't', t)
        if f in adjList:
            adjList[f].append(t)
        else: 
            adjList[f] = [t]
            # adjTo[f] = 0
    
    for key in adjList:
        adjList[key].sort()

    print('adjList', adjList)

    # smaller lexical order
    res = False
    def dfs(key, itinerary):
        # print(key, 'adj[key]', adjList[key])
        nonlocal res
        if len(itinerary) == len(tickets) + 1:
            print('itinerary', itinerary)
            if res == False: 
                res = itinerary
            return True
        
        if key in adjList:
            temp = adjList[key].copy()
            # print('temp', temp)
            for i in range(0, len(temp)):
                if res != False: return
                val = adjList[key][i]
                itinerary.append(val)
                adjList[key].pop(i)
                dfs(val, itinerary)
                itinerary.pop()
                adjList[key].insert(i, val)
    
    dfs('JFK', ['JFK'])
    return res


# Neetcode's solution (time limit exceeded)
def sol(tickets):
    adj = { src: [] for src, dst in tickets}

    tickets.sort()
    for src, dst in tickets:
        adj[src].append(dst)
    
    res = ['JFK']
    def dfs(src):
        if len(res) == len(tickets) + 1:
            return True 
        if src not in adj: 
            return False 
        
        temp = list(adj[src])
        for i, v in enumerate(temp):
            adj[src].pop(i)
            res.append(v)
            if dfs(v): return True 
            adj[src].insert(i, v)
            res.pop()

        return False
    dfs('JFK')
    return res



# need hierholzer's algorithm  
t1 = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]] # ["JFK","MUC","LHR","SFO","SJC"]

t3 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"],["SFO", "ATL"]] # ["JFK","ATL","JFK","SFO","ATL","SFO","ATL"]
t4 = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]] # ["JFK","NRT","JFK","KUL"]
t6 = [["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"]]

# print('RESULT: ', findItinerary(t6))
# print('RESULT: ', sol(t5))
# a = ["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","JFK"]
# print(''.join(a))

# Eulerian path (hierholzer's Algorithm)
def eul(tickets):
    graph = {}
    for f, t in tickets: 
        if f not in graph: graph[f] = [t]
        else: graph[f].append(t)
    
    for ts in graph.values(): 
        ts.sort(reverse=True)

    print('graph', graph)

    res = [] 
    def dfs(f):
        if f not in graph or len(graph[f]) == 0:
            res.append(f)
            return 

        while len(graph[f]):
            dfs(graph[f].pop())
        
        res.append(f)
    
    dfs('JFK')
    res.reverse()
    print('res', res)
    return res
t2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]] # ["JFK","ATL","JFK","SFO","ATL","SFO"]
t5 = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]] # ["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","JFK"]
eul(t1)
g1 = {
    1: [2,3],
    2: [2,4,4],
    3: [1,2,5],
    4: [3,6],
    5: [6],
    6: [3]
}

# eul(g1)