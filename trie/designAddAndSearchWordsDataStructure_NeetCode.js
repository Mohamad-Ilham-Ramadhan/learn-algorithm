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

   Solution by NeetCode:
      Use Trie and DFS
   
   LeetCode submission:
      - runtime: 894 ms, beats 88.55%
      - Memory: 116.4 MB, beats 37%
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
      this.word = false;
   }
}

class WordDictionary {
   constructor() {
      this.root = new TrieNode();
   }
   /**
    * @param {string} word
    * @return {void}
    */
   addWord(word) {
      let cur = this.root;
      for (let c of word) {
         if (!(c in cur.children)) cur.children[c] = new TrieNode();
         cur = cur.children[c];
      }
      cur.word = true;
   }


   /**
    * @param {string} word
    * @return {boolean}
    */
   search(word) {
      function dfs(j, root) {
         let cur = root;

         for (let i = j; i < word.length; i++) {
            const c = word[i];
            
            if (c === '.') {
               for (let key in cur.children) {
                  let child = cur.children[key];
                  if (dfs(i + 1, child)) return true;
               }
               return false;
            } else {
               if (!(c in cur.children)) return false;
               cur = cur.children[c];
            }
         }

         return cur.word;
      }
      return dfs(0, this.root);
   }
}
let w = new WordDictionary();

// test 1
w.addWord('bad');
w.addWord('dad');
w.addWord('mad');
w.addWord('bxyd');
w.addWord('bxxd');

console.log('search pad', w.search('pad'), 'expect false'); // expected: false;
console.log('search bad', w.search('bad'), 'expect true'); // expected: true;
console.log('search .ad', w.search('.ad'), 'expect true'); // expected: true;
console.log('search b..', w.search('b..'), 'expect true'); // expected: true;
console.log('search b..d', w.search('b..d'), 'expect true'); // expected: true;
console.log('search .a.', w.search('.a.'), 'expect true'); // expected: true;

/* test 2 
  ["WordDictionary","addWord","addWord","addWord","addWord",  "search","search",  "addWord",  "search","search","search","search","search","search"]

  [[],["at"],["and"],["an"],["add"],   ["a"],[".at"],  ["bat"],  [".at"],["an."],["a.d."],["b."],["a.d"],["."]]

  expect: [null,null,null,null,null,  false,false,  null,  true,true,false,false,true,false]
  output: fixed, all passed
*/
// w.addWord('at');
// w.addWord('and');
// w.addWord('an');
// w.addWord('add');
// console.log('search a', w.search('a'), 'expect false'); // expect: false
// console.log('search .at', w.search('.at'), 'expect false'); // expect: false
// w.addWord('bat');
// console.log('search .at', w.search('.at'), 'expect true'); // expect: true
// console.log('search an.', w.search('an.'), 'expect true'); // expect: true
// console.log('search a.d.', w.search('a.d.'), 'expect false'); // expect: false
// console.log('search b.', w.search('b.'), 'expect false'); // expect: false
// console.log('search a.d', w.search('a.d'), 'expect true'); // expect: true
// console.log('search .', w.search('.'), 'expect false'); // expect: false


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


