/*
  Leetcode: 647. Palindromic Substrings (medium)

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

  solution by myself:
    #2 (usind dynamic programming)
        pattern n = result of n - 1 + n
        1(0 + 1) 3(2 + 1) 6(3 + 3) 10(6 + 4) 15(10 + 5) 21(15 + 6) 28(21 + 7) 36(28 + 8) 45(36 + 9)

        for example 'aaaa'
        n1 = 'a' = 0 + 1 = 1 -> 'a'
        n2 = 'aa' = 1 + 2 = 3 -> 'a' + 'a', 'aa'
        n3 = 'aaa' = 3 + 3 = 6 -> 'a' 'a' 'aa' + 'a'[2] 'aa'[1,2] 'aaa'[0,2]
        n4 = 'aaaa' = 6 + 4 = 10 => 'a' 'a' 'aa' 'a' 'aa' 'aaa' + 'a'[3] 'aa'[2,3] 'aaa'[1,3] 'aaaa'[0,3]

        and count found palindrome with char in the mid part and left/right side is different for example: 'xyyx', 'aba' not 'aaa' as one:
          xaaxyy
          found palindrome is xaax
          x = 1
          aa = 3
          x = 1
          yy = 3
          xaax = 1

          total = 9


  Leetcode submission:
    #1 (naive solution) O(n^3)
      Runtime: 375 ms, beats 18.22%;
      Memory: 44 MB, beats 41.90%;
    #2 (using dynamic programming), newCountSubstrings
      Runtime: 49 ms, beats 99.64%
      Memory: 44.4 MB, beats 39.31%
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
      const substr = s.slice(j, i + 1);
      let l; let r;
      if ((i - j + 1) % 2 === 0) {
        l = Math.floor((i + j) / 2);
        r = l + 1;
      } else {
        l = r = Math.floor((i + j) / 2);
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
const s4 = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'; // 1000 length of a. Expect: 500500
// const start = Date.now();
// console.log('RESULT: ', countSubstrings(s4));
// console.log('RUNTIME: ', Date.now() - start);
// pattern
// 1(0 + 1) 3(2 + 1) 6(3 + 3) 10(6 + 4) 15(10 + 5) 21(15 + 6) 28(21 + 7) 36(28 + 8) 45(36 + 9)
function pattern(n) {
  const map = { 1: 1 }
  let s = 'aaa';
  for (let i = 2; i <= n; i++) {
    map[i] = map[i - 1] + i;
    s += 'a';
  }
  console.log('s', s)
  return map[n];
}
// console.log('pattern: ', pattern(2))

/*
  axxabyyb
  a 1
  xx 3
  a 1
  axxa 1
  b 1
  yy 3
  b 1
  byyb 1

  axxaaxxa
  prevTwo [a,4]
  prevOne [x,5]
  current [a,7]
  a 1
  xx 3
  axxaa 1
  aa 3
  xaax 1
  xxaaxx 1
  axxaaxxa 1
  xx 3
  axxa 1 
  a 1
*/
// using dynamic programming, O(n)
function newCountSubstrings(s) {
    let result = 0;
    let prevTwo = []; // [char, index], prev two char different from current. Example axxa, a at 0 is prevTwo, current is a at 3
    let prevOne = []; // [char, index], prev one char different from current. Example axxa, x at 2 is prevTwo, current is a at 3
    let count = 0; // count substring sequence using dynamic programming
    let countChars = 0; // chars count for example 'a' = 1, 'bb' = 2, 'xxx' = 3
    for (let i = 0; i <= s.length; i++) {
      console.log('prevOne', prevOne, 'prevTwo', prevTwo);
      const c = s[i];
      if (s[i-1] !== c) {
        prevTwo = [...prevOne];
        prevOne = [s[i-1], i-1];
        console.log('po', prevOne);
        // current[0] = s[i];
        result += count;
        count = 0;
        countChars = 0;

        // palindromic count. For example axxa = 1, aaxxaa = 1
        let l = prevTwo[1];
        let r = i;
        while (c !== prevOne[0] && s[l] === s[r] && l >= 0 && r < s.length) {
          console.log('PALINDROMIC', s.slice(l, r + 1));
          result++;
          l--;
          r++;
        }

      }
      countChars++;
      console.log('count before', count);
      count = count + countChars;
      console.log('countChars', countChars);
      console.log('count after', count);


      console.log('result', result);
      console.log('===========');
    }
    return result;
}
const start = Date.now();
console.log('RESULT: ', newCountSubstrings('xaaaax'));
console.log('RUNTIME: ', Date.now() - start);

module.exports = countSubstrings;