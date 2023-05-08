/*
   LeetCode problem: Valid Palindrom (Easy)

   A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

   Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

   Example 1:
      Input: s = "A man, a plan, a canal: Panama"
      Output: true
      Explanation: "amanaplanacanalpanama" is a palindrome.

   Example 2:
      Input: s = "race a car"
      Output: false
      Explanation: "raceacar" is not a palindrome.

   Example 3:
      Input: s = " "
      Output: true
      Explanation: s is an empty string "" after removing non-alphanumeric characters.
      Since an empty string reads the same forward and backward, it is a palindrome.

   Constraints:

   1 <= s.length <= 2 * 105
   s consists only of printable ASCII characters.

   Solution by myself: 
      convert input jadi lowercase/uppercase lalu hapus non-alphanumeric (bisa pake regex)
      stop jika next index dari ponter 1 === pointer 2
      stop jika next index dari pointer 1 === next index dari pointer 2

   LeetCode submission:
      #1
      Runtime: 79 ms, beats 36.99%
      Memorry: 44.6 MB, beats 72.34%

      #2
      Runtime: 104 ms, beats 7.43%
      Memory: 50.5 MB, beats 12.6%
*/

function validPalindrome(s) {
   if (s.trim() === '') return true;
   s = s.toLowerCase().replaceAll(/[^a-zA-Z0-9]/g,'')
   let j = s.length - 1;
   for (let i = 0; i < s.length; i++) {
      console.log(s[i], s[j]);
      if (s[i] !== s[j]) return false;
      if (i+1 === j || i + 1 === j - 1) break;
      j--;
   }
   return true;
}
const s1 = "A man, a plan, a canal: Panama";
const s2 = "race a car" // 'raceacar'
const s3 = ' ';
const s4 = 'abxba';
const s5 = 'a : bab %a';
const s6 = 'a.';
console.log(validPalindrome2(s6));

function validPalindrome2(s) {
   if (s.length === 1 || s.length === 0) return true
   if (s.trim() === '') return true;
   let j = s.length - 1;
   for (let i = 0; i < s.length; i++) {
      while (/[^a-zA-Z0-9]/.test(s[j])) --j;
      while (/[^a-zA-Z0-9]/.test(s[i])) ++i;
      if (s[i] === undefined || s[j] === undefined) return true;
      if (s[i].toLowerCase() !== s[j].toLowerCase()) return false;
      if (i === j || i+1 === j || i + 1 === j - 1) break;
      j--;
   }
   return true;
}