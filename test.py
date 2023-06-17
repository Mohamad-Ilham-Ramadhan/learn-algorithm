import unittest


class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}
def wordBreak(s, wordDict):
    # construct trie
    trie = TrieNode()

    for i in range(len(wordDict)):
        w = wordDict[i]
        pointer = trie
        for c in w:
            if c not in pointer.children:
                pointer.children[c] = TrieNode()
            pointer = pointer.children[c]
        pointer.isEnd = True

    store = [""]
    si = 0
    # store index
    pointer = trie
    for i in range(len(s)):
        c = s[i]
        # print('store', store)
        # print('c', c)
        # print('pointer', pointer.children)
        if c in trie.children:
            #   print('ROOT CHILDREN', pointer.isEnd, si - 1)
            if pointer.isEnd:
                # print('NEW or SPACE')
                store.append(c)
                si += 1
                pointer = trie.children[c]
            else:
                if c in pointer.children:
                    store[si] += c 
                    pointer = pointer.children[c]
                else: 
                    return False

        else:
            #   print('NOT ROOT CHILDREN')
            if c in pointer.children:
                # print('ADD')
                store[si] += c
                pointer = pointer.children[c]
            else:
                # print('REJOIN', store[si])
                # rejoin
                store[si - 1] += store[si]
                store.pop()
                si -= 1
                if si == -1:
                    return False
                # reset pointer
                pointer = trie
                for x in store[si]:
                    if x not in pointer.children:
                        return False
                    else:
                        pointer = pointer.children[x]

                store[si] += c
                # print('pointer.children', pointer.children)
                pointer = pointer.children[c]
    # check words
    #   print('last pointer', pointer.isEnd)
    #   print('store', store)

    # last rejoin
    if not pointer.isEnd:
        store[si - 1] += store[si]
        store.pop()
        si -= 1
        if si == -1:
            return False
        # reset pointer
        pointer = trie
        # print('store', store)
        for x in store[si]:
            if x not in pointer.children:
                return False
            else:
                pointer = pointer.children[x]

    return pointer.isEnd

from coba import wordBreak4

s1 = "leetcode"
wd1 = ["leet", "code"]
# expect: true

s2 = "applepenapple"
wd2 = ["apple", "pen"]
# expect: true
x2 = "applepenapple"
xd2 = ["apple", "ap", "pp", "pen"]
"""
ap pl
cat and cats
cats and cat
"""
s3 = "catsandog"
wd3 = ["cats", "dog", "sand", "and", "cat"]
# expect: false

s4 = "catandcats"
wd4 = ["cat", "and", "cats"]
# expect: true
s5 = "catsandcat"
wd5 = ["cat", "and", "cats"]
# expect: true
s6 = "ab"
wd6 = ["a", "b"]  # expect: true
s7 = "bb"
wd7 = ["a", "b", "bb", "bbb", "bbbb"]  # expect: true, output: false
s8 = "cars"
wd8 = ["car", "ca", "rs"]  # expect: true
s9 = "a"
wd9 = ["b"]
# expect: false,
s10 = "aaaaaaa"
wd10 = ["aaaa", "aa"]
# expect: false, output: true
s11 = "aaaaaaa"
wd11 = ["aaaa", "aaa"]  # expect: true, output: false
s12 = "catscat"
wd12 = ["cat", "cats"]
s13 = 'ccbb'
wd13 = ['bc', 'cb'] # expet: false
s14 = "catsandogcat"
wd14 = ["cats","dog","sand","and","cat","an"] # expect: True, output: false
s15 = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
wd15 = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

class TestCalc(unittest.TestCase):
    def test_xxx(self):
        self.assertEqual(wordBreak4(s1, wd1), True)  # true
        self.assertEqual(wordBreak4(s2, wd2), True)  # true
        self.assertEqual(wordBreak4(x2, xd2), True)  # true
        self.assertEqual(wordBreak4(s3, wd3), False)  # False
        self.assertEqual(wordBreak4(s4, wd4), True)  # True
        self.assertEqual(wordBreak4(s5, wd5), True)  # True
        self.assertEqual(wordBreak4(s6, wd6), True)  # True
        self.assertEqual(wordBreak4(s8, wd8), True)  # True
        self.assertEqual(wordBreak4(s9, wd9), False)  # False
        self.assertEqual(wordBreak4(s10, wd10), False)  # False
        self.assertEqual(wordBreak4(s11, wd11), True)  # True
        self.assertEqual(wordBreak4(s12, wd12), True)  # True
        self.assertEqual(wordBreak4(s13, wd13), False)  # False
        self.assertEqual(wordBreak4(s14, wd14), True)  # True
        self.assertEqual(wordBreak4(s15, wd15), False)  # False


if __name__ == "__main__":
    unittest.main()
