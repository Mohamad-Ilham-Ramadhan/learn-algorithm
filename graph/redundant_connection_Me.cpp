/*
   (graph) leetcode: 684. Redundant Connection (medium)

   In this problem, a tree is an undirected graph that is connected and has no cycles.

   You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two different vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges` of length `n` where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the graph.

   Return an edge that can be removed so that the resulting graph is a tree of `n` nodes. If there are multiple answers, return the answer that occurs last in the input.



   Example 1:
      1---2
      | /
      3

      Input: edges = [[1,2],[1,3],[2,3]]
      Output: [2,3]

   Example 2:
      2---1---5
      |   |
      3---4

      Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
      Output: [1,4]


   Constraints:
      - n == edges.length
      - 3 <= n <= 1000
      - edges[i].length == 2
      - 1 <= ai < bi <= edges.length
      - ai != bi
      - There are no repeated edges.
      - The given graph is connected.

   Related Topics:
      (Depth-first search) (Breadth-first search) (Union find) (Graph)

   ===================================================================

   solution by myself
      using union find with path compression

leetcode submission
      runtime: 8 ms, beats 73.40%
      memory:  10.27 MB, beats 16.03%
*/

// Definition for singly-linked list.
#include <bits/stdc++.h>
using namespace std;

// # union find
class Solution
{
public:
   vector<int> findRedundantConnection(vector<vector<int>> &edges)
   {
      int n = 0; // max node number
      for (auto edge : edges) {
         n = max(n, edge[0]);
         n = max(n, edge[1]);
      }

      // init parent each node is parent for itself,
      // graph: { parent: [child...]}
      vector<int> parent;
      unordered_map<int, vector<int>> graph; 
      for (int i = 0; i <= n; i++) {
         parent.push_back(i); 
         graph[i] = {};
      }
      
      // union find with path compression
      vector<int> result;
      for (auto edge : edges) {
         int n1Parent = parent[edge[0]];
         int n2Parent = parent[edge[1]];
         cout << "e1 " << edge[0] << ", e2 " << edge[1] << "\n";
         cout << " parent1 " << n1Parent << ", parent2 " << n2Parent << "\n";
         if (n1Parent == n2Parent) {
            cout << "CYCLE" << "\n";
            result = {edge[0], edge[1]};
            continue;
         }

         if ( graph[n1Parent].size() + 1 > graph[n2Parent].size() + 1) {
            graph[n1Parent].push_back(n2Parent); 
            for (auto child : graph[n2Parent]) {
               graph[n1Parent].push_back(child);
               parent[child] = n1Parent; 
            }
            parent[n2Parent] = n1Parent;
            graph[n2Parent] = {};
         } else {
            graph[n2Parent].push_back(n1Parent); 
            for (auto child : graph[n1Parent]) {
               graph[n2Parent].push_back(child);
               parent[child] = n2Parent; 
            }
            parent[n1Parent] = n2Parent;
            graph[n1Parent] = {};
         }
      }
      return result;
   }
};

int main()
{
   vector<vector<int>> e2 = {{1,2},{2,3},{3,4},{1,4},{1,5}};
   Solution s;
   vector<int> result = s.findRedundantConnection(e2);
   cout << " r1 " << result[0] << " r2 " << result[1];
   return 0;
}