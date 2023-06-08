/*
  Leetcode: 647. Palindromic Substrings

  Given a string `s`, return the number of palindromic substrings in it.

  A string is a palindrome when it reads the same backward as forward.

  A substring is a contiguous sequence of characters within the string.
  

  Example 1:
    Input: s = "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".

  Example 2:
    Input: s = "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
  

  Constraints:
    - 1 <= s.length <= 1000
    - s consists of lowercase English letters.

  solution by myself

  Leetcode submission:
    #1 (naive solution) O(n^3)
      Runtime: 375 ms, beats 18.22%;
      Memory: 44 MB, beats 41.90%;
*/

// #1 O(n^3)
function countSubstrings(s) {
  let result = 0;
  let start = [];
  for (let i = 0; i < s.length; i++) {
    // result++;
    start.push(i);
    /*
      aaabbaaa
      a a aa a aaa aa b b bb a abba a aabbaa aa a aaabbaaa aaa aa
    */
    for (let j = 0; j < start.length; j++) {
      const substr = s.slice(j, i+1);
      let l; let r;
      if ((i - j + 1) % 2 === 0) {
        l = Math.floor( (i + j) / 2);
        r = l + 1;
      } else {
        l = r = Math.floor( (i + j) / 2);
      }
      let isPalindrome = true;
      while (l >= j && r <= i) {
        if (s[l] !== s[r]) { 
          isPalindrome = false;
          break;
        }
        l--; r++;
      }
      if (isPalindrome) result++;
    }
  }
  return result;
}
const s1 = 'aaa'; // expect: 6
const s2 = 'abc'; // expect 3
const s3 = 'aaabbaaa'; // expect: 18
// a a aa a aaa aa b b bb a abba a aabbaa aa a aaabbaaa aaa aa'
const start = Date.now();
console.log('RESULT: ', countSubstrings(s2));
console.log('RUNTIME: ', Date.now() - start);

module.exports = countSubstrings;