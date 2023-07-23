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

   solution by NeetCode
      using union find with path compression

leetcode submission
      runtime: 13 ms, beats 28.25%
      memory:  9.16 MB, beats 31.92%
*/

// Definition for singly-linked list.
#include <bits/stdc++.h>
using namespace std;

// # union find
class Solution
{
private: 
   vector<int> par; 
   vector<int> rank;
   int find(int n) {
      int p = par[n];
      while (p != par[p]) {
         par[p] = par[par[p]];
         p = par[p];
      }
      return p;
   };
   bool uni(int n1, int n2) { // union
      int p1 = find(n1);
      int p2 = find(n2);

      if (p1 == p2) return false; // cycle

      if (rank[p1] > rank[p2]) {
         par[p2] = p1;
         rank[p1] += rank[p2];
      } else {
         par[p1] = p2;
         rank[p2] += rank[p1];
      }
      return true;
   }
public:
   vector<int> findRedundantConnection(vector<vector<int>> &edges)
   {
      
      for (int i = 0; i <= edges.size(); i++) {
         par.push_back(i);
         rank.push_back(1);
      }


      for (vector<int> edge : edges) {
         
         if (!uni(edge[0], edge[1])) {
            return {edge[0], edge[1]};
         }
      }
      return {0, 0};
   }
};

int main()
{
   vector<vector<int>> e2 = {{1,2},{2,3},{3,4},{1,4},{1,5}};
   Solution s;
   vector<int> result = s.findRedundantConnection(e2);
   cout << " r1 " << result[0] << " r2 " << result[1];

   // vector<int> par; 
   // for (int i = 0; i <= e2.size(); i++) {
   //    par.push_back(i);
   // }
   // for (auto x : par) {
   //    cout << " x " << x << "\n";
   // }
   return 0;
}