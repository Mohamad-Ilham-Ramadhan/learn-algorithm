const startFromMiddle = require('../main');

test('babad', () => {
   // expect(startFromMiddle('babad')).toBe('bab').or.toBe('aba');
   expect(startFromMiddle('babad')).toMatch(/bab|aba/);
});

