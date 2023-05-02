// Greedy algorithm bulbs FAANG Interview

// O(n^2)
function bulbs(n) {
   let cost = 0;
   let execution = 0;
   for (let i = 0; i < n.length; i++) {
      execution++;
      if (n[i] === 0) {
         cost++;
         for (let j = i + 1; j < n.length; j++) {
            n[j] = n[j] === 0 ? 1 : 0;
         }
      }
   }
   return cost;
}

// O(n)
function bulbsGreedy(n) {
   let cost = 0;
   let execution = 0;
   for (let i = 0; i < n.length; i++) {
      execution++;
      if ((cost % 2 === 0) && n[i] === 0) { cost++; continue; }
      if ((cost % 2 === 0) && n[i] === 1) { continue; }

      if ((cost % 2 === 1) && n[i] === 0) { continue; }
      if ((cost % 2 === 1) && n[i] === 1) { cost++; continue; }
   }
   console.log("Execution: ", execution);
   return cost;
}
const series = [0, 1, 0, 1, 1, 0, 1, 1];
const series2 = [0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1]; // result: 22, execution : 379
console.log('RESULT:', blubs(series)); 