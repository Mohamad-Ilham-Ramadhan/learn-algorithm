const coinChange = require('../main')

test('[1,2,5], 11', () => {
   expect(coinChange([1,2,5], 11)).toEqual(3);
})
