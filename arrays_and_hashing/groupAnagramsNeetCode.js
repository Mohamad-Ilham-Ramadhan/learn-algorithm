// Arrays & Hasing

/*
   LeetCode Group Anagrams (medium)

   Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

   An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

   Example 1:
      Input: strs = ["eat","tea","tan","ate","nat","bat"]
      Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

   Example 2:
      Input: strs = [""]
      Output: [[""]]

   Example 3:
      Input: strs = ["a"]
      Output: [["a"]]
   
   Constraints:
      - 1 <= strs.length <= 104
      - 0 <= strs[i].length <= 100
      - strs[i] consists of lowercase English letters.

   Solution converted from NeetCode: 
      mapping setiap huruf dari `s` pada sebuah array dengan length 26 yg artinya a-z 
      loop `c` pada `s` dan ++1 pada array tersebut dengan respected index (a = 0, b = 1)
      jadikan array tersebut menjadi string untuk digunakan sebagai keys dari group anagram 
      loop `strs`

   LeetCode submission:
      Runtime: 159 ms, beats 18.79%
      Memory: 54.7 MB, beats 21.51%

*/

// O(m * n) where m is the longest string.length in the `strs`
function groupAnagrams(strs) {
   let result = {};
   for (let s of strs) {
      let count = []; count.length = 26; count.fill(0,0,26); // char count of  a ... z
       
      for (let m = 0; m < s.length; m++) {
         count[s[m].charCodeAt(0) - ('a').charCodeAt(0)] += 1 // a = 0, b = 1, c = 2, d = 3 ..
      }
      if (result[count.join(' ')] === undefined) {
         result[count.join(' ')] = [s];
      } else {
         result[count.join(' ')].push(s);
      }
   }
   return Object.values(result);
}
const strs = ["eat","tea","tan","ate","nat","bat"];
const strs2 = ["",""];
const strs3 = ['', 'baso', 'soba', 'anjing', ''];
const strs4 = ["bdddddddddd","bbbbbbbbbbc"];
console.log('groupAnagrams', groupAnagrams(strs4));