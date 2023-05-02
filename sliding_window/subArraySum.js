// sliding window technique (the fixed-size sliding window)

// finding sum of subarray (not using slidinw window) 
// O(n * k)
function subArraySum(arr, k) {
   let result = [];
   const last = k;

   // O(n * k)
   for (let i = 0; i <= arr.length - last; i++) {
      let sum = 0;
      for (let j = i; j < k; j++) {
         console.log('i', i, 'arr[j]', arr[j]);
         sum = sum + arr[j];
      }
      result.push(sum);
      k++;
   }

   return result;
}

const arr = [1,2,3,4,5,6]; const k = 3;
console.log('Not sliding window',subArraySum(arr, k));

// using sliding window technique
function subArraySumSlidingWindow(arr, k) {
   let result = [];
   result.push(arr.slice(0, k).reduce((acc, i) => acc + i, 0))

   // O(n)
   for (let i = 0; i < arr.length; i++) {
      if (arr[k + i] === undefined) break;
      const lastSum = result[result.length - 1];
      result.push(lastSum - arr[i] + arr[k + i]);
   }
   return result;
}
console.log('Using sliding window', subArraySumSlidingWindow(arr,k));