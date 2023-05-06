/*
   LeetCode: Valid Anagram (easy)

   Given two strings s and t, return true if t is an anagram of s, and false otherwise.

   An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

   Example 1:
   Input: s = "anagram", t = "nagaram"
   Output: true

   Example 2:
   Input: s = "rat", t = "car"
   Output: false
*/
/*
   Solution by NeetCode:
      #1
      Using hashmap to count the number of each character 

      Time complexity O(n)
      Space complexity O(n)

      LeetCode submission:
         Runtime: 68 ms, beats 91.59%
         Memory: 43.3 MB, beats 71.64%

      #2 
      using sort then check by equality ===

      Time complexity O(n log n)

      LeetCode submission:
         Runtime: 105 ms, beats 20.61%
         Memory: 48.4 MB, beats 16.16%
*/

function isAnagram1(s,t) {
   if (s.length !== t.length) return false;
   let sHashmap = {};
   let tHashmap = {};
   for (let i = 0; i < s.length; i++) {
      if (sHashmap[s[i]] === undefined) sHashmap[s[i]] = 1;
      sHashmap[s[i]] += 1;
      if (tHashmap[t[i]] === undefined) tHashmap[t[i]] = 1;
      tHashmap[t[i]] += 1;
   }
   // anagram check 
   for (let i = 0; i < s.length; i++) {
      if (sHashmap[s[i]] !== tHashmap[s[i]]) return false
   }
   return true;
}
const s = 'anagram'; const t = 'nagaram';
console.log('isAnagram', isAnagram1(s,t));

var isAnagram2 = function(s, t) {
   if (s.length !== t.length) return false;
   if (s.split('').sort().join('') === t.split('').sort().join('')) {
      return true;
   } else {
      return false;
   }
};