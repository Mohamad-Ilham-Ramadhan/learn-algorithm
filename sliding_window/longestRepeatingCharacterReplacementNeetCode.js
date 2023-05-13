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

   Solution by NeetCode
   
   LeetCode submission:
      Runtime: 408 ms, beats 12.25%
      Memory: 48.8 MB, beats 13.99%
*/

function longestRepeatingCharacterReplacement(s, k) {
   let count = {};
   let res = 0;

   let l = 0;
   for (let r = 0; r < s.length; r++) { 
      count[s[r]] = count[s[r]] === undefined ? 1 : 1 + count[s[r]];

      while ( (r - l + 1) - Math.max(...Object.values(count)) > k) {
         count[s[l]] -= 1;
         l++;
      }

      res = Math.max(res, r - l + 1); // r - l + 1 is the size of window (substring)
   }
   return res;
}

const s1 = 'ABAB'; const k1 = 2; // 4
const s2 = 'AABABBA'; const k2 = 1; // 4
const s3 = 'AABCABABBBCBBA'; const k3 = 2; // 8 (BABBBCBB -> BBBBBBBB)
const s4 = 'AAB'; const k4 = 1; // 3
const s5 = 'ABBBCBCBB'; const k5 = 2; // 8
const s6 = 'AAAAABBBBCBB'; const k6 = 4; // 10
const s7 = 'KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF'; const k7 = 4;
console.log(longestRepeatingCharacterReplacement(s7, k7));