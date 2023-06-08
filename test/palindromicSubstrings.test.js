const countSubstrings = require('../main');

test('aaa', () => {
   expect(countSubstrings('aaa')).toEqual(6);
})
test('abc', () => {
   expect(countSubstrings('abc')).toEqual(3);
})
test('aaabbaaa', () => {
   expect(countSubstrings('aaabbaaa')).toEqual(18);
})
test('aaacxxc', () => {
   expect(countSubstrings('aaacxxc')).toEqual(12);
})
/*
   a aa a aaa aa a c x xx x cxxc c
*/
