/*
   LeetCode: 211. Design Add and Search Words Data Structure (medium)

   Design a data structure that supports adding new words and finding if a string matches any previously added string.

   Implement the `WordDictionary` class:

   `WordDictionary()` Initializes the object.
   `void addWord(word)` Adds `word` to the data structure, it can be matched later.
   `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.
   

   Example:
      Input
         ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
         [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
      Output
         [null,null,null,null,false,true,true,true]

      Explanation
         WordDictionary wordDictionary = new WordDictionary();
         wordDictionary.addWord("bad");
         wordDictionary.addWord("dad");
         wordDictionary.addWord("mad");
         wordDictionary.search("pad"); // return False
         wordDictionary.search("bad"); // return True
         wordDictionary.search(".ad"); // return True
         wordDictionary.search("b.."); // return True
   

   Constraints:
      - 1 <= word.length <= 25
      - word in addWord consists of lowercase English letters.
      - word in search consist of '.' or lowercase English letters.
      - There will be at most 2 dots in word for search queries.
      - At most 104 calls will be made to addWord and search.

   Solution by myself:
   
   LeetCode submission:
      - runtime: 906 ms, beats 87.18%
      - Memory: 126.3 MB, beats 19.1%
*/

/** 
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */

class TrieNode {
   constructor() {
      this.children = {};
      this.endOfWord = false;
   }
}

class WordDictionary {
   constructor() {
      this.root = new TrieNode();
      this.dot = 0;
   }
   /**
    * @param {string} word
    * @return {void}
    */
   addWord(word) {
      let current = this.root;
      for (let l of word) {
         if (!(l in current.children)) current.children[l] = new TrieNode();
         current = current.children[l];
      }
      current.endOfWord = true;
   }

   searchDot(word, current, dot) {
      // console.log(`searchDot ${dot} word`, word);
      for (let i = 0; i < word.length; i++) {
         let char = word.charAt(i);
         // console.log(`searchDot ${dot} char`, char)
         // console.log(`searchDot ${dot} current.children`, current.children);
         if (char === '.') {
            // console.log('(char === .) current.children', current.children);
            if (Object.keys(current.children).length === 0) return false;
            for (const c in current.children) {
               // console.log(`searchDot ${dot} dot as`, c);
               if (this.searchDot(word.slice(i+1), current.children[c], dot + 1)) return true;
            }
         }
         if (!(char in current.children)) {
            // console.log(`searchDot ${dot}, char is not found`)
            return false
         };
         current = current.children[char];
      }
      return current.endOfWord;

   }


   /**
    * @param {string} word
    * @return {boolean}
    */
   search(word) {
      let current = this.root;
      for (let i = 0; i < word.length; i++) {
         let char = word.charAt(i);
         // console.log('search char', char)
         // console.log('search current', current);

         if (char === '.') {
            // console.log('(char === .) current', current);
            if (Object.keys(current.children).length === 0) return false;
            for (const c in current.children) {
               // console.log('search dot as', c);
               if (this.searchDot(word.slice(i+1), current.children[c], this.dot)) return true;
            }
            return false;
         }

         if (!(char in current.children)) {
            return false
         };
         current = current.children[char];
      }
      return current.endOfWord;
   }
}
let w = new WordDictionary();

// test 1
// w.addWord('bad');
// w.addWord('dad');
// w.addWord('mad');

// console.log('search pad', w.search('pad'), 'expect false'); // expected: false;
// console.log('search bad', w.search('bad'), 'expect true'); // expected: true;
// console.log('search .ad', w.search('.ad'), 'expect true'); // expected: true;
// console.log('search b..', w.search('b..'), 'expect true'); // expected: true;
// console.log('search .a.', w.search('.a.'), 'expect true'); // expected: true;

/* test 2 
  ["WordDictionary","addWord","addWord","addWord","addWord",  "search","search",  "addWord",  "search","search","search","search","search","search"]

  [[],["at"],["and"],["an"],["add"],   ["a"],[".at"],  ["bat"],  [".at"],["an."],["a.d."],["b."],["a.d"],["."]]

  expect: [null,null,null,null,null,  false,false,  null,  true,true,false,false,true,false]
  output: fixed, all passed
*/
w.addWord('at');
w.addWord('and');
w.addWord('an');
w.addWord('add');
console.log('search a', w.search('a'), 'expect false'); // expect: false
console.log('search .at', w.search('.at'), 'expect false'); // expect: false
w.addWord('bat');
console.log('search .at', w.search('.at'), 'expect true'); // expect: true
console.log('search an.', w.search('an.'), 'expect true'); // expect: true
console.log('search a.d.', w.search('a.d.'), 'expect false'); // expect: false
console.log('search b.', w.search('b.'), 'expect false'); // expect: false
console.log('search a.d', w.search('a.d'), 'expect true'); // expect: true
console.log('search .', w.search('.'), 'expect false'); // expect: false


/* 
abah
azas

a.a.x

      a
    b   z   <--- 0
    a   a
    h   s   <--- 1

aba   
*/


