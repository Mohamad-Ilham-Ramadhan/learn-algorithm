/*
   LeetCode problem: Container With Most Water (medium)

   You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

   Find two lines that together with the x-axis form a container, such that the container contains the most water.

   Return the maximum amount of water a container can store.

   Notice that you may not slant the container.

   

   Example 1:
      8 - |    ||             ||
      7 - |    ||-------------||----||
      6 - |    || ||          ||    ||
      5 - |    || ||    ||    ||    ||
      4 - |    || ||    || || ||    ||
      3 - |    || ||    || || || || ||
      2 - |    || || || || || || || ||
      1 - | || || || || || || || || ||
      0----------------------------------------------------------
             1  2  3  4  5  6  7  8  9
      Input: height = [1,8,6,2,5,4,8,3,7]
      Output: 49 --> horizontal-diff (9-2) * vertical Math.min(8,7) = 49
      Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

   Example 2:
      Input: height = [1,1]
      Output: 1

   Constraints:

   n == height.length
   2 <= n <= 105
   0 <= height[i] <= 104

   LeetCode submission (attempt 1):
      Runtime: 83 ms, beats 28.69%
      Memory: 49.39 MB, beats 91.49%;

      #Optimize (shorting)
      Runtime: 77 ms, beats 56.16%
      Memory: 49.39 MB, beats 74.99%;

      #Optimize (shorting)
      Runtime: 83 ms, beats 28.69%
      Memory: 49.6 MB, beats 74.99%;

   Time Complexity: O(n)
*/

function containerMostWater(height) {
   let result = 0;
   let l = 0;
   let r = height.length - 1;
   while (l < r) {
      let distance = r - l;
      let shortest = Math.min(height[l], height[r])
      let currentWater = shortest * distance;
      result = Math.max(result, currentWater);
      if (shortest === height[l]) {
         l++;
      } else if (shortest === height[r]) {
         r--;
      }
   }
   return result;
}
const height1 = [1,8,6,2,5,4,8,3,7];
const height2 = [1, 8, 6, 2, 100, 100, 8, 3, 7];
const height3 = [1,1];
const height4 = [100, 8, 6, 2, 100, 200, 8, 3, 100];
console.log('result', uglify(height4));
// [1, 8, 6, 2, 100, 100, 8, 3, 7] = length = 8

// dis = 2
// result = 100;

function containerMostWaterOptimize(height) {
   let result = 0;
   let l = 0;
   let r = height.length - 1;
   while (l < r) {
      result = Math.max(result, Math.min(height[l], height[r]) * (r - l));
      if (height[l] < height[r]) {
         l++;
      } else {
         r--;
      }
   }
   return result;
}
function uglified(t){let n=0,e=0,a=t.length-1;for(;e<a;)n=Math.max(n,Math.min(t[e],t[a])*(a-e)),t[e]<t[a]?e++:a--;return n}

// top #1 solution for inspiration of optimized version
var maxArea = function(height) {
   var max = 0;
   var left = 0;
   var right = height.length -1;

   while(left <= right) {
       max = Math.max(max, (right-left)*Math.min(height[left], height[right]));
       if (height[left] < height[right]) {
           left++;
       } else {
           right--;
       }
   }
   return max;
}