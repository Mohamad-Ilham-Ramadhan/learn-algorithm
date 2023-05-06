// Arrays & Hasing

/*
   LeetCode Group Anagrams

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

   LeetCode test:
      Runtime: 2066 ms, beats 5.1%
      Memory: 107.4 MB, Beats 5.4%
*/

// O(n^2)
function groupAnagrams(strs) {
   const result = [];
   const resultContainer = {}; // anagrams container to check matching with 

   for (let i = 0; i < strs.length; i++) {
      const word = strs[i];
      const hashmap = {}
      if (word.length === 0) { 
         hashmap[''] = 1;
      } else {
         for (let j = 0; j < word.length; j++) {
            const char = word[j];
            console.log('char', char);
            if (hashmap[char] === undefined){ 
               hashmap[char] = 1;
            } else {
               hashmap[char] += 1;
            }
         }
      }
      // if grup is empty (initial loop), then push a new group
      if (result.length === 0) {
         result.push([word]);
         resultContainer[0] = {hashmap, length: word.length};
         continue;
      } 
      // check current anagram with the group anagrams that collected
      // iterate each group
      let isAnagram = false;
      for (let x = 0; x < result.length; x++) {
         const {hashmap: hashmapContainer, length: lengthContainer} = resultContainer[x];

         if (word === '') {
            if (hashmap[''] === hashmapContainer['']) {
               isAnagram = true;
               result[x].push(word);
               break;
            } else {
               continue;
            }
         }

         
         // check current anagram with in result anagram
         if (lengthContainer !== word.length) continue;
         for (let y = 0; y < word.length; y++) {
            if (hashmap[word[y]] !== hashmapContainer[word[y]]) {
               isAnagram = false; break;
            } else {
               isAnagram = true;
            }
         }
         if (isAnagram) {
            result[x].push(word);
            break;
         }
      }
      // push to the new group is no match anagram
      if (isAnagram === false) {
         result.push([word]);
         resultContainer[result.length - 1] = {hashmap, length: word.length};
      }
   }
   return result;
}
const strs = ["eat","tea","tan","ate","nat","bat"];
const strs2 = ["",""];
const strs3 = ['', 'baso', 'soba', 'anjing'];
console.log('groupAnagrams', groupAnagrams(strs3));