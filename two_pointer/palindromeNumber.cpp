/*
   (two pointer): 9. Palindrome Number (easy)

   Given an integer x, return true if x is a palindrome, and false otherwise.

 

   Example 1:
      Input: x = 121
      Output: true
      Explanation: 121 reads as 121 from left to right and from right to left.

   Example 2:
      Input: x = -121
      Output: false
      Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

   Example 3:
      Input: x = 10
      Output: false
      Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
   

   Constraints:
      -231 <= x <= 231 - 1

   Follow up: Could you solve it without converting the integer to a string?

   ========================================================================================

   Solution by myself: 
      #1
         - convert x to string then check it
      #2 
         - same with #1 but
         - if x negative then return false


   Leetcode submission: 
      #1
         runtime: 15 ms, beats 64.28%
         memory: 5.96 MB, beats 41.09%
      #2
         runtime: 21 ms, beats 28.71%
         memory: 5.96 MB, beats 41.09%

*/

#include <iostream>
#include <cmath>
using namespace std;
class Solution {
public:
   bool isPalindrome(int x) {
      if (x < 0) {return false;} // #2
      string xs = to_string(x); 

      int l;
      int r; 
      int mid = floor(xs.length() / 2);
      if (xs.length() % 2) { // odd
         l = r = mid;
      } else { // even
         r = mid; 
         l = mid - 1;
      }
      cout << "l: " << l << " r: " << r << "\n";
      while (l >= 0 && r < xs.length()) {
         cout << "xs[l]: " << xs[l] << " xs[r]: " << xs[r] << "\n";
         if (xs[l] != xs[r]) {
            return false;
         }
         l--;
         r++;
      }
      return true;
   }
};

int main() {
   Solution s = Solution(); 

   cout << "RESULT : " << s.isPalindrome(10);

   return 0;
}