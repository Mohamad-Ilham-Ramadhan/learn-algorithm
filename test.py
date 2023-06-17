import unittest
from coba import wordBreak

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
        self.assertEqual(wordBreak(s1, wd1), True)  # true
        self.assertEqual(wordBreak(s2, wd2), True)  # true
        self.assertEqual(wordBreak(x2, xd2), True)  # true
        self.assertEqual(wordBreak(s3, wd3), False)  # False
        self.assertEqual(wordBreak(s4, wd4), True)  # True
        self.assertEqual(wordBreak(s5, wd5), True)  # True
        self.assertEqual(wordBreak(s6, wd6), True)  # True
        self.assertEqual(wordBreak(s8, wd8), True)  # True
        self.assertEqual(wordBreak(s9, wd9), False)  # False
        self.assertEqual(wordBreak(s10, wd10), False)  # False
        self.assertEqual(wordBreak(s11, wd11), True)  # True
        self.assertEqual(wordBreak(s12, wd12), True)  # True
        self.assertEqual(wordBreak(s13, wd13), False)  # False
        self.assertEqual(wordBreak(s14, wd14), True)  # True
        self.assertEqual(wordBreak(s15, wd15), False)  # False


if __name__ == "__main__":
    unittest.main()
