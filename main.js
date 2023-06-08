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
    #6 (start from middle of possible palindrome) (after watching half of NeetCode's solution explanation)
      #1
        Runtime: 5283 ms, beats 5.92%
        Memory: 49.6 MB, beats 21.76%
      #2 clear comments
        Runtime: 5374 ms, beats 5.71%
        Memory: 49.4 MB, beats 23.40%
      #3 optimized set
        Runtime: 109 ms, beats 57.1%
        Memory: 51.1 MB, beats 16.51%;
      
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
  console.log('x', x);
  return result;
}
const s1 = 'babad';
/*
  b
  ba

  a
  ba
  ab
  bab

  b
  ab
  ba
  aba

  a
  ba
  ad
  bad

  d
  ad
*/
const s2 = 'cbbd';
/*
  c
  cb
  cbb
  cbbd

  b
  cb
  bb
  bbd

  b
  bb
  cbb
  bd

  d

*/
const s3 = 'aacabdkacaa'; // aca
/*
*/
const c1 = 'aba';
const c2 = 'bbxxbb';
const c3 = 'lasdjfiejfifjababababababababababababasdfrasdfiejfiejfiejfiljfsdklfja;sldfjseifjisefjlsidjfisjf';
const c4 = 'bbxxbbccccycccc';
const s4 = "abacab"; // bacab
/*
  ab
  aba
  bac
  bacab

  a
  ab
  aba yes
  bac
  abac

  aca
*/
const s5 = 'ac'; // a or c
const s6 = 'fdebasabemni'; // ebasabe
/*
  fd
  fde
  deb
  eba
  bas
  ebasabe

  s yes
  sa no
  ab no
  asa yes
  sab no
  basa no
  asab no
  basab yes
  ebasab no
  basabe no
  ebasabe yes
  debasabe no
  ebasabem no
  debasabem no
  fdebasabem no
  debasabemn no
  fdebasabemn no
  fdebasabemni no

*/
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
const s8 = 'zccxxxccui';

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
        if (substr.length <= result.length) { console.log('below result'); break };
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
// console.log('new longest: ', newLongest(s6))

