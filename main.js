/*
  Leetcode: 139. Word Break (medium)

  Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

  Note that the same word in the dictionary may be reused multiple times in the segmentation.

  

  Example 1:
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".

  Example 2:
    Input: s = "applepenapple", wordDict = ["apple","pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
    Note that you are allowed to reuse a dictionary word.

  Example 3:
    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: false
  

  Constraints:
    - 1 <= s.length <= 300
    - 1 <= wordDict.length <= 1000
    - 1 <= wordDict[i].length <= 20
    - s and wordDict[i] consist of only lowercase English letters.
    - All the strings of wordDict are unique.
*/
class TrieNode {
  constructor() {
    this.isEnd = false
    this.children = {}
  }
}
function wordBreak(s, wordDict) {
  let trie = new TrieNode();
  for (let i = 0; i < wordDict.length; i++) {
    const w = wordDict[i]
    let pointer = trie;
    console.log('w', w)
    for (const c of w) {
      console.log('c', c, !(c in pointer.children))
      if (! (c in pointer.children)) {
        pointer.children[c] = new TrieNode()
      }
      pointer = pointer.children[c]
    }
    pointer.isEnd = true;
  }
  console.log('trie', trie);
}
const s1 = 'leetcode'; const wd1 = ['leet', 'code']; // expect: true
const s2 = 'applepenapple'; const wd2 = ['apple', 'pen']; // expect: true
console.log('RESULT: ', wordBreak(s2, wd2));