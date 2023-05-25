/*
   Leetcode: 208. Implement Trie (Prefix Tree) (medium)

   A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

   Implement the Trie class:
      - `Trie()` Initializes the trie object.
      - `void insert(String word)` Inserts the string `word` into the trie.
      - `boolean search(String word)` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
      - `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.
   

   Example 1:

   Input
      ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
      [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

   Output
      [null, null, true, false, true, null, true]

   Explanation
      Trie trie = new Trie();
      trie.insert("apple");
      trie.search("apple");   // return True
      trie.search("app");     // return False
      trie.startsWith("app"); // return True
      trie.insert("app");
      trie.search("app");     // return True
   

   Constraints:
      - 1 <= word.length, prefix.length <= 2000
      - word and prefix consist only of lowercase English letters.
      - At most 3 * 104 calls in total will be made to insert, search, and startsWith.

   Solution by NeetCode:
      not use hash set to store inserted word
      mark the end of the word with boolean for searching for word

   LeetCode submission:
      - runtime: 167 ms, beats 99%
      - memory: 63.5 MB, beats 46.72%
*/

/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */

class TrieNode {
   constructor() {
      this.children = {};
      this.endOfWord = false;
   }
}

class Trie {
   constructor() {
      this.root = new TrieNode();
   }
   /**
    * @param {string} word
    * @return {void}
    */
   insert(word) {
      let cur = this.root;
      for (let c of word) {
         if (! (c in cur.children)) {
            cur.children[c] = new TrieNode();
         }
         cur = cur.children[c];
      }
      cur.endOfWord = true;
   }
   /**
    * @param {string} word
    * @return {boolean}
    */
   search(word) {
      let cur = this.root;
      for (let c of word) {
         if (! (c in cur.children)) {
            return false;
         }
         cur = cur.children[c];
      }
      return cur.endOfWord;
   }
   /**
    * @param {string} prefix
    * @return {boolean}
    */
   startsWith(prefix) {
      let cur = this.root;
      for (let c of prefix) {
         if (! (c in cur.children)) {
            return false;
         }
         cur = cur.children[c];
      }
      return true;
   }
}

/*
   Trie trie = new Trie();
   trie.insert("apple");
   trie.search("apple");   // return True
   trie.search("app");     // return False
   trie.startsWith("app"); // return True
   trie.insert("app");
   trie.search("app");     // return True
*/

const trie = new Trie();
trie.insert('apple');
console.log('search apple: ', trie.search('apple')); // expect: true
console.log('search app: ', trie.search('app')); // expect: false
console.log('startsWith app: ', trie.startsWith('app')); // expect: true
trie.insert('app');
console.log('search app: ', trie.search('app')); // expect: true
trie.insert('ape');
console.log('search ape: ', trie.search('ape')); // expect: true
