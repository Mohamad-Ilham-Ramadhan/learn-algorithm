// sliding window technique (the dynamic-size sliding window)

// find the maximum legnth sub array which have all unique characters

// O(2 * n) ==> O(n): meskipun 2 depth loop, ini cuma O(2 * n) karena worst case nya (i) harus loop ke (n) + (j) harus loop ke (n) alias (n) * 2
function longestUniqueSubArray(array) {
   let result = new Set();
   let subArr = new Set();
   let j = 0;
   for (let i = 0; i < array.length; i++) {
      const char = array[i];
      if (subArr.has(char)) {
         while (j <= i) {
            const jChar = array[j];
            if (!subArr.has(char)) break;
            subArr.delete(jChar);
            ++j
         }
      }
      subArr.add(char);
      console.log(subArr.size, result.size);
      result = subArr.size > result.size ? new Set(subArr) : result;
   }
   return {length: result.size, set: result};
}
const array = ['p', 'w', 'w', 'k', 'y', 'x', 'w', 'a', 'b', 'c', 'd', 'e', 'f', 'w', 'z'];

console.log('result', longestUniqueSubArray(array));