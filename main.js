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
    #5 (newLongest function)
      Runtime: 318 ms, beats 39.67%
      Memory: 48.8 MB, beats 30.90%
      
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
    x++;
    console.log(s.slice(i, j+1), i, j);
    const substr = s.slice(i, j+1);
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
      if ( isP) {
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
  console.log('x', x);
  return result;
}
const s1 = 'babad';
/*
  b yes
  ba  no
  bab yes 
  baba no
  babad no
  aba yes
*/
const s2 = 'cbbd';
/*
  c yes
  cb no
  cbb no
  cbbd no
  bb yes
*/
const s3 = 'aacabdkacaa'; // aca
/*
  a yes
  aa yes
  aac no
  aaca no
  aacabd no
  aacabdk no
  aacabdka no
  aacabdkac no
  aacabdkaca no
  aacabdkacaa no
  acabkdacaa no
  acabdkaca no
  acabdkac no
  acabdka no
  acabdk no
  acabd no
  acab no
  aca yes

  aacabdkacaa
  d yes
  bdk no
  acaa no
  aca yes
*/
const c1 = 'aba';
const c2 = 'bbxxbb';
const c3 = 'lasdjfiejfifjababababababababababababasdfrasdfiejfiejfiejfiljfsdklfja;sldfjseifjisefjlsidjfisjf';
const c4 = 'bbxxbbccccycccc';
const s4 = "abacab"; // bacab
/*
  a yes

  ab
  b yes

  aba yes
  ba
  a yes 

  abac
  bac
  ac
  c yes 

  abaca
  baca
  aca yes 
  ca
  a yes

  abacab
  bacab yes
  acab
  cab
  ab
  b
*/
const s5 = 'ac'; // a or c
const s6 = 'fdebasabemni'; // ebasabe
const s7 = 'bb';
/*
  f yes

  fd
  d yes

  fde
  de
  e yes

  fdeb
  deb
  eb
  b yes

  fdeba
  deba
  eba
  ba
  a yes

  fdebas
  debas
  ebas
  bas
  as
  s yes

  fdebasa
  debasa
  ebasa
  basa
  asa yes
  no need

  fdebasab
  debasab
  ebasab
  basab yes
  no need

  fdebasabe
  debasabe
  ebasabe yes (7)
  no need
  fdebasabem
  
*/
// const start = Date.now();
// console.log('RESULT: ', longestPalindrome(s6));
// console.log('RUNTIME: ', Date.now() - start);
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

function newLongest(s) {
  if (s.length === 1) return s;
  console.log('full s', s);
  let map = new Map(); // map of char : Set(indexes...)
  // right go right 
    // check palindrome from left to right
    // store char : index in map
  
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    map.set(c, map.get(c) ? map.get(c).add(i) : new Set([i]))
  }
  console.log('map', map);
  // when right touch the last
  // right go left
    // del char, index from map
    // if leftChar in map then palindrome check
  let result = s[0];
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    console.log('c', c, map.get(c));
    if (map.get(c)) {
      const set = Array.from(map.get(c));
      for (let j = set.length - 1; j > 0; j--) {
        const nextIndex = set[j];
        console.log('nextIndex', nextIndex);
        const substr = s.slice(i, nextIndex + 1);
        if (substr.length <= result.length) {console.log('below result'); break};
        // console.log('substr', substr);
        if (isPalindrome(substr)) {
          console.log('substr', substr);
          if (substr.length === s.length) return substr;
          result = substr.length > result.length ? substr : result;
          break;
        }
      }
    }
  }

  return result;
}
console.log('new longest: ', newLongest(s6))