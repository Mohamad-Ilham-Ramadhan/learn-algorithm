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

  Solution by NeetCode

  Leetcode submission:
      Runtime: 71 ms, beats 90.91%
      Memory: 44.2 MB, beats 73.20%
*/


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
