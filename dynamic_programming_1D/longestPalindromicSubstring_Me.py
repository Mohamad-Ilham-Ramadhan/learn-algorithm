import datetime
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

  Solution by myself:

  Leetcode submission:
   #1
      Runtime: 324 ms, beats 94.39%
      Memory: 16.6 MB, beats 24.65%
   #2 remove if r == len(s): return result and loop until len(s) - 1
      Runtime: 343 ms, beats 94.6%
      Memory: 16.4 MB, beats 34.49%
      
'''



def longestPalindrome(s):
   if len(s) == 1: return s

   result = s[0]
   for i in range(len(s)-1):
      c = s[i]

      l = i - 1
      r = i + 1
      set = {s[i]}

      if (s[l] != c or l == -1) and c == s[r]:
         result = s[i:r+1] if len(s[i:r+1]) > len(result) else result
         set.add(s[r])
         r += 1
      
      while l >= -1 and r < len(s):
         if len(result) == len(s): return result

         if i >= 20 and i <= 28:
            print('i', i, 'l', l, 'r', r)
            print('result', result, 'substr', s[l: r+1])
            if (s[r] == s[l+1]):
               print('s[r] == s[l+1]', s[r], s[l+1])
               print('s[l] == s[r]', s[l], s[r])

         if l >= 0 and s[l] == s[r]:
            print('BOTH EQUAL')
            result = s[l:r+1] if len(s[l:r+1]) > len(result) else result
            set.add(s[l]); set.add(s[r])
            l = l - 1
            r +=1
         elif s[r] == s[l+1]:
            print('ELIF', set)
            if len(set) == 1:
               result = s[l+1:r+1] if len(s[l+1:r+1]) > len(result) else result 
               r += 1
            else:
               break
         else:
            break
   
   return result
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
s23 = 'bb'

start = datetime.datetime.now().timestamp()
print('Result: ', longestPalindrome('cbbd'))
# s = 'aaac'
# print('s[-1:4]', s[-1:4])
print('Runtime: ', datetime.datetime.now().timestamp() - start)