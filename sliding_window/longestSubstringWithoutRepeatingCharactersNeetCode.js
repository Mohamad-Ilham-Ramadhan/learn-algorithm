/*
   LeetCode problem: Longest Substring Without Repeating Characters (medium)

   Given a string s, find the length of the longest 
   substring
   without repeating characters.


   Example 1:
      Input: s = "abcabcbb"
      Output: 3
      Explanation: The answer is "abc", with the length of 3.

   Example 2:
      Input: s = "bbbbb"
      Output: 1
      Explanation: The answer is "b", with the length of 1.

   Example 3:
      Input: s = "pwwkew"
      Output: 3
      Explanation: The answer is "wke", with the length of 3.
      Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

   Constraints:

   0 <= s.length <= 5 * 104
   s consists of English letters, digits, symbols and spaces.

   Solution by NeetCode
   
   LeetCode submissions:
      Runtime: 83 ms, beats 73.24%
      Memory: 46.4 MB, beats 81.6%
*/

function longestSubstringWithoutRepeatingCharacters(s) {
   let charSet = new Set();
   let l = 0;
   let res = 0;
   for (let r = 0; r < s.length; r++) {
      while (charSet.has(s[r])) {
         charSet.delete(s[l]);
         l++;
      }
      charSet.add(s[r]);
      res = Math.max(res, r - l + 1);
   }
   return res;
}
const s1 = 'abcabcxbb'; // 4
const s2 = 'abcabcxy'; // 5
const s3 = 'bbbbb'; // 1
const s4 = 'pwwkew'; // 3
const s5 = ''; // 0;
console.log(longestSubstringWithoutRepeatingCharacters(s5));
