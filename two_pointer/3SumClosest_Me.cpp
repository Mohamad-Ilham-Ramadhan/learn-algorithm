/*
   (two pointers) leetcode: 16. 3Sum Closest (medium)

   Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`.

   Return the sum of the three integers.

   You may assume that each input would have exactly one solution.



   Example 1:

      Input: nums = [-1,2,1,-4], target = 1
      Output: 2
      Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
      
   Example 2:

      Input: nums = [0,0,0], target = 1
      Output: 0
      Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
   

   Constraints:
      3 <= nums.length <= 500
      -1000 <= nums[i] <= 1000
      -10^4 <= target <= 10^4
   
   Related topics: 
      (array) (two pointers) (sorting)
   
   Solution by myself
      sort, two pointers
   leetcode submission: 
      runtime: 42 ms, beats 93.03%
      memory: 10.22 MB, beats 16.29%
*/
#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
   int threeSumClosest(vector<int>& nums, int target) {
      sort(nums.begin(), nums.end()); 
      long long total = INT_MAX; // kalo pake LLONG_MAX bisa error signed integer overflow contoh: target = -100, abs(-100 - LLONG_MAX) = LLONG_MAX + 100 (error overflow)
      long long prevN = INT_MAX; 
      long long sz = nums.size();
      for (long long i = 0; i < sz; i++) {
         long long n = nums[i];
         if (n == prevN) continue;
         long long l = i + 1;
         long long r = sz - 1;
         long long need = target - n;
         while (l < r) {
            long long sumLR = nums[l] + nums[r];
            if (sumLR == need) return target;
            if (sumLR < need) {
               l++;
            } else {
               r--; 
            }
            if( abs(target - (n+sumLR)) < abs(target - total) ) {
               total = n+sumLR;
            }
         }
      }
      return total;
   }
};



int main() {
   Solution s;
   vector<int> n1 = {-4,-1,1,2}; int t1 = 1;
   vector<int> n2 = {0,0,0}; int t2 = 1;
   vector<int> n3 = {0,1,2}; int t3 = 0;
   vector<int> n4 = {1,1,1,1}; int t4 = -100; // Line 22: Char 58: runtime error: signed integer overflow: -100 - 9223372036854775807 cannot be represented in type 'long long' (solution.cpp) SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior prog_joined.cpp:31:58
   long long total = LLONG_MAX;
   cout << total + 1;
   // cout << "Result: " << s.threeSumClosest(n4,t4) << "\n";
   return 0;
}