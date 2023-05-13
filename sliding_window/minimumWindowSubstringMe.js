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

   Solution:
      - use linked list for tracking t's char inside a window (substring)
      - use map for tracking count of characters t's remaining characters to construct a substring, for example:
         t = 'abc'; 
         currentSubstring = 'axb';
         currentT = 'c';
         map = {
            a: 0,
            b: 0,
            c: 1,
         }
         list = a->b;
         ----------------------------------------------------------------
         t = 'abc';
         currentSubstring = 'bbbaxy';
         currentT = 'c';
         map = {
            b: -2,
            a: 0,
            c: 1,
         }
         list = b->b->b->a;
      - when t = '' it means substring is valid then we compare it against current result we choose the min if the result's values not initial 
      - and we pop list's head and increment in the map
      - if the char in the map is above 0 then we can add the char to current t

   LeetCode submission:
      Runtime: 214 ms, beats 16.94%
      Memory: 69 MB, beats 5.29%
*/



function minimumWindowSubstring(s, t) {
   if (t.length > s.length) return '';
   
   console.log(s);
   class LinkedList {
      head = null;      
      size = 0;
      addTail(val) {
         if (this.head === null) {
            this.head = {value: val, next: null};
            this.tail = this.head;
         } else {
            const newTail = {value: val, next: null}
            if (this.head.next === null) {
               this.head.next = newTail;
               this.tail = this.head.next;
               this.size++;
               return;
            }
            this.tail.next = newTail;
            this.tail = this.tail.next;
         }
         this.size++;
      }
      popHead() {
         if (this.head == null) {
            return null;
         } else {
            const poppedHead = Object.assign({}, this.head.value);
            this.head = this.head.next;
            this.size--;
            return poppedHead;
         }
      }
   }

   let list = new LinkedList();
   
   let result = '';

   let sub = '';
   let map = new Map(); // for storing t char in substring
   let l = 0;
   for (let x= 0; x < t.length; x++) {
      if (map.has(t[x])) {
         map.set(t[x], map.get(t[x]) + 1);
      } else {
         map.set(t[x], 1);
      }
   }

   for (let r = 0; r < s.length; r++) {
      
      if (map.has(s[r])) {
         
         if (list.size === 0) {
            console.log('mungkin ini');
            l = r; 
         }
         console.log('list addTail',r, s[r]);
         list.addTail({index: r, char: s[r]});
         map.set(s[r], map.get(s[r]) - 1);
         t = t.replace(s[r], '');
         // console.log('sub outside', sub);
         
         console.log('l', l, 'r', r, 'substring',s.slice(l, r + 1), 'map & list.size', new Map(map), Object.assign({},list), 't', t);
         while (t.length === 0) {
            sub = s.slice(l, r + 1);
            console.log('INSIDE', 'l', l, 'r', r, 'substring',sub, 'map & list.size', map, list.size);

            if (result === '') {
               result = sub;
            } else {
               result = r - l + 1 < result.length ? sub : result;
            }

            console.log('result', result);
            const deletedChar = list.popHead().char;
            // console.log('deletedChar', deletedChar);
            if (list.head === null) {
               return result;
            } else {
               l = 2;
               console.log('next l', l);
            }
            map.set(deletedChar, map.get(deletedChar) + 1)
            // re populate t again, 
            if (map.get(deletedChar) > 0) {
               t += deletedChar;
            }
            console.log('after increase map', new Map(map), 'l', l);
         }
      }

   }
   return result;
}
const s = 'XZADOBECODEBANC'; const t = 'ABC';
const s1 = 'ADOBECODEBANC'; const t1 = 'ABC';
const s2 = 'a'; const t2 = 'a';
const s3 = 'a'; const t3 = 'aa';
const s4 = 'xaybycabcxxba'; const t4 = 'abc'; // cab
const s5 = 'aayxbxcca'; const t5 = 'abc'; // bxcca
const s6 = 'aa'; const t6 = 'aa';
const s7 = 'bdabxfa'; const t7 = 'ab';
console.log('RESULT', minimumWindowSubstring(s7, t7));
/*
   {
      a: 0, b: 0, c: 0
   }
   'banc'
   result = 'banc'
   'bbbbaxc'
   'babbyybbxca'; 'babbyybbxc', 'abbyybbxc', 
*/