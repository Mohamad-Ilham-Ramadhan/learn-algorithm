// Prepare -> Algorithms -> Implementation -> Subarray Division
// https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true 

function birthday(s,d,m) {

   let totalShare = 0;
   for (let i = 0; i + m <= s.length; i++) {
    const contiguousSquare = s.slice(i, i + m);
    if (contiguousSquare.reduce((acc, v) => {return acc + v}, 0) === d) {
       totalShare++;
    }
   }
   
   return totalShare;
   
 }
 const s1 = [1,2,1,3,2]; const d1 = 3; const m1 = 2;
 const s2 = [1,1,1,1,1,1]; const d2 = 3; const m2 = 2;
 console.log('RESULT:', birthday(s2, d2, m2)) 