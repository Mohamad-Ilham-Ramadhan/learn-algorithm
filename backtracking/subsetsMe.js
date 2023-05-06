// Backtracking algorithm/technique

// Subsets from LeetCode (medium)

/*
   Given an integer array `nums` of unique elements, return all possible subsets (the power set).

   The solution set must not contain duplicate subsets. Return the solution in any order.

   Example 1:
      Input: nums = [1,2,3]
      Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

   Example 2:
      Input: nums = [0]
      Output: [[],[0]]
   
   Constraints:
      1 <= nums.length <= 10
      -10 <= nums[i] <= 10
      All the numbers of nums are unique.

   Solution Idea:

   Power Set: Power set P(S) of a set S is the set of all subsets of S. For example S = {a, b, c} then P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}.
   If S has n elements in it then P(s) will have 2n elements

   Example:
   Set  = [a,b,c]
   power_set_size = pow(2, 3) = 8
   Run for binary counter = 000 to 111

   Value of Counter            Subset
      000                    -> Empty set
      001                    -> a
      010                    -> b
      011                    -> ab
      100                    -> c
      101                    -> ac
      110                    -> bc
      111                    -> abc

   Angka 1 dibinary berarti ambil dari set. [PERHTIAN] urutan binary dari kanan ke kiri sedangkan set/array dari kiri ke kanan jadi sesuaikan indexnya
*/

/* 
   My own solution not using backtracking because I don't have any idea.

   LeetCode submition:
      Runtime: 61ms, beats 70%.
      Memory: 44.3MB, beats 30.5%
*/
function subsets(nums) {
   let result = [];
   const subsetLength = Math.pow(2, nums.length);

   const binaryLength = (subsetLength - 1).toString(2).length;
   for (let i = 0; i < subsetLength; i++) {
      const binary = (i).toString(2).padStart(binaryLength, '0');
      let subset = [];
      for (let j = 0; j < binary.length; j++) {
         if (binary[j] === '1') {
            const index = (nums.length - 1) - j;
            subset.push(nums[index]);
         }
      }
      result.push(subset.sort((a, b) => a - b));
   }
   return result;
}

const nums = [1, 2, 3, 4];
console.log('subsets:', subsets([3, 2, 4, 1]));


/*
   [3,2,4,1]

   0000 -> []
   0001 -> [3]
   0010 -> [2]
   0011 -> [2,3]
   0100 -> [4]
   0101 -> [3,4]
   0110 -> [2,4]
   0111 -> [2,3,4]
   1000 -> [1]
   1001 -> [1,3]
   1010 -> [1,2]
   1100 -> [3,4]
*/