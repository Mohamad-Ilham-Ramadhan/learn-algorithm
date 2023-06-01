/*
  207. Course Schedule (medium)

  There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

  For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
  Return `true` if you can finish all courses. Otherwise, return `false`.

  

  Example 1:

    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0. So it is possible.

  Example 2:

    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
  

  Constraints:
    - 1 <= numCourses <= 2000
    - 0 <= prerequisites.length <= 5000
    - prerequisites[i].length == 2
    - 0 <= ai, bi < numCourses
    - All the pairs prerequisites[i] are unique.
  
  Solution by myself:
    using dfs to detect cycle 
    if there is a cycle then false 
    true
  
  LeetCode submission:
    #1 
      - Runtime: 103 ms, beats 22.4%
      - Memory: 51.2 MB, beats 14.58%
    #2 (clear comments)
      - Runtime: 92 ms, beats 26.84%
      - Memory: 51.4 MB, beats 12.95%
    
*/

/*
I returned false for the following test case:
5
[[1,4],[2,4],[3,1],[3,2]]

and the result shows it should be true. Can someboly explain why there are only four courses (1,2,3 and 5) but we need to take 5?

    learned {
        4,
        1
        2
        3
        3
    }

    4->1->3
    |->2__^

    0-->1

    3
    [0,1][0,2][2,1]
    1->0
    v  ^
    2__|
*/

function canFinish(numCourses, prerequisites) {
   // if there is a cyclic then it must be false;
   let learned = new Set();
   let totalLearn = 0;
   let visited = new Set();
   let list = {}; // adjency list
   for (const [learn, required] of prerequisites) {
     list[learn] = list[learn] ? list[learn] : {};
     list[learn].require = list[learn].require ? list[learn].require.add(required) : (new Set()).add(required);
     list[learn].adj = list[learn].adj ? list[learn].adj : new Set();
 
     list[required] = list[required] ? list[required] : {};
     list[required].require = list[required].require ? list[required].require : new Set();
     list[required].adj = list[required].adj ? list[required].adj.add(learn) : (new Set()).add(learn);
   }
   console.log('list', list);
   /*
    [ [1,4],[2,4],[3,1],[3,2] ];
     4->1->3
     |->2__^
   */
   function dfs(learn) {
     console.log('learn', learn);
     let isCan = 0;
     visited.add(learn);
     for (let r of list[learn].require) {
       console.log('r', r);
       if (visited.has(r)) {
         // there is a cyclic
         console.log('THERE IS A CYCLIC');
         return false;
       }
       if (!learned.has(r)) {
         dfs(r);
       }
       if (learned.has(r)) {
         isCan++;
       }
     }
     visited.delete(learn);
     // console.log('isCan', isCan);
     // can learn current course
     if (isCan === list[learn].require.size) {
       console.log('learned', learn);
       totalLearn++;
       learned.add(learn);
       return true;
     }
     return false;
   }
   for (const [learn, required] of prerequisites) {
     console.log('============');
     if (!dfs(learn)) {
       return false;
     } 
   }
   console.log('total learn', totalLearn);
   // return totalLearn === numCourses ? true : false;
   return true;
 };
 const numCourses1 = 2;
 const prerequisites1 = [[1,0]]; // expect: true
 
 const numCourses2 = 2;
 const prerequisites2 = [ [0,1], [1,0]]; // expect: false
 
 const numCourses3 = 5;
 const prerequisites3 = [ [1,4],[2,4],[3,1],[3,2] ]; // expect: true
 
 const numCourses4 = 3;
 const prerequisites4 = [[1,0]]; // expect: true
 
 const numCourses5 = 1;
 const prerequisites5 = []; // expect: true 
 
 const numCourses6 = 4;
 const prerequisites6 = [[0,3],[1,0],[2,1],[0,2]]; // expect: false
 
 
 console.log('RESULT :', canFinish(numCourses1, prerequisites1));