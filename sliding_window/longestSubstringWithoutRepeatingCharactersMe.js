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

   LeetCode submissions:
      #1 
      Runtime: 88 ms, beats 61.38%
      Memory: 49.4 MB, beats 19.12%
      #2
      Runtime: 97 ms, beats 45.19%
      Memory: 47.8 MB, beats 49.40%
*/

function longestSubstringWithoutRepeatingCharacters(s) {
   if (s === '') return 0;
   if (s.length === 1) return 1;
   let result = 1; // longest substring
   let l = 1;
   let count = 1; // current length of substring
   let map = new Map(); // for index of char 
   map.set(s[0], 0);
   for (let r = 1; r < s.length; r++) {
      console.log(s[r]);
      console.log('map', new Map(map));
      if (!map.has(s[r])) {
         map.set(s[r], r);
         count++;
         result = Math.max(count, result);
      } else {
         for (let [c,i] of map) {
            count--;
            map.delete(c);
            if (c === s[r]) {
               map.set(s[r], r);
               count++;
               break;
            }
         }
         // console.log(map);
      }
   }
   return result;
}
const s1 = 'abcabcxbb'; // 4
const s2 = 'abcabcxy'; // 5
const s3 = 'bbbbb'; // 1
const s4 = 'pwwkew'; // 3
const s5 = ''; // 0;
// const res = longestSubstringWithoutRepeatingCharacters('    xa _-');
// console.log(res);
console.log(attempt2(s5));
function attempt2(s) {
   if (s === '') return 0;
   if (s.length === 1) return 1;
   let result = 1; // longest substring
   // let l = 1;
   // let count = 1; // current length of substring
   let subs = ''; // current substring
   subs += s[0];
   for (let r = 1; r < s.length; r++) {
      if (subs.includes(s[r])) {
         const del = subs.indexOf(s[r]) + 1;
         subs = subs.slice(del);
      }
      subs += s[r];
      console.log(subs);
      result = Math.max(result, subs.length);
   }
   return result;
}