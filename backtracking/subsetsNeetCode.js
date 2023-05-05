// Backtracking algorithm/technique

// Subsets from LeetCode.

/*
   Given an integer array `nums` of unique elements, return all possible subsets (the power set).

   The solution set must not contain duplicate subsets. Return the solution in any order.

   Example 1:
      Input: nums = [1,2,3]
      Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

   Example 2:
      Input: nums = [0]
      Output: [[],[0]]
   
   Constraints:
      1 <= nums.length <= 10
      -10 <= nums[i] <= 10
      All the numbers of nums are unique.

   Solution Idea by NeetCode: https://www.youtube.com/watch?v=REOH22Xwdkk

      [1,2,3]
      1     2     3
      /\   /\     /\
    [1][] [2][] [3][]

    2 * 2 * 2 = 8 Or 2^n   2 pangkat length of `nums`
    [1][] * [2][] * [3][] = 
    DFS:
                         root
                   1/            \[]
               [1]                 []
          2/       \[]          2/     \[] 
        [1,2]      [1]         [2]     []
      3/    \[]   3/  \[]    3/  \[]  3/ \[]
   [1,2,3] [1,2] [1,3] [1] [2,3] [2] [3] []

   LeetCode submition:
      Runtime: 61ms, beats 70.69%
      Memory: 42.5MB, beats 97.21%
*/

function subsets(nums) {
   let result = [];
   let subset = [];
   function dfs(i) {
      if (i >= nums.length) {
         result.push(subset.slice());
         return;
      }
      // Decision to include nums[i]
      subset.push(nums[i]);
      dfs(i + 1);
      // Decision NOT to include nums[i]
      subset.pop();
      dfs(i + 1);
   }
   dfs(0);
   return result;
}

const nums = [1, 2, 3];
console.log('subsets:', subsets([3, 2, 4, 1]));
