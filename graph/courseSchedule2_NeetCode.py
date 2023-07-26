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

   Solution by NeetCode

   Leetcode submission:
      runtime: 103 ms, beats 97.36%
      memory: 19.45 MB, beats 38.67%
'''

def findOrder(numCourses, prerequisites): 
   # builds adjacency list of prereqs
   prereq = {c: [] for c in range(numCourses)}
   for crs, pre in prerequisites:
      prereq[crs].append(pre)
   # a course has 3 possible state:
      # visited -> course has been added to output
      # visiting -> course not added to output but added to cycle
      # unvisitted -> course not added to output or cycle
   output = []
   visit, cycle = set(), set() 
   def dfs(crs): 
      if crs in cycle: return False
      if crs in visit: return True

      cycle.add(crs)
      for pre in prereq[crs]:
         if dfs(pre) == False: return False

      cycle.remove(crs)
      visit.add(crs)
      output.add(crs)
      return True 
   
   for c in range(numCourses):
      if dfs(c) == False: return False 
   return output

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