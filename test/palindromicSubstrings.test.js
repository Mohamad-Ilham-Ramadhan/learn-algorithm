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
test('aabbaa', () => {
   expect(countSubstrings('aabbaa')).toEqual(11);
})
/*
   aabbaa
   aa 3
   bb 3
   aa 3
   abba 1
   aabbaa 1

   total 11

   aabbaa
   a a aa b b bb a abba a aabbaa aa
*/
test('abxxxbayy', () => {
   expect(countSubstrings('abxxxbayy')).toEqual(15);
})
/*
   abxxxbayy
   a 1
   b 1
   xxx 6
   b 1
   a 1
   yy 3
   bxxxb 1
   abxxba 1
   total: 15
*/
test('abxxxbayya', () => {
   expect(countSubstrings('abxxxbayya')).toEqual(17);
})
/*
   abxxxbayya
   a 1
   b 1
   xxx 6
   b 1
   a 1
   yy 3
   a 1
   bxxxb 1
   abxxba 1
   ayya 1
   total: 17
*/
