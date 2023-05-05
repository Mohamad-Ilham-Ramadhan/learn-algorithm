/*
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
   Solution by me:
      Using hashmap to count the number of each character 

      Time complexity O(n)
      Space complexity O(n)
*/
/*
   LeetCode submission:
      Runtime: 92 ms, beats 65%
      Memory: 48.3 MB, beats 71.64%
*/

function isAnagram(s,t) {
   if (s.length !== t.length) return false;
   let sHashmap = {};
   let tHashmap = {};
   for (let i = 0; i < s.length; i++) {
      if (sHashmap[s[i]] === undefined) sHashmap[s[i]] = 1;
      sHashmap[s[i]] += 1;
   }
   for (let i = 0; i < t.length; i++) {
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
console.log('isAnagram', isAnagram(s,t));