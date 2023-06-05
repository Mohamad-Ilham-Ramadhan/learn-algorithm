/*
  Leetcode: 5. Longest Palindromic Substring (medium)

  Given a string s, return the longest palindromic substring in s.


  Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

  Example 2:
    Input: s = "cbbd"
    Output: "bb"
  

  Constraints:
    - 1 <= s.length <= 1000
    - s consist of only digits and English letters.

  Solution by myself:
    using two pointer 

  Leetcode submission:
    #1
      Runtime: 600 ms, beats 29.38%
      Memory: 47.8 MB, beats 46.31%
    #2 (break the loop when j === s.length -1 when palindrome found)
      Runtime: 518 ms, beats 33.48%
      Memory: 47.9 MB, beats 43.97%
    #3 (set variable minJ to store min j index when palindrome found, the is j is <= minJ then reset continue)
      Runtime: 535 ms, beats 32.25%
      Memory: 47.5 MB, beats 47.54%
    #4 if substr.length < result.length reset continue
        if substr.length < result.length && j === s.length - 1 break
      Runtime: 445 ms, beats 37.15%
      Memory: 47.9 MB, beats 43.97%
      
*/

function longestPalindrome(s) {
   if (s.length === 1) return s;

   function isPalindrome(str) {
      let j = str.length - 1;
      for (let i = 0; i < Math.floor(str.length / 2); i++) {

         if (str[i] !== str[j]) {
            return false;
         }
         if (j < i) {
            // reach mid
            break;
         }
         j--;
      }
      return true;
   }

   // let possible = []; // possible string tobe palindrome
   // let 
   let result = '';
   let j = s.length - 1;
   let minJ = 0; // min j index when new palindrom length > result length
   let i = 0;
   x = 0;
   while (i < s.length) {
      console.log(s.slice(i, j + 1), i, j);
      const substr = s.slice(i, j + 1);
      // #4 [start]
      if (substr.length <= result.length || j < i || j <= minJ) {
         if (j === s.length - 1) break;
         console.log('reset');
         i++;
         j = s.length - 1;
         continue;
      }
      // #4 [end]

      // #3 [start]
      if (j < i || j <= minJ) {
         console.log('reset');
         i++;
         j = s.length - 1;
         continue;
      }
      // #3 [end]
      if (s[i] !== s[j]) {
         j--;
      } else {
         const isP = isPalindrome(substr)
         if (isP) {
            // #3 [start]
            if (substr.length > result.length) {
               result = substr;
               console.log('FOUND PALINDROME', substr);
               minJ = j;
            }
            // #3 [end]
            // #2 [start]
            // when j is s.length - 1 then is the longest
            if (j === s.length - 1) {
               break;
            }
            // #2 [end]
            j = s.length - 1;
            i++;
            console.log('true palindrome');
            continue;
         }
         j--;
         continue;
      }

   }
   return result;
}
const s1 = 'babad';
const s2 = 'cbbd';
const s3 = 'aacabdkacaa'; // aca
const c1 = 'aba';
const c2 = 'bbxxbb';
const c3 = 'lasdjfiejfifjababababababababababababasdfrasdfiejfiejfiejfiljfsdklfja;sldfjseifjisefjlsidjfisjf';
const s4 = "abacab"; // bacab
const s5 = 'ac'; // a
const start = Date.now();
console.log('RESULT: ', longestPalindrome(c3));
console.log('RUNTIME: ', Date.now() - start);
function isPalindrome(str) {
   let j = str.length - 1;
   for (let i = 0; i < Math.floor(str.length / 2); i++) {

      if (str[i] !== str[j]) {
         return false;
      }
      if (j < i) {
         // reach mid
         break;
      }
      j--;
   }
   return true;
}
 // console.log('is palindrome: ', isPalindrome('a'));