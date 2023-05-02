// Two pointer techniques

// Remove duplicates numbers from sorted array 

var removeDuplicates = function(nums) {
   let result = Object.assign([], nums);
   let i = 0;
   let j = i + 1;
   while (i < result.length) {
      while (result[j] === result[i]) {
         result.splice(j, 1);
      }
      i = j;
      j++;
   }
   return result;
};
const nums = [1,1,1,2,2,3,4,4,5]; // [1,2,3,4,5]
const nums2 = [1,1,2]; // [1,2]
console.log('numbers: ', removeDuplicates(nums2));