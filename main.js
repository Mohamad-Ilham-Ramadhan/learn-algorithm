// Two pointers techniques 

// Two sum 

// naive solution will have time complexity of O(n^2) by checking all possible pairs of numbers in the array,
// but with two pointers technique will have time complexity of O(n);

function twoSum(numbers, target) {
   let result = [];
   let l = 0;
   let ln;
   let r = numbers.length - 1;
   let rn;
   while (l !== r) {
      ln = numbers[l];
      rn = numbers[r];
      const sum = ln + rn;
      if (sum === target) {
         result.push(ln); result.push(rn);
         return result;
      } else if (sum < target) {
         l++;
      } else if (sum > target) {
         r--;
      }
   }
   return result;
}
const numbers = [2, 7, 11, 15];
const target = 9;
console.log(twoSum(numbers, target)); // [2,7]