/*
   LeetCode problem: Longest Repeating Character Replacement (medium)

   You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

   Return the length of the longest substring containing the same letter you can get after performing the above operations.
   
   Example 1:
      Input: s = "ABAB", k = 2
      Output: 4
      Explanation: Replace the two 'A's with two 'B's or vice versa.

   Example 2:
      Input: s = "AABABBA", k = 1
      Output: 4
      Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
      The substring "BBBB" has the longest repeating letters, which is 4.
      There may exists other ways to achive this answer too.

   Constraints:
      - 1 <= s.length <= 105
      - s consists of only uppercase English letters.
      - 0 <= k <= s.length

   Solution by Myself:
      using hash map to store the counts of each character from left pointer to right pointer (window)
      and we count the substring (window) length for result;
      if kCount (limit number that we can change any character between those characters) exceeds `k` 
      we substract total characters in that window with the dominant or the most char many count.
      For example:
      'ABBCBBC' and k = 2. When left pointer is 0 (A) and right is 6 (C) 
      the hash map is {
         A: 1
         B: 4
         C: 2
      }
      so it will be 7 - 4 = 3, 3 > 2(k). So we will move left pointer to right and calculate the kCount again. until <= k
      'BBCBBC' {
         B: 4
         C: 2
      } 4 - 2 = 2, it pass, and substring.length is 6
   LeetCode submission:
      #1
      Runtime: 109 ms, beats 30.99%
      Memory: 50.7 MB, beats 5.19%
*/

function longestRepeatingCharacterReplacement(s, k) {
   console.log(s.split(''));
   let result = 0;
   let map = new Map();
   let kCount = 0; // replacement count
   let dominant = ''; // the most frequent chars
   let l = 0; // the left pointer
   let longest = 0;
   for (let r = 0; r < s.length; r++) {

      if (map.has(s[r])) {
         map.set(s[r], map.get(s[r]) + 1);
         longest++;
         if (map.get(s[r]) > map.get(dominant)) {
            dominant = s[r];
         }
      } else {
         if (map.size === 0) {
            dominant = s[r];
         } 
         map.set(s[r], 1);
         longest++;
      }

      if (s[r] !== dominant) {
         kCount++;
      }
      // reset the count and 
      while (kCount > k) {
         // console.log('batas', r, s[r], 'dominant before', dominant);
         const deletedChar = s[l];
         console.log();
         map.set(deletedChar, map.get(deletedChar) - 1);
         let dominantCount = 0;
         let totalChar = 0;
         for (let [char, count] of map) { 
            if (count > dominantCount) {
               dominantCount = count;
               dominant = char;
            }
            totalChar += count;
         }
         // console.log('batas', r, s[r], 'dominant after', dominant);
         console.log('l', l, 'r',r,'deleted char', deletedChar,'map', new Map(map), 'dominant after', dominant, 'kCount', kCount, 'longest', longest);
         // console.log('totalChar - dominantCount = kCount', totalChar, dominantCount, totalChar - dominantCount);
         kCount = totalChar - dominantCount;
         l++;
         longest--;
      }
      console.log('save longest', longest, 'l', l, 'r', r, 'map', new Map(map));
      result = Math.max(result, longest);
      // console.log('l',l,'r', r, 'map', map, 'kCount', kCount);
   }
   return result;
}
const s1 = 'ABAB'; const k1 = 2; // 4
const s2 = 'AABABBA'; const k2 = 1; // 4
const s3 = 'AABCABABBBCBBA'; const k3 = 2; // 8 (BABBBCBB -> BBBBBBBB)
const s4 = 'AAB'; const k4 = 1; // 3
const s5 = 'ABBBCBCBB'; const k5 = 2; // 8
const s6 = 'AAAAABBBBCBB'; const k6 = 4; // 10
const s7 = 'KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF'; const k7 = 4;
console.log(longestRepeatingCharacterReplacement('ABBB', 2));


// function longestRepeatingCharacterReplacement(s, k) {
//    let result = 0;
//    let l = 0; 
//    let substr = '';
//    let kCount = 0; // replacement count
//    for (let r = 0; r < s.length; r++) {
//       console.log('s[l]', s[l], 's[r]', s[r], 'kCount', kCount);
//       if (s[r] !== substr[0] && substr.length > 0) {
//          kCount++;
//          if (s[l] === substr[0]) {
//             l = r; // let l to the next substring when kCount greater than k
//          }
//       }
//       if (kCount > k) {
//          substr = s[l];
//          r = l;
//          kCount = 0;
//          continue;
//       }
//       substr += s[r];
//       result = Math.max(result, substr.length);
//       console.log('substr', substr);
//    }
//    return result;
// }