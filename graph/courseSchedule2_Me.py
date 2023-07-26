'''
   (graph) leetcode: 210. Course Schedule II (medium)

   There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

      - For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

   Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.


   Example 1:
      Input: numCourses = 2, prerequisites = [[1,0]]
      Output: [0,1]
      Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

   Example 2:
      Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
      Output: [0,2,1,3]
      Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
      So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
   
   Example 3:
      Input: numCourses = 1, prerequisites = []
      Output: [0]

   Constraints:
      - 1 <= numCourses <= 2000
      - 0 <= prerequisites.length <= numCourses * (numCourses - 1)
      - prerequisites[i].length == 2
      - 0 <= ai, bi < numCourses
      - ai != bi
      - All the pairs [ai, bi] are distinct.
   
   Related Topics: 
      (depth-first search) (breadth-first search) (graph) (topological sort)
      
   =========================================================================== 

   Solution by myself 
      create graph (adjency list)
      depth first search the graph
      create needs for each nodes (course) before take specific course : index as node and value as its needs. 
      track total Needs if after traversing graph total needs still 0 then there is a cycle so return an empty list.

   Leetcode submission:
      runtime: 113 ms, beats 74.80%
      memory: 17.99 MB, beats 73.12%
'''

def findOrder(numCourses, prerequisites): 
   pass

'''
   Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
   Output: [0,2,1,3]
   Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
   So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

   0: [1,2,3]

   [[1,0],[2,0],[3,1],[3,2]] n = 4

   graph {
      0: [1,2],
      1: [3],
      2: [3],
   }

   0->1
   |->2

   p4 = [[3,5],[4,5],[0,2],[7,8],[4,9],[5,8],[1,9]]; n4 = 10 # [9,8,7,6,5,4,3,2,1,0] # coba urutan edges nya diubah

   needs {
      5: 0,
      3: 0,
      1: 0, 
      4: 0,
      0: 0,
      7: 0,
   }
   graph {
      5: [3,4]
      2: [0]
      8: [7,5]
      9: [4,1]
   }
   cur = 
   queue = []
   res = 
   [2,0,8,7,5,3,9,4,1,6] # betul
   [8,5,7,3,9,1,4,2,0] # betul
   [8,5,9,2,3,1,0,7,4,6] # betul
   8->5->3

      7--v
   3->5->8
   4--^
   |--v
   1->9
   0->2

   [2,9,2,5,9,8,6,8,8,9]
   [0,1,2,3,4,5,6,7,8,9]

   p5 = [[1,0], [1,3], [0,3], [3,1]]; n5 = 4 # []

   graph {
      0: [1,3],
      3: [1],
      1: [3]
   }

   p6 = [[1,0], [1,3], [0,3]]; n6 = 4 # [3,2,0,1]

   p7 = [[1,0], [2,1], [3,2]] n7 = 4

   needs {
      1: 0,
      2: 0,
      3: 0,
      0: 0,
   }
   graph {
      0: [1]
      1: [2]
      2: [3]
      3: [0]
   }
   cur = 
   queue = []
   res = [0,1,2,3]
   [] # betul
'''

from collections import deque;
def findOrder(numCourses, prerequisites):
   needs = [0 for i in range(numCourses)] # index as course, value as course prerequisites
   totalNeeds = 0;
   graph = {}
   s = set() # required course
   for n1, n2 in prerequisites:
      needs[n1] += 1
      totalNeeds += 1
      s.add(n1); s.add(n2)
      if n2 in graph: 
         graph[n2].append(n1)
      else: 
         graph[n2] = [n1]
   
   result = []

   for i in range(numCourses): 
      if i not in s: 
         result.append(i)
   
   # print('s', s)
   # print('needs', needs, 'totalNeeds', totalNeeds)
   # print('graph', graph)

   # depth-first search
   q = deque()
   added = set()
   for key in graph.keys(): 
      q.append(key)
      while len(q): 
         # print('queue copy', q.copy())
         cur = q.popleft()
         # print('cur', cur)
         if needs[cur] <= 0 and cur not in added: 
            result.append(cur)
            added.add(cur)
         else: 
            continue
         if cur not in graph: continue
         for nextCourse in graph[cur]: 
            # print('nextCourse', nextCourse)
            q.append(nextCourse)
            needs[nextCourse] -= 1 # because cur (their prerequisite) has learned
            totalNeeds -= 1

   # print('totalNeeds after', totalNeeds)
   # print('result before last', result.copy())
   if totalNeeds == 0:
      return result
   else: 
      return []
   # 3.998.000

p1 = [[1,0],[2,0],[3,1],[3,2]]; n1 = 4
p3 = []; n3 = 1
p4 = [[3,5],[4,5],[0,2],[7,8],[4,9],[5,8],[1,9]]; n4 = 10
p5 = [[1,0], [2,1], [3,2], [0,3]]; n5 = 4 # [], cycle
print('result: ', findOrder(n1, p1))
'''
needs [1, 1, 0, 1, 2, 1, 0, 1, 0, 0]
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
graph {
   5: [3, 4], 
   2: [0], 
   8: [7, 5], 
   9: [4, 1]
}

'''