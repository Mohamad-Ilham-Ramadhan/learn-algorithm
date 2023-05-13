/*
   LeetCode problem: Minimum Window Substring (hard)

   Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window 
   substring
   of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string "".

   The testcases will be generated such that the answer is unique.
   

   Example 1:
      Input: s = "ADOBECODEBANC", t = "ABC"
      Output: "BANC"
      Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
   Example 2:
      Input: s = "a", t = "a"
      Output: "a"
      Explanation: The entire string s is the minimum window.
   Example 3:
      Input: s = "a", t = "aa"
      Output: ""
      Explanation: Both 'a's from t must be included in the window.
      Since the largest window of s only has one 'a', return empty string.
   

   Constraints:
      - m == s.length
      - n == t.length
      - 1 <= m, n <= 105
      - s and t consist of uppercase and lowercase English letters.

   Solution By NeetCode: https://www.youtube.com/watch?v=jSto0O4AJbM

   LeetCode submission:
      Runtime: 127 ms, beats 23.68%
      Memory: 47.9 MB, beats 37.73%
*/



function minimumWindowSubstring(s, t) {
   if (t === '') return '';

   const countT = {}; const window = {};

   for (let c of t) {
      countT[c] = countT[c] === undefined ? 1 : countT[c] + 1;
   }

   let have = 0; let need = Object.keys(countT).length;
   let res = [-1, -1]; let resLen = Infinity;
   let l = 0;
   // return ;
   for (let r = 0; r < s.length; r++) {
      const c = s[r];
      window[c] = window[c] === undefined ? 1 : window[c] + 1;
      console.log('c', c, Object.assign({}, window))
      if (c in countT && window[c] === countT[c]) {
         have++;
      }
      console.log('have', have);
      while (have === need) {
         console.log('have === need');
         // update our result
         if ((r - l + 1) < resLen) {
            console.log('update resLen');
            res = [l, r];
            resLen = (r - l) + 1;
         }
         // pop from the left of our window
         window[s[l]] -= 1
         if (s[l] in countT && window[s[l]] < countT[s[l]]) have--;
         l++;
         console.log('new l', l);
      }
      console.log('res', res, 'resLen', resLen);
   }
   [l, r] = res;
   if (resLen !== Infinity) {
      return s.slice(l, r + 1);
   } else {
      return '';
   }
}
const s = 'XZADOBECODEBANC'; const t = 'ABC'; // BANC
const s1 = 'ADOBECODEBANC'; const t1 = 'ABC'; // BANC
const s2 = 'a'; const t2 = 'a'; // a
const s3 = 'a'; const t3 = 'aa'; // ''
const s4 = 'xaybycabcxxba'; const t4 = 'abc'; // cab
const s5 = 'aayxbxcca'; const t5 = 'abc'; // bxcca
const s6 = 'aa'; const t6 = 'aa'; // aa
const s7 = 'bdabxfa'; const t7 = 'ab'; // bda
console.log('RESULT', minimumWindowSubstring(s3, t3));
