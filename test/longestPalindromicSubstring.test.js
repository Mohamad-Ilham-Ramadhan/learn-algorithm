const startFromMiddle = require('../main');

test('babad', () => {
   expect(startFromMiddle('babad')).toMatch(/^bab|aba$/);
})
test('cbbd', () => {
   expect(startFromMiddle('cbbd')).toMatch(/^bb$/);
});
test('aacabdkacaa', () => {
   expect(startFromMiddle('aacabdkacaa')).toMatch(/^aca$/);
})
test('bbxxbb', () => {
   expect(startFromMiddle('bbxxbb')).toMatch(/^bbxxbb$/);
})
test('lasdjfiejfifjababababababababababababasdfrasdfiejfiejfiejfiljfsdklfja;sldfjseifjisefjlsidjfisjf', () => {
   expect(startFromMiddle('lasdjfiejfifjababababababababababababasdfrasdfiejfiejfiejfiljfsdklfja;sldfjseifjisefjlsidjfisjf')).toMatch(/^ababababababababababababa$/);
})
test('abacab;sldfjseifjisefjlsidjfisjf', () => {
   expect(startFromMiddle('abacab')).toMatch(/^bacab$/);
})
test('ac', () => {
   expect(startFromMiddle('ac')).toMatch(/^a$/);
})
test('fdebasabemni', () => {
   expect(startFromMiddle('fdebasabemni')).toMatch(/^ebasabe$/);
})
test('bb', () => {
   expect(startFromMiddle('bb')).toMatch(/^bb$/);
})
test('zccxxxccui', () => {
   expect(startFromMiddle('zccxxxccui')).toMatch(/^ccxxxcc$/);
})
test('astxtsxas', () => {
   expect(startFromMiddle('astxtsxas')).toMatch(/^stxts$/);
})
test('aaaa', () => {
   expect(startFromMiddle('aaaa')).toMatch(/^aaaa$/);
})
test('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', () => {
   expect(startFromMiddle('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')).toMatch(/^xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx$/);
})
test('aaabaaaa', () => {
   expect(startFromMiddle('aaabaaaa')).toMatch(/^aaabaaa$/);
})
test('xxxxccxxxxxx', () => {
   expect(startFromMiddle('xxxxccxxxxxx')).toMatch(/^xxxxccxxxx$/);
})
test('xxxxxxccxxxx', () => {
   expect(startFromMiddle('xxxxxxccxxxx')).toMatch(/^xxxxccxxxx$/);
})
test('xxxxxxcccxxxx', () => {
   expect(startFromMiddle('xxxxxxcccxxxx')).toMatch(/^xxxxcccxxxx$/);
})
test('xxxxxxcacxxxx', () => {
   expect(startFromMiddle('xxxxxxcacxxxx')).toMatch(/^xxxxcacxxxx$/);
})
test('caaaaa', () => {
   expect(startFromMiddle('caaaaa')).toMatch(/^aaaaa$/);
})
test('aaaac', () => {
   expect(startFromMiddle('aaaac')).toMatch(/^aaaa$/);
})
test('zabcbazxxx', () => {
   expect(startFromMiddle('zabcbazxxx')).toMatch(/^zabcbaz$/);
})
test('xxxazbcbza', () => {
   expect(startFromMiddle('xxxazbcbza')).toMatch(/^azbcbza$/);
})
test('abbcccbbbcaaccbababcbcabca', () => {
   expect(startFromMiddle('abbcccbbbcaaccbababcbcabca')).toMatch(/^bbcccbb$/);
})
test('aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa', () => {
   expect(startFromMiddle("aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa")).toMatch(/^aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa$/);
})


