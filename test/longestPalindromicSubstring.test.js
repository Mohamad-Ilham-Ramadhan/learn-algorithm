const neetCodes = require('../main');

test('babad', () => {
   expect(neetCodes('babad')).toMatch(/^bab|aba$/);
})
test('cbbd', () => {
   expect(neetCodes('cbbd')).toMatch(/^bb$/);
});
test('aacabdkacaa', () => {
   expect(neetCodes('aacabdkacaa')).toMatch(/^aca$/);
})
test('bbxxbb', () => {
   expect(neetCodes('bbxxbb')).toMatch(/^bbxxbb$/);
})
test('lasdjfiejfifjababababababababababababasdfrasdfiejfiejfiejfiljfsdklfja;sldfjseifjisefjlsidjfisjf', () => {
   expect(neetCodes('lasdjfiejfifjababababababababababababasdfrasdfiejfiejfiejfiljfsdklfja;sldfjseifjisefjlsidjfisjf')).toMatch(/^ababababababababababababa$/);
})
test('abacab;sldfjseifjisefjlsidjfisjf', () => {
   expect(neetCodes('abacab')).toMatch(/^bacab$/);
})
test('ac', () => {
   expect(neetCodes('ac')).toMatch(/^a$/);
})
test('fdebasabemni', () => {
   expect(neetCodes('fdebasabemni')).toMatch(/^ebasabe$/);
})
test('bb', () => {
   expect(neetCodes('bb')).toMatch(/^bb$/);
})
test('zccxxxccui', () => {
   expect(neetCodes('zccxxxccui')).toMatch(/^ccxxxcc$/);
})
test('astxtsxas', () => {
   expect(neetCodes('astxtsxas')).toMatch(/^stxts$/);
})
test('aaaa', () => {
   expect(neetCodes('aaaa')).toMatch(/^aaaa$/);
})
test('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', () => {
   expect(neetCodes('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')).toMatch(/^xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx$/);
})
test('aaabaaaa', () => {
   expect(neetCodes('aaabaaaa')).toMatch(/^aaabaaa$/);
})
test('xxxxccxxxxxx', () => {
   expect(neetCodes('xxxxccxxxxxx')).toMatch(/^xxxxccxxxx$/);
})
test('xxxxxxccxxxx', () => {
   expect(neetCodes('xxxxxxccxxxx')).toMatch(/^xxxxccxxxx$/);
})
test('xxxxxxcccxxxx', () => {
   expect(neetCodes('xxxxxxcccxxxx')).toMatch(/^xxxxcccxxxx$/);
})
test('xxxxxxcacxxxx', () => {
   expect(neetCodes('xxxxxxcacxxxx')).toMatch(/^xxxxcacxxxx$/);
})
test('caaaaa', () => {
   expect(neetCodes('caaaaa')).toMatch(/^aaaaa$/);
})
test('aaaac', () => {
   expect(neetCodes('aaaac')).toMatch(/^aaaa$/);
})
test('zabcbazxxx', () => {
   expect(neetCodes('zabcbazxxx')).toMatch(/^zabcbaz$/);
})
test('xxxazbcbza', () => {
   expect(neetCodes('xxxazbcbza')).toMatch(/^azbcbza$/);
})
test('abbcccbbbcaaccbababcbcabca', () => {
   expect(neetCodes('abbcccbbbcaaccbababcbcabca')).toMatch(/^bbcccbb$/);
})
test('aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa', () => {
   expect(neetCodes("aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa")).toMatch(/^aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa$/);
})


