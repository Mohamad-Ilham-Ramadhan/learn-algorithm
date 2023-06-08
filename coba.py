import datetime

def longestPalindrome(s):
   pass

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