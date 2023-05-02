// Prepare -> Algorithms -> Recursion -> The Power Sum 
// https://www.hackerrank.com/challenges/the-power-sum/problem?isFullScreen=true

/**
 * Find the number of ways that a given integer, Nth , can be expressed as the sum of the  powers of UNIQUE, natural numbers.
 * @param {number} x : the integer to sum to
 * @param {number} n : the integer power to raise numbers to
 */
function powerSum(x, n) {

   // Find maximum operand [start]
   let combination = [1];
   let sum = 0;
   for (let i = 0; i < x; i++) {
      console.log('combination', combination);
      sum += Math.pow(combination[i], n);
      console.log('sum', sum);
      if (sum > x) {
         break;
      } else {
         combination.push(combination.length + 1);
      }
   }
   combination.pop();
   // Find maximum operand [end]

   console.log('combination', combination);

}

console.log('result: ', powerSum(100, 2));
// max tiap operand 32 loop (power 2 sampai > 1000);

// ======== BELUM SELESAI ========
