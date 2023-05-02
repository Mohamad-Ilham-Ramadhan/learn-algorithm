// sliding window technique (the dynamic-size sliding window)

// find the minimum length of sub arrays that sum up to (x)

// O(n * 2) or O(n)
function minSubArrayLength(array, x) {
   let result = Infinity;
   let base = 0;
   let subArr = [];

   for (var i = base; i < array.length; i++) {
      if (result === 1) break;
      subArr.push(array[i]);
      const sum = subArr.reduce((acc, i) => acc + i ,0);
      console.log(subArr, sum);
      if (sum === x) {
         result = Math.min(subArr.length, result)
         subArr = [];
         continue;
      }
      if (sum > x) {
         for (let j = 0; j < subArr.length; j++) {
            subArr.shift();
            const sum = subArr.reduce((acc, i) => acc + i ,0);
            console.log('decrease', 'subArr', subArr, 'sum', sum)
            if (sum < x) break;
            if (sum === x) {
               result = Math.min(subArr.length, result)
               subArr = [];
               break;
            }
         }
      }
   }
   return result;
}
const x = 7;
const array = [2,2,3,4,5,6,1];
console.log('result', minSubArrayLength(array, x));