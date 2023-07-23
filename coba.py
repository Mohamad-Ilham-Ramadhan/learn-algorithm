# Python Program for union-find algorithm
# to detect cycle in a undirected graph
# we have one edge for any two vertex
# i.e 1-2 is either 1-2 or 2-1 but not both

from collections import defaultdict

# This class represents a undirected graph
# using adjacency list representation


class Graph:

	def __init__(self, vertices):
		self.V = vertices # No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# A utility function to find the subset of an element i
	def find_parent(self, parent, i):
		if parent[i] == i:
			return i
		if parent[i] != i:
			return self.find_parent(parent, parent[i])

	# A utility function to do union of two subsets
	def union(self, parent, x, y):
		parent[x] = y

	# The main function to check whether a given graph
	# contains cycle or not

	def isCyclic(self):

		# Allocate memory for creating V subsets and
		# Initialize all subsets as single element sets
		parent = [0]*(self.V)
		for i in range(self.V):
			parent[i] = i

		# Iterate through all edges of graph, find subset of both
		# vertices of every edge, if both subsets are same, then
		# there is cycle in graph.
		for i in self.graph:
			for j in self.graph[i]:
				x = self.find_parent(parent, i)
				y = self.find_parent(parent, j)
				if x == y:
					return True
				self.union(parent, x, y)


# Create a graph given in the above diagram
g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)

'''
    graph {
        0: [1],
        1: [2],
        2: [0],
    }
    parent = [2,2,2]
    0->1->2
'''

# if g.isCyclic():
# 	print("Graph contains cycle")
# else:
# 	print("Graph does not contain cycle ")

# This code is contributed by Neelam Yadav
# parent = [0] * 3;
# for i in range(3):
# 			parent[i] = i
# print('parent', parent)


'''
	1: [0,2],

'''

'''
e2 = [[20,24],[3,17],[17,20],[8,15],[14,17],[6,17],[15,23],[6,8],[15,19],[16,22],[7,9],[8,22],[2,4],[4,11],[22,25],[6,24],[13,19],[15,18],[1,9],[4,9],[4,19],[5,10],[4,21],[4,12],[5,6]] # [6,24]

parent = [None, 24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24]
         [None, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
graph {
   24: [20,17,3,14,6,8,15,23,19,22,16,25,13,18,9,7,1,4,2,11,12,10,5],
   17: [3] ###
   20: [], ###
   15: [8,23] ###
   22: [16], ###
   9: [7,1,4], ###
   4: [2,11], ###
   10: [5] ###
}
result = [6,4]

e2 = [[1,2],[2,3],[3,4],[1,4],[1,5]] # [1,4]


parent [None, 4,4,4,4,5]
graph {
   2: [1] ###
   3: [2,1] ### 
   4: [3,2,1],
}
result = [1,4]
'''

def findRedundantConnection(edges): 
   par = [i for i in range(len(edges) + 1)] # parent
   rank = [1] * (len(edges) + 1)
   
   def find(n): 
      p = par[n]
      while p != par[p]: # path compression
         par[p] = par[par[p]]
         p = par[p]
      return p 

   # return False if can't complete 
   def union(n1, n2): 
      p1, p2 = find(n1), find(n2)

      if p1 == p2: # cycle
         return False
      
      if rank[p1] > rank[p2]:
         par[p2] = p1 
         rank[p1] += rank[p2]
      else: 
         par[p1] = p2 
         rank[p2] += rank[p1]
      return True
   
   for n1, n2 in edges: 
      if not union(n1, n2): 
         return [n1, n2]
         

# print('n', n, 'parent', parent, 'graph', graph)

e2 = [[1,2],[2,3],[3,4],[1,4],[1,5]]

e3 = [[20,24],[3,17],[17,20],[8,15],[14,17],[6,17],[15,23],[6,8],[15,19],[16,22],[7,9],[8,22],[2,4],[4,11],[22,25],[6,24],[13,19],[15,18],[1,9],[4,9],[4,19],[5,10],[4,21],[4,12],[5,6]] 
print('RESULT: ', findRedundantConnection(e3))