// After watching half of NeetCode solution explanation.
function startFromMiddle(s) {
  if (s.length === 1) return s;

  let result = s[0]
  for (let i = 0; i < s.length; i++) {
    const c = s[i];

    let l = i - 1;
    let r = i + 1;
    let x = 0;
    // if (s[l] === c && c === s[r]) {
    //   if (s.slice(i-1,r+1).length > result.length) {
    //     result = s.slice(i-1,r+1);
    //     set = new Set(result);
    //   }
    //   l--; r++;
    // } else if (s[l] === c) {
    //   if (s.slice(l,i+1).length > result.length) {
    //     result = s.slice(l,i+1);
    //     set = new Set(result);
    //   }
    //   l--;
    // } else if (s[r] === c) {
    //   if (s.slice(i,r+1).length > result.length) {
    //     result = s.slice(i,r+1);
    //     set = new Set(result);
    //   }
    //   r++;
    // }
    // cbbd
    // bbxxbb
    // set optimization [start]
    let set = new Set(c); // if only one char then current result is all the same char
    // set optimization [end]
    if (s[l] !== c && c === s[r]) {
      result = s.slice(i, r + 1).length > result.length ? s.slice(i, r + 1) : result;
      // set optimization [start]
      set.add(s[r]);
      // set optimization [end]
      r++;
    }
    // console.log('FOR result:', result) // <-- x
    while (l >= -1 && r <= s.length) {
      // if (i >= 20 && i <= 28) {
      //   console.log('substr', substr, 'set', set); // <-- x
      //   console.log('char', c, 'i', i, 'l',l, 'r', r); // <-- x
      //   console.log('result', result); // <-- x
      // }
      // if (x === 10) break;
      // x++;
      if (result.length === s.length) return result;


      if (s[l] === s[r]) {
        // console.log('both equal', s.slice(l, r+1)); // <-- x
        result = s.slice(l, r + 1).length > result.length ? s.slice(l, r + 1) : result;
        // set optimization [start]
        set.add(s[l]).add(s[r])
        // set optimization [end]
        l--;
        r++;
      } else if (s[r] === s[l + 1]) {
        // console.log('push right'); // <-- x
        // let substr = s.slice(l+1, r+1);
        // console.log('s[mid]', s[mid], 's[mid-1]', s[mid-1]); // <-- x
        // if (s[mid] === s[mid-1] && s[mid] === s[mid+1]) {
        // console.log('set', set) // <-- x  
        // set = new Set(s.slice(l+1, r+1));
        if (set.size === 1) {
          // console.log('able push', s.slice(l+1, r+1)) // <-- x
          result = s.slice(l + 1, r + 1).length > result.length ? s.slice(l + 1, r + 1) : result;
          r++;
        }
        else {
          // console.log('cannot push'); // <-- x
          break;
        }
      } else {
        break;
      }
    }
  }
  return result; // axaxaa
}
function startFromMiddle_SetOptimized(s) {
  if (s.length === 1) return s;

  let result = s[0]
  for (let i = 0; i < s.length; i++) {
    const c = s[i];

    let l = i - 1;
    let r = i + 1;
    let set = new Set(c); // if only one char then current result is all the same char

    if (r === s.length) return result;

    if (s[l] !== c && c === s[r]) {
      result = s.slice(i, r + 1).length > result.length ? s.slice(i, r + 1) : result;
      set.add(s[r]);
      r++;
    }
    // console.log('for');
    while (l >= 0 && r <= s.length - 1) {
      if (result.length === s.length) return result;

      if (i >= 20 && i <= 28) {
        console.log('i', i, 'l', l, 'r', r)
        console.log('result', result, 'substr', s.slice(l,r+1))
      }
      
      // console.log('i', i, 'l', l, 'r', r);

      if (s[l] === s[r]) {
        result = s.slice(l, r + 1).length > result.length ? s.slice(l, r + 1) : result;
        set.add(s[l]).add(s[r])
        // l--;
        l = l > 0 ? l - 1 :  l;
        r++;
      } else if (s[r] === s[l + 1]) { // push next right char if it's same char with current palindrome
        if (set.size === 1) { // if only 1 char variety in current substr/palindrome
          result = s.slice(l + 1, r + 1).length > result.length ? s.slice(l + 1, r + 1) : result;
          r++;
        } else { break; }
      } else {
        break;
      }
    }
  }
  return result; 
};

function neetCodes(s) {
  let res = '';
  let resLen = 0;


  for (let i = 0; i < s.length; i++) {

    // odd length palindrome
    let l = i; let r = i;
    while (l >= 0 && r < s.length && s[l] == s[r]) {
      if ((r - l + 1) > resLen) {
        res = s.slice(l, r+1);
        resLen = r - l + 1;
      }
      l--; r++;
    }

    // even length palindrome
    l = i; r = i + 1;
    while (l >= 0 && r < s.length && s[l] == s[r]) {
      if ((r - l + 1) > resLen) {
        res = s.slice(l, r+1);
        resLen = r - l + 1;
      }
      l--; r++;
    }
  }
  return res;
}
const s9 = 'astxtsxas'; // expect: stxts
const s10 = 'aaaa'; // expect: aaaa, output: aaa
const s11 = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'; // length = 47
const s12 = 'aaabaaaa'; // expect: aaabaaa, output: aaabaaaa
const s13 = 'xxxxccxxxxxx' // expect: xxxxccxxxx
const s14 = 'xxxxxxccxxxx' // expect: xxxxccxxxx
const s15 = 'xxxxxxcccxxxx' // expect: xxxxcccxxxx
const s16 = 'xxxxxxcacxxxx' // expect: xxxxcacxxxx
const s17 = 'caaaaa' // expect: aaaaa, output: aa
const s18 = 'aaaac'; // expect: aaaa
const s19 = 'acaa'; // expect: aca
const s20 = 'abbcccbbbcaaccbababcbcabca'; // expect: bbcccbb, output: bbcccbbb
const s21 = 'aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa'; // expect: same
const s22 = 'ccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbcccccccccc';

/*
  caaaaa
  ca
  caa -> aa
*/
const start = Date.now()
console.log('START FROM MIDDLE: ', neetCodes(s21));
console.log('runtime : ', Date.now() - start);
/*
  c2 = 'bbxxbb'; mid must be 'xx'
*/
module.exports = startFromMiddle;
