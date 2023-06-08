'''
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

  Solution by NeetCode:
    using two pointer 

  Leetcode submission:
   Runtime: 700 ms, beats 60.90%
   Memory: 16.4 MB, beats 34.49%
      
'''
import datetime

def longestPalindrome(s):
   res = ''
   resLen = 0

   for i in range(len(s)):
      # odd length palindrome 
      l, r = i, i
      while l >= 0 and r < len(s) and s[l] == s[r]:
         if (r - l + 1) > resLen:
            res = s[l:r+1]   
            resLen = r - l + 1
         l -= 1
         r += 1
      
      # even length palindrome 
      l, r = i, i + 1
      while l >= 0 and r < len(s) and s[l] == s[r]:
         if (r - l + 1) > resLen:
            res = s[l:r+1]
            resLen = r - l + 1
         l -= 1
         r += 1
   
   return res 

s9 = 'astxtsxas' # expect: stxts
s10 = 'aaaa' # expect: aaaa, output: aaa
s11 = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # length = 47
s12 = 'aaabaaaa' # expect: aaabaaa, output: aaabaaaa
s13 = 'xxxxccxxxxxx' # expect: xxxxccxxxx
s14 = 'xxxxxxccxxxx' # expect: xxxxccxxxx
s15 = 'xxxxxxcccxxxx' # expect: xxxxcccxxxx
s16 = 'xxxxxxcacxxxx' # expect: xxxxcacxxxx
s17 = 'caaaaa' # expect: aaaaa, output: aa
s18 = 'aaaac' # expect: aaaa
s19 = 'acaa' # expect: aca
s20 = 'abbcccbbbcaaccbababcbcabca' # expect: bbcccbb, output: bbcccbbb
s21 = 'aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa' # expect: same
s22 = 'ccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbcccccccccc'

start = datetime.datetime.now().timestamp()
print('Result: ', longestPalindrome(s21))
print('Runtime: ', datetime.datetime.now().timestamp() - start)